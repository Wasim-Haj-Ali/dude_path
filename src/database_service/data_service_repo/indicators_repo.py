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

        # query = f"SELECT * FROM {self.table} WHERE slug = %s;"
        
        # cursor.execute(query, (slug,))

        query = f"SELECT * FROM {self.table} WHERE slug = '{slug}';"

        cursor.execute(query)

        data = cursor.fetchone()

        self.db_object.close_cursor_and_coonnection(cursor=cursor, connection=connection)

        return data


    @benchmark
    def create(self, indicator: Indicator):
        
        connection = self.db_object.connect()

        cursor = connection.cursor()

        # Execute the insert statement with placeholders
        # sql_insert = f"INSERT INTO {self.table} (slug, content) VALUES (%s, %s);"
        # cursor.execute(sql_insert, (indicator.slug, indicator.content))
        sql_insert = f"INSERT INTO {self.table} (slug, name, userslug, content) VALUES ('{indicator.slug}', '{indicator.name}', '{indicator.userslug}', '{indicator.content}');"
        cursor.execute(sql_insert)

        connection.commit()

        # sql_fetch = (f"SELECT * FROM {self.table} WHERE slug = %s;")

        # cursor.execute(sql_fetch, (indicator.slug,))

        sql_fetch = (f"SELECT * FROM {self.table} WHERE slug = '{indicator.slug}';")

        cursor.execute(sql_fetch)
        
        result = cursor.fetchone()

        connection.close()

        return result
    
    
    @benchmark
    def update(self, indicator: Indicator):
        
        connection = self.db_object.connect()
        
        cursor = connection.cursor()

        # Prepared statements
        # sql_update = f"UPDATE {self.table} SET name = %s, content = %s WHERE slug = %s;"
        # cursor.execute(sql_update, (indicator.name, indicator.content))

        sql_update = f"UPDATE {self.table} SET name = '{indicator.name}', content = '{indicator.content}', userslug = '{indicator.userslug}' WHERE slug = '{indicator.slug}';"
        cursor.execute(sql_update)

        connection.commit()

        # sql_fetch = (f"SELECT * FROM {self.table} WHERE slug = %s;")

        # cursor.execute(sql_fetch, (indicator.slug,))

        sql_fetch = (f"SELECT * FROM {self.table} WHERE slug = '{indicator.slug}';")

        cursor.execute(sql_fetch)
        
        result = cursor.fetchone()

        connection.close()

        return result


    @benchmark
    def delete(self, slug: str):
        
        connection = self.db_object.connect()
        
        cursor = connection.cursor()

        # Execute the delete statement with placeholders
        # sql = f"DELETE FROM {self.table} WHERE slug = %s;"
        # cursor.execute(sql, (slug,))

        sql = f"DELETE FROM {self.table} WHERE slug = '{slug}';"
        cursor.execute(sql)
        
        connection.commit()

        self.db_object.close_cursor_and_coonnection(cursor=cursor, connection=connection)
        
        return True

