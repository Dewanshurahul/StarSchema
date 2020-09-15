import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

list_of_alter_statement = []

for stmt in list_of_alter_statement:
    db_cursor.execute(stmt)