import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Create table DimStores(StoreID int primary key," \
        "StoreAltID varchar(10)," \
        "StoreName varchar(100)," \
        "StoreLocation varchar(100)," \
        "City varchar(100)," \
        "State varchar(100)," \
        "Country varchar(100))"

db_cursor.execute(query)
