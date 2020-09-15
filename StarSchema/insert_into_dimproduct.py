import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Insert into DimProduct(ProductKey,ProductAltKey,ProductName, ProductActualCost, ProductSalesCost) values " \
        "(100,'ITM-001','Wheat Floor 1kg',5.50,6.50)," \
        "(101,'ITM-002','Rice Grains 1kg',22.50,24)," \
        "(102,'ITM-003','SunFlower Oil 1 ltr',42,43.5)," \
        "(103,'ITM-004','Nirma Soap',18,20)," \
        "(104,'ITM-005','Arial Washing Powder 1kg',135,139)"

db_cursor.execute(query)
db_connection.commit()
