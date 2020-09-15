import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Insert into DimCustomer(" \
        "CustomerID,CustomerAltID,CustomerName,Gender) values " \
        "(1,'IMI-001','Henry Ford','M')," \
        "(2,'IMI-002','Bill Gates','M')," \
        "(3,'IMI-003','Muskan Shaikh','F')," \
        "(4,'IMI-004','Richard Thrubin','M')," \
        "(5,'IMI-005','Emma Wattson','F')"

db_cursor.execute(query)
db_connection.commit()
