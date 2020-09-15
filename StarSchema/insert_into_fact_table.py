import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Insert into FactProductSales(TransactionId," \
        "SalesInvoiceNumber,SalesDateKey," \
        "SalesTimeKey,SalesTimeAltKey,StoreID,CustomerID,ProductID ," \
        "SalesPersonID,Quantity,ProductActualCost,SalesTotalCost,Deviation)values" \
        "(101,1,20130101,44347,121907,50,1,100,1,2,11,13,2)," \
        "(102,1,20130101,44347,121907,50,1,101,1,1,22.50,24,1.5)," \
        "(103,1,20130101,44347,121907,50,1,102,1,1,42,43.5,1.5)," \
        "(104,2,20130101,44519,122159,50,2,103,1,1,42,43.5,1.5)," \
        "(105,2,20130101,44519,122159,50,2,104,1,3,54,60,6)," \
        "(106,3,20130101,52415,143335,50,3,102,2,2,11,13,2)," \
        "(107,3,20130101,52415,143335,50,3,103,2,1,42,43.5,1.5)," \
        "(108,3,20130101,52415,143335,50,3,104,2,3,54,60,6)," \
        "(109,3,20130101,52415,143335,50,3,104,2,1,135,139,4)," \
        "(110,4,20130102,44347,121907,50,1,101,1,2,11,13,2)," \
        "(111,4,20130102,44347,121907,50,1,102,1,1,22.50,24,1.5)," \
        "(112,5,20130102,44519,122159,50,2,103,1,1,42,43.5,1.5)," \
        "(113,5,20130102,44519,122159,50,2,104,1,3,54,60,6)," \
        "(114,6,20130102,52415,143335,50,3,102,2,2,11,13,2)," \
        "(115,6,20130102,52415,143335,50,3,104,2,1,135,139,4)," \
        "(116,7,20130102,44347,121907,51,1,104,3,3,54,60,6)," \
        "(117,7,20130102,44347,121907,51,1,104,3,1,135,139,4)," \
        "(118,8,20130103,59326,162846,50,1,103,1,2,84,87,3)," \
        "(119,8,20130103,59326,162846,50,1,104,1,3,54,60,3)," \
        "(220,9,20130103,59349,162909,52,2,101,1,1,5.5,6.5,1)," \
        "(221,9,20130103,59349,162909,52,2,102,1,1,22.50,24,1.5)," \
        "(222,10,20130103,67390,184310,50,3,101,2,2,11,13,2)," \
        "(223,10,20130103,67390,184310,52,3,104,2,3,54,60,6)," \
        "(224,11,20130103,74877,204757,51,1,102,3,1,5.5,6.5,1)," \
        "(225,11,20130103,74877,204757,51,1,103,3,1,42,43.5,1.5)"

db_cursor.execute(query)
db_connection.commit()
