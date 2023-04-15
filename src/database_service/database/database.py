import json
import psycopg2

from src.decorators.timer import benchmark


class Database:
    
    database: str
    database_object = None

    # Singleton
    def __new__(cls):
        if cls.database_object is None:
            cls.database_object = super(Database, cls).__new__(cls)
        return cls.database_object


    def __init__(self):
        with open("src/config.json") as json_file:
            config = json.load(json_file)

        database_service = config["database_service"]
        
        self.database = database_service["database_name"]
    

    @benchmark
    @staticmethod
    def get_database_object():

        if Database.database_object == None:
            return Database()
        
        return Database.database_object


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
    def close_cursor_and_coonnection(self, cursor, connection):
        
        try:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

        except psycopg2.DatabaseError as error:
            connection.rollback()
            print(error)
    

