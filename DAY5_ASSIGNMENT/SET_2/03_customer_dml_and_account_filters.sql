USE BankBranchDB;
GO

-- Customer INSERT, SELECT, UPDATE, DELETE as demonstrated in the assignment
INSERT INTO Customer (Customer_Name, Address) VALUES
('Harshith', 'Chennai'),
('Rahul', 'Bangalore'),
('Priya', 'Hyderabad');

SELECT * FROM Customer;
SELECT * FROM Customer WHERE Customer_Name = 'Harshith';

UPDATE Customer
SET Address = 'Coimbatore'
WHERE Customer_Name = 'Rahul';
SELECT * FROM Customer;

DELETE FROM Customer
WHERE Customer_Name = 'Priya';
SELECT * FROM Customer;
GO

-- Add Opened_Date to support the previous-quarter query extension
IF COL_LENGTH('Account', 'Opened_Date') IS NULL
    ALTER TABLE Account ADD Opened_Date DATE NULL;
GO
-- Sample dates are illustrative and support running the quarter filter.
UPDATE Account SET Opened_Date = '2026-08-15' WHERE Account_No = 'ACC1001';
UPDATE Account SET Opened_Date = '2026-09-02' WHERE Account_No = 'ACC1002';
UPDATE Account SET Opened_Date = '2026-10-12' WHERE Account_No = 'ACC1003';
UPDATE Account SET Opened_Date = '2026-07-03' WHERE Account_No = 'ACC1004';
GO

DECLARE @Today DATE = CAST(GETDATE() AS DATE);
DECLARE @ThisQuarterStart DATE =
    DATEFROMPARTS(YEAR(@Today), ((DATEPART(QUARTER, @Today)-1)*3)+1, 1);
DECLARE @LastQuarterStart DATE = DATEADD(QUARTER, -1, @ThisQuarterStart);

SELECT *
FROM Account
WHERE Opened_Date >= @LastQuarterStart
  AND Opened_Date < @ThisQuarterStart
  AND Balance > 50000;

-- AND
SELECT * FROM Account WHERE Balance >= 10000 AND Account_Type = 'Savings';
-- OR
SELECT * FROM Account WHERE Account_Type = 'Savings' OR Account_Type = 'Current';
-- IN
SELECT * FROM Account WHERE Branch_ID IN (1,2,3);
-- BETWEEN
SELECT * FROM Account WHERE Balance BETWEEN 10000 AND 100000;
GO
