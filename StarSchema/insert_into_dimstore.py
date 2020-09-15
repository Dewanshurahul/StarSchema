import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Insert into DimStores(StoreID,StoreAltID,StoreName,StoreLocation,City,State,Country ) values" \
        "(50,'LOC-A1','X-Mart','S.P. RingRoad','Ahmedabad','Guj','India')," \
        "(51,'LOC-A2','X-Mart','Maninagar','Ahmedabad','Guj','India')," \
        "(52,'LOC-A3','X-Mart','Sivranjani','Ahmedabad','Guj','India');"

db_cursor.execute(query)
db_connection.commit()
