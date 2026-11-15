USE RetailInventoryDB;
GO
INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Phone) VALUES
('S01','ABC Traders','9876501001'),
('S02','TechSource','9876501002'),
('S03','Vision Supplies','9876501003'),
('S04','Comfort Furnishers','9876501004'),
('S05','DataWorld','9876501005'),
('S06','Sound Planet','9876501006'),
('S07','Office Machines Co','9876501007'),
('S08','Global Electronics','9876501008'),
('S09','Prime Distributors','9876501009'),
('S10','Smart Retailers','9876501010'),
('S11','New Supplier','9876501234');

INSERT INTO Product (SKU, Product_Name, Category, Supplier_ID) VALUES
('P101','Laptop','Electronics','S01'),
('P102','Wireless Mouse','Accessories','S01'),
('P103','Mechanical Keyboard','Accessories','S02'),
('P104','Monitor','Electronics','S03'),
('P105','USB-C Hub','Accessories','S02'),
('P106','Webcam','Electronics','S03'),
('P107','Office Chair','Furniture','S04'),
('P108','Desk Lamp','Furniture','S04'),
('P109','External SSD','Storage','S05'),
('P110','USB Flash Drive','Storage','S05');

INSERT INTO Inventory (SKU, Warehouse, Quantity, Reorder_Level) VALUES
('P101','Chennai',20,5),('P101','Bengaluru',10,5),
('P102','Chennai',50,10),('P102','Hyderabad',30,10),
('P103','Bengaluru',15,5),('P103','Chennai',9,5),
('P104','Chennai',12,4),('P104','Bengaluru',7,4),
('P105','Hyderabad',8,5),('P105','Chennai',13,5),
('P106','Hyderabad',25,8),
('P107','Chennai',6,3),('P107','Bengaluru',4,3),
('P108','Bengaluru',18,6),
('P109','Chennai',14,5),('P109','Hyderabad',9,5),
('P110','Bengaluru',60,15);

-- Joined view for product, supplier, and stock details
SELECT P.SKU, P.Product_Name, S.Supplier_Name, I.Warehouse, I.Quantity
FROM Product P
JOIN Supplier S ON P.Supplier_ID = S.Supplier_ID
JOIN Inventory I ON P.SKU = I.SKU;
