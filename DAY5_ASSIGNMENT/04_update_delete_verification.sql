USE RetailInventoryDB;
GO
-- UPDATE Supplier phone for S01 and verify
SELECT * FROM Supplier WHERE Supplier_ID = 'S01';
UPDATE Supplier
SET Supplier_Phone = '9876509999'
WHERE Supplier_ID = 'S01';
SELECT * FROM Supplier WHERE Supplier_ID = 'S01';
GO

-- DELETE discontinued product SKU inventory rows and verify before/after
SELECT * FROM Inventory WHERE SKU = 'P109';
DELETE FROM Inventory WHERE SKU = 'P109';
SELECT * FROM Inventory WHERE SKU = 'P109';
GO
