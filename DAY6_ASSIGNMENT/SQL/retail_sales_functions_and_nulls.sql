/*
Day 6 – Set 1: Retail Sales Reporting
Student: Samberapu Ayyappa
SQL Server

This script contains SQL statements for Tasks 2 and 3, reconstructed from the
assignment document. Task 1's eight report query screenshots/queries are retained
in the source DOCX and should be transcribed there if a fully runnable set is needed.
*/
USE RetailSalesDB;
GO

-- Task 2.1: Convert customer names to uppercase
SELECT UPPER(CustomerName) AS UppercaseName
FROM Customers;
GO

-- Task 2.2: Concatenate customer name and city
SELECT CONCAT(CustomerName, ' - ', City) AS CustomerDetails
FROM Customers;
GO

-- Task 2.3: Calculate date difference from the assignment's reference date
SELECT OrderID,
       DATEDIFF(DAY, OrderDate, '2026-04-01') AS DaysDifference
FROM Orders;
GO

-- Task 2.4: Format order date
SELECT OrderID,
       FORMAT(OrderDate, 'dd-MM-yyyy') AS FormattedDate
FROM Orders;
GO

-- Task 2.5: Calculate price including 18% tax, rounded to 2 decimals
SELECT ProductName,
       UnitPrice,
       ROUND(UnitPrice * 1.18, 2) AS PriceWithTax
FROM Products;
GO

-- Task 3: Demonstrate NULL handling in aggregate functions
-- Insert a NULL payment value only if an appropriate row can be added
-- according to the Payments table's required columns/constraints.
-- Example (adapt PaymentID and other required fields to your schema):
-- INSERT INTO Payments (PaymentID, Amount) VALUES (999, NULL);

SELECT COUNT(*) AS TotalRows,
       COUNT(Amount) AS NonNullAmountCount,
       AVG(Amount) AS AverageAmount
FROM Payments;
GO
