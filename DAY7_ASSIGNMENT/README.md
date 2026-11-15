# Day 7 – Set 1: Logistics Shipment Analysis

**Student:** Samberapu Ayyappa  
**Database:** LogisticsDB  
**Technologies:** SQL Server 2025, MongoDB 8.0

## Assignment overview
This project analyzes logistics shipments across hubs, carriers, customers, employees, and delivery events. It demonstrates SQL joins, subqueries, nested queries, and MongoDB `$lookup` aggregation pipelines.

## Repository contents
- `Day7_Set1_Logistics_Shipment_Analysis_Ayyappa.docx` — assignment document
- `advanced_reports.sql` — SQL Server database/table setup and query script (Parts A–E)
- `reports.js` — MongoDB sample collection inserts and `$lookup` pipelines (Parts F–G)

## How to use
### SQL Server
1. Open SQL Server Management Studio (SSMS).
2. Open `advanced_reports.sql`.
3. Run the database setup and table creation first.
4. Execute query sections sequentially; ensure the database `LogisticsDB` is selected.

### MongoDB
1. Open MongoDB Compass or mongosh.
2. Select/use the `LogisticsDB` database.
3. Run relevant commands in `reports.js` in order. If sample data is already inserted, avoid rerunning `insertMany` blocks to prevent duplicate-key errors.

## Topics covered
- INNER, LEFT, FULL OUTER, and SELF JOIN
- `IN`, `EXISTS`, `ANY`, and `ALL` subqueries
- Rewriting subqueries using joins
- Second-highest shipping cost per hub using a nested query
- MongoDB collections and `$lookup` aggregations

## Note
The provided assignment document includes its own explanatory text and evidence screenshots. This repository includes the source assignment plus extracted script files for convenient code access.
