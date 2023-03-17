import mysql.connector

from app.decorators.timer import benchmark
from app.entities import Indicator


TABLE = "indicators"

@benchmark
def connect():
    
    connection = mysql.connector.connect( user="root", password="root", host="mysql", port="3308", database="dude_path_database")
    
    print("Connect to database successfully!")
    
    return connection


@benchmark
def close_connection(connection: mysql.connector):
    
    connection.close()
    
    return
    

@benchmark
def get_all_indicators():
    
    connection = connect()
    
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {TABLE}")

    data = cursor.fetchall()

    close_connection(connection)
    
    return data


@benchmark
def get_indicator_by_slug(slug: str):
    
    connection = connect()
    
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {TABLE} WHERE id = {slug};")

    data = cursor.fetchall()

    close_connection(connection)
    
    return data



@benchmark
# def create_indicator(indicator: Indicator):  # parameter prepared for future use. At the moment not necessary
def create_indicator():
    
    connection = connect()
    
    cursor = connection.cursor()

    # Execute the insert statement
    cursor.execute(f'INSERT INTO {TABLE}(slug, content) VALUES ("abc123", "Hello abc123");')
    
    # Retrieve the inserted indicator
    cursor.execute(f'SELECT * FROM {TABLE} WHERE slug = "abc123";')
    
    result = cursor.fetchone()
    
    close_connection(connection)
    
    return result
