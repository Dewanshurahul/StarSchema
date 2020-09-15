import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()


query = "Create table DimProduct (ProductKey int primary key," \
        "ProductAltKey varchar(10)," \
        "ProductName varchar(100)," \
        "ProductActualCost int," \
        "ProductSalesCost int)"

db_cursor.execute(query)
