import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Insert into DimSalesPerson(SalesPersonID,SalesPersonAltID,SalesPersonName,StoreID,City,State,Country )values " \
        "(1,'SP-DMSPR1','Ashish',1,'Ahmedabad','Guj','India')," \
        "(2,'SP-DMSPR2','Ketan',1,'Ahmedabad','Guj','India')," \
        "(3,'SP-DMNGR1','Srinivas',2,'Ahmedabad','Guj','India')," \
        "(4,'SP-DMNGR2','Saad',2,'Ahmedabad','Guj','India')," \
        "(5,'SP-DMSVR1','Jasmin',3,'Ahmedabad','Guj','India')," \
        "(6,'SP-DMSVR2','Jacob',3,'Ahmedabad','Guj','India')"

db_cursor.execute(query)
db_connection.commit()
