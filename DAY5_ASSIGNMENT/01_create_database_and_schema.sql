IF DB_ID('RetailInventoryDB') IS NULL
    CREATE DATABASE RetailInventoryDB;
GO
USE RetailInventoryDB;
GO

CREATE TABLE Supplier (
    Supplier_ID VARCHAR(10) PRIMARY KEY,
    Supplier_Name VARCHAR(100) NOT NULL,
    Supplier_Phone VARCHAR(15) NOT NULL UNIQUE
);

CREATE TABLE Product (
    SKU VARCHAR(10) PRIMARY KEY,
    Product_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Supplier_ID VARCHAR(10) NOT NULL,
    CONSTRAINT FK_Product_Supplier FOREIGN KEY (Supplier_ID)
        REFERENCES Supplier(Supplier_ID)
);

CREATE TABLE Inventory (
    SKU VARCHAR(10) NOT NULL,
    Warehouse VARCHAR(50) NOT NULL,
    Quantity INT NOT NULL,
    Reorder_Level INT NOT NULL DEFAULT 0,
    CONSTRAINT PK_Inventory PRIMARY KEY (SKU, Warehouse),
    CONSTRAINT FK_Inventory_Product FOREIGN KEY (SKU) REFERENCES Product(SKU),
    CONSTRAINT CK_Inventory_Quantity CHECK (Quantity >= 0),
    CONSTRAINT CK_Inventory_Reorder CHECK (Reorder_Level >= 0)
);

CREATE TABLE ProductReview (
    Review_ID INT IDENTITY(1,1) PRIMARY KEY,
    SKU VARCHAR(10) NOT NULL,
    Customer_Name VARCHAR(100) NOT NULL,
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Review_Text NVARCHAR(1000),
    CONSTRAINT FK_ProductReview_Product FOREIGN KEY (SKU) REFERENCES Product(SKU)
);

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';
