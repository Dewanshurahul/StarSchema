import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Create table DimCustomer(" \
        "CustomerID int primary key," \
        "CustomerAltID varchar(10)," \
        "CustomerName varchar(50)," \
        "Gender varchar(20))"
db_cursor.execute(query)
