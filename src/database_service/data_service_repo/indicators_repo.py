import json

from src.decorators.timer import benchmark
from src.entities.Indicator import Indicator
from src.database_service.database.database import Database


class IndicatorsRepo:
    
    def __init__(self):
        # Remember that this path is inside the docker container
        with open("src/config.json") as json_file:
            config = json.load(json_file)

        database_service = config["database_service"]

        self.database_name = database_service["database_name"]
        self.table = database_service["indicators_table_name"]
        self.db_object = Database.get_database_object()

    @benchmark
    def get_all(self):
        """"""
        connection = self.db_object.connect()

        cursor = connection.cursor()
        
        cursor.execute(f"SELECT * FROM {self.table};")

        data = cursor.fetchall()
        
        self.db_object.close_cursor_and_coonnection(cursor=cursor, connection=connection)

        return data
    

    @benchmark
    def get_one(self, slug: str):
        """"""
        connection = self.db_object.connect()

        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {self.table} WHERE slug = {slug};")

        data = cursor.fetchall()

        self.db_object.close_cursor_and_coonnection(cursor=cursor, connection=connection)

        return data


    @benchmark
    def create(self, data: dict):
        # Validate the data
        indicator = Indicator(**data)

        connection = self.db_object.connect()
        
        cursor = connection.cursor()

        # Execute the insert statement with placeholders
        sql_insert = f"INSERT INTO {self.table} (slug, content) VALUES (%s, %s);"
        cursor.execute(sql_insert, (indicator.slug, indicator.content))

        connection.commit()

        sql_fetch = (f"SELECT * FROM {self.table} WHERE slug = %s;")

        cursor.execute(sql_fetch, (indicator.slug,))
        
        result = cursor.fetchone()

        connection.close()

        return result


    @benchmark
    def delete(self, slug: str):
        
        connection = self.db_object.connect()
        
        cursor = connection.cursor()

        # Execute the delete statement with placeholders
        sql = f"DELETE FROM {self.table} WHERE slug = %s;"
        cursor.execute(sql, (slug,))
        
        connection.commit()

        self.db_object.close_cursor_and_coonnection(cursor=cursor, connection=connection)
        
        return True

