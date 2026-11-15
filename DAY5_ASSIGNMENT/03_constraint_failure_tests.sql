USE RetailInventoryDB;
GO
-- Run each test separately. Each INSERT below is expected to fail.
-- Test 1: Duplicate Supplier_ID (PK)
INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Phone)
VALUES ('S01','Duplicate Supplier','9876509999');
GO
-- Test 2: Supplier_Name is mandatory (NOT NULL)
INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Phone)
VALUES ('S12',NULL,'9876501020');
GO
-- Test 3: Duplicate phone number (UNIQUE)
INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Phone)
VALUES ('S12','Phone Duplicate','9876501001');
GO
-- Test 4: Negative quantity (CHECK)
INSERT INTO Inventory (SKU, Warehouse, Quantity, Reorder_Level)
VALUES ('P101','Mumbai',-10,5);
GO
-- Test 5: Invalid supplier reference (FK)
INSERT INTO Product (SKU, Product_Name, Category, Supplier_ID)
VALUES ('P111','Test Product','Electronics','S99');
GO
