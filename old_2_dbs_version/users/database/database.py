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
            print("_________________STARTED CONNECTING________________")
            connection = psycopg2.connect(
                dbname="usersdatabase",
                user="postgres",
                password="postgres",
                port="5432",
                host="usersdatabase"
            )
            print("Connect to database successfully!")
            print("Connect obj in connect(): ", connection)
            return connection
        except Exception as exception:
            print(f"The connection failed. Error message: {exception}")
            return None

    @benchmark
    def get_all(self):
        connection = self.connect()
        print("Connect obj in get_all(): ", connection)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table};")
        data = cursor.fetchall()
        connection.close()
        return data

    @benchmark
    def get_one(self, slug: str):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE slug = {slug};")
        data = cursor.fetchall()
        connection.close()
        return data

    @benchmark
    def create(self, data: dict):
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
    def delete(self, slug: str):
        
        connection = self.connect()
        
        cursor = connection.cursor()

        # Execute the delete statement with placeholders
        sql = f"DELETE FROM {self.table} WHERE slug = %s;"
        cursor.execute(sql, (slug,))
        
        connection.commit()

        connection.close()
        
        return True

