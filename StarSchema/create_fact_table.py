import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="admin", passwd="Admin@123", database="Sales_DW")
db_cursor = db_connection.cursor()

query = "Create Table FactProductSales(TransactionId bigint primary key," \
        "SalesInvoiceNumber int," \
        "SalesDateKey int," \
        "SalesTimeKey int," \
        "SalesTimeAltKey int," \
        "StoreID int NOT NULL," \
        "CustomerID int NOT NULL," \
        "ProductID int NOT NULL," \
        "SalesPersonID int NOT NULL," \
        "Quantity float," \
        "SalesTotalCost int," \
        "ProductActualCost int," \
        "Deviation float)"
        # "CONSTRAINT FK_StoreID FOREIGN KEY (StoreID) REFERENCES DimStores(StoreID)"
        # "CONSTRAINT FK_SalesPersonID FOREIGN KEY (SalesPersonID) REFERENCES DimSalesPerson(SalesPersonID)" \
        # "CONSTRAINT FK_CustomerID FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID)" \
        # "CONSTRAINT FK_ProductKey FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductKey)"

db_cursor.execute(query)
