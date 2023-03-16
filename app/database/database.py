import mysql.connector

connection = mysql.connector.connect(
    user="root", password="root", host="mysql", port="3306", database="db"
)

print("Connect to database successfully!")

cursor = connection.cursor()

table = "indicators"

cursor.execute(f"SELECT * FROM {table}")

data = cursor.fetchall()
connection.close()

print(f"Data of the table {table}: ")
print(data)
print("____________FINISHED____________")
