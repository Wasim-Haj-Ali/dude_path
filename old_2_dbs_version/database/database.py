import psycopg2

from src.decorators.timer import benchmark
from src.entities.Indicator import Indicator


class Database:
    
    def __init__(self, database, table):
        self.database = database
        self.table = table

    @benchmark
    def connect(self):
        try:
            # These values should match the values that are specified in the environment variables of the dude_path_app container in the docker-compose.yml file
            connection = psycopg2.connect(user="postgres", password="postgres", host="dude_path_database", dbname=self.database)
            print("Connect to database successfully!")
            return connection
        except Exception as exception:
            print(f"The connection failed. Error message: {exception}")
            return None

    @benchmark
    def get_all_indicators(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table};")
        data = cursor.fetchall()
        connection.close()
        return data

    @benchmark
    def get_indicator(self, slug: str):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE slug = {slug};")
        data = cursor.fetchall()
        connection.close()
        return data

    @benchmark
    def create_indicator(self, data: dict):
        # Validate the data
        indicator = Indicator(**data)

        connection = self.connect()
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
    def delete_indicator(self, slug: str):
        
        connection = self.connect()
        
        cursor = connection.cursor()

        # Execute the delete statement with placeholders
        sql = f"DELETE FROM {self.table} WHERE slug = %s;"
        cursor.execute(sql, (slug,))
        
        connection.commit()

        connection.close()
        
        return True

