-- PART A – SQL SERVER DATABASE AND TABLE SETUP
Create LogisticsDB and the six related tables. Foreign keys connect shipments to customers, hubs, carriers and employees, and delivery events to shipments.

-- A.1 Table structure
-- A.2 Database and table creation script
CREATE DATABASE LogisticsDB;
GO
USE LogisticsDB;
GO
CREATE TABLE Hubs (

);
CREATE TABLE Carriers (

);
CREATE TABLE Customers (

);
CREATE TABLE Employees (

);
CREATE TABLE Shipments (

);
CREATE TABLE DeliveryEvents (     EventID INT PRIMARY KEY, ShipmentID INT, EventDate DATE,

);

-- A.3 Sample data
-- Additional records inserted for Arun:
INSERT INTO Shipments VALUES

GO


-- Figure 1. SQL Server database setup and sample table data visible in the results grid.
-- PART B – TEN SQL BUSINESS QUESTIONS USING JOINS
-- The queries below combine shipment, customer, carrier, hub, employee and delivery-event information.
-- Query 1 – Shipment details with customer, carrier and hub
INNER JOIN
SELECT S.ShipmentID, C.CustomerName, CR.CarrierName, H.HubName, S.Status
FROM Shipments S
INNER JOIN Customers C ON S.CustomerID = C.CustomerID
INNER JOIN Carriers CR ON S.CarrierID = CR.CarrierID
INNER JOIN Hubs H ON S.HubID = H.HubID;

-- Query 2 – Shipments delayed by more than two days
INNER JOIN
SELECT S.ShipmentID, CR.CarrierName, S.ExpectedDeliveryDate,
S.ActualDeliveryDate,

FROM Shipments S
INNER JOIN Carriers CR ON S.CarrierID = CR.CarrierID
WHERE S.ActualDeliveryDate IS NOT NULL
AND DATEDIFF(DAY, S.ExpectedDeliveryDate, S.ActualDeliveryDate) > 2;

-- Query 3 – Hubs with no outbound shipments
LEFT JOIN
SELECT H.HubID, H.HubName, S.ShipmentID
FROM Hubs H LEFT JOIN Shipments S ON H.HubID = S.HubID
WHERE S.ShipmentID IS NULL;

-- Query 4 – All carriers and shipment counts
FULL OUTER JOIN
SELECT CR.CarrierName, X.TotalShipments
FROM Carriers CR
FULL OUTER JOIN (
SELECT CarrierID, COUNT(*) AS TotalShipments
FROM Shipments GROUP BY CarrierID
) X ON CR.CarrierID = X.CarrierID;

-- Query 5 – Employees and their supervisors
SELECT E.EmployeeName AS Employee, M.EmployeeName AS Supervisor
FROM Employees E
LEFT JOIN Employees M ON E.SupervisorID = M.EmployeeID;

-- Query 6 – Customers and their shipments
LEFT JOIN
SELECT C.CustomerName, S.ShipmentID, S.Status
FROM Customers C LEFT JOIN Shipments S ON C.CustomerID = S.CustomerID;

-- Query 7 – Shipments with delivery events
INNER JOIN
SELECT S.ShipmentID, D.EventType, D.EventDate, D.Location
FROM Shipments S
INNER JOIN DeliveryEvents D ON S.ShipmentID = D.ShipmentID;

-- Query 8 – Shipments without delivery events
LEFT JOIN
SELECT S.ShipmentID, S.Status
FROM Shipments S
LEFT JOIN DeliveryEvents D ON S.ShipmentID = D.ShipmentID
WHERE D.EventID IS NULL;

-- Query 9 – Average delivery delay by carrier
LEFT JOIN
SELECT CR.CarrierName,

AS DECIMAL(10,2))) AS AverageDelay
FROM Carriers CR
LEFT JOIN Shipments S ON CR.CarrierID = S.CarrierID
AND S.ActualDeliveryDate IS NOT NULL
GROUP BY CR.CarrierName;

-- Query 10 – Hub-wise employee and shipment details
INNER JOIN + LEFT JOIN
SELECT H.HubName, E.EmployeeName, S.ShipmentID, S.ShippingCost
FROM Hubs H
INNER JOIN Employees E ON H.HubID = E.HubID
LEFT JOIN Shipments S ON E.EmployeeID = S.EmployeeID
ORDER BY H.HubName; Join selection

-- Evidence (Queries 1–10)
-- Figure 2. SQL Server JOIN query execution and result grids.
-- PART C – SUBQUERIES USING IN, EXISTS, ANY AND ALL
-- Query 11 – Customers who shipped to every hub
SELECT CustomerName
FROM Customers
WHERE CustomerID IN (
SELECT CustomerID
FROM Shipments
GROUP BY CustomerID
HAVING COUNT(DISTINCT HubID) = (SELECT COUNT(*) FROM Hubs)
);

