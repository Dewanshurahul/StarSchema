import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Create table DimSalesPerson(SalesPersonID int primary key," \
        "SalesPersonAltID varchar(10)," \
        "SalesPersonName varchar(100)," \
        "StoreID int,City varchar(100)," \
        "State varchar(100)," \
        "Country varchar(100))"

db_cursor.execute(query)