-- Query 12 – Customers who shipped to every hub
SELECT C.CustomerID, C.CustomerName
FROM Customers C
WHERE NOT EXISTS (
SELECT 1 FROM Hubs H
WHERE NOT EXISTS (
SELECT 1 FROM Shipments S
WHERE S.CustomerID = C.CustomerID AND S.HubID = H.HubID
)
);

-- Query 13 – Carrier average delay greater than ANY returned average
SELECT CR.CarrierName,

AS DECIMAL(10,2))) AS AverageDelay
FROM Carriers CR JOIN Shipments S ON CR.CarrierID = S.CarrierID
WHERE S.ActualDeliveryDate IS NOT NULL
GROUP BY CR.CarrierID, CR.CarrierName
HAVING AVG(CAST(DATEDIFF(DAY, S.ExpectedDeliveryDate, S.ActualDeliveryDate)
AS DECIMAL(10,2))) > ANY (
SELECT AVG(CAST(DATEDIFF(DAY, ExpectedDeliveryDate, ActualDeliveryDate)
AS DECIMAL(10,2)))
FROM Shipments WHERE ActualDeliveryDate IS NOT NULL
);

-- Query 14 – Carrier average delay greater than ALL returned averages
SELECT CR.CarrierName,        AVG(CAST(DATEDIFF(DAY, S.ExpectedDeliveryDate, S.ActualDeliveryDate)
AS DECIMAL(10,2))) AS AverageDelay FROM Carriers CR JOIN Shipments S ON CR.CarrierID = S.CarrierID
WHERE S.ActualDeliveryDate IS NOT NULL
GROUP BY CR.CarrierID, CR.CarrierName
HAVING AVG(CAST(DATEDIFF(DAY, S.ExpectedDeliveryDate, S.ActualDeliveryDate)
AS DECIMAL(10,2))) > ALL (     SELECT AVG(CAST(DATEDIFF(DAY, ExpectedDeliveryDate, ActualDeliveryDate)
AS DECIMAL(10,2)))
FROM Shipments WHERE ActualDeliveryDate IS NOT NULL
);

-- How each operator works
-- Figure 3. SQL Server carrier-delay subquery output (ALL form) shown in the results grid.
-- PART D – REWRITE TWO SUBQUERIES AS JOINS
-- Query 15 rewrites the all-hubs customer test using an INNER JOIN and GROUP BY. Query 16 joins carriers to shipments and compares each carrier's average delay with the overall average.
-- Query 15 – All-hubs customer test rewritten using JOIN
INNER JOIN + GROUP BY (replaces Queries 11 and 12)
SELECT C.CustomerID, C.CustomerName
FROM Customers C
INNER JOIN Shipments S ON C.CustomerID = S.CustomerID
GROUP BY C.CustomerID, C.CustomerName
HAVING COUNT(DISTINCT S.HubID) = (SELECT COUNT(*) FROM Hubs);

-- Query 16 – Carrier average delay compared with overall average
INNER JOIN + GROUP BY (replaces Queries 13 and 14)
SELECT CR.CarrierName,

AS DECIMAL(10,2))) AS AverageDelay
FROM Carriers CR
INNER JOIN Shipments S ON CR.CarrierID = S.CarrierID
WHERE S.ActualDeliveryDate IS NOT NULL
GROUP BY CR.CarrierID, CR.CarrierName
HAVING AVG(CAST(DATEDIFF(DAY, S.ExpectedDeliveryDate, S.ActualDeliveryDate)
AS DECIMAL(10,2))) > (
SELECT AVG(CAST(DATEDIFF(DAY, ExpectedDeliveryDate, ActualDeliveryDate)
AS DECIMAL(10,2)))
FROM Shipments WHERE ActualDeliveryDate IS NOT NULL
);

-- Readability note
-- The JOIN versions make the relationship between tables explicit. The grouped customer query is useful for counting distinct hubs; the carrier query keeps the carrier-level grouping visible.
-- Figure 4. SQL Server comparison query output shown in the results grid.
-- Evidence status. The submitted screenshots show the carrier comparison result. The screenshot set does not show the post-insert execution result for the all-hubs customer query; the expected matching customer in the supplied sample data is Arun.
-- PART E – NESTED SUBQUERY: SECOND-HIGHEST SHIPPING COST PER HUB
-- The innermost query finds the maximum shipping cost for the current hub. The outer nested query finds the maximum cost that is lower than that value. This returns the second-highest distinct cost for each hub that has at least two distinct shipping costs.
SELECT H.HubName,

FROM Hubs H
INNER JOIN Shipments S ON H.HubID = S.HubID
WHERE S.ShippingCost = (
SELECT MAX(S2.ShippingCost)
FROM Shipments S2
WHERE S2.HubID = H.HubID
AND S2.ShippingCost < (
SELECT MAX(S3.ShippingCost)
FROM Shipments S3
WHERE S3.HubID = H.HubID
)
);


-- Figure 5. SQL Server second-highest shipping cost per hub; the result grid shows Chennai, Hyderabad and Bangalore.