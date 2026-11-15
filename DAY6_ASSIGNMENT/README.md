# Day 6 – Set 1: Retail Sales Reporting
**Student: Samberapu Ayyappa**  
**Topics: SQL Server 2025 and MongoDB 8.0**

This repository contains the Day 6 assignment source document, runnable SQL scripts for the functions and aggregate NULL behavior tasks, MongoDB aggregation pipelines, and embedded evidence images from the submitted assignment.

## Assignment analysis

### Task 1 — Eight SQL business reports
The assignment covers these reports:
1. Top 5 products by revenue
2. Monthly sales report
3. Customer-wise total orders
4. Customers with more than 2 orders
5. Display orders with customer names (JOIN)
6. Orders without payments (LEFT JOIN / missing payment)
7. Total revenue by product category
8. Average order value

The source Word file includes the query screenshots/evidence. The source document's query code for Task 1 is not fully represented in text extraction, so use the document and evidence folder as the reference for those query examples.

### Task 2 — SQL string, date and numeric functions
Demonstrates `UPPER()`, `CONCAT()`, `DATEDIFF()`, `FORMAT()` and `ROUND()` in SQL Server. See `sql/retail_sales_functions_and_nulls.sql`.

### Task 3 — NULL behavior in aggregates
Shows the difference between `COUNT(*)` (all rows), `COUNT(Amount)` (non-NULL values) and `AVG(Amount)` (ignores NULL). The optional NULL insert is commented out because the exact required columns/constraints of the local Payments table may vary.

### Task 4 — MongoDB aggregation
Three pipelines using `$match`, `$group` and `$sort`:
- Count reviews by rating for ratings >= 4
- Average rating per SKU for ratings >= 3
- Count five-star reviews per customer

See `mongodb/review_aggregation_pipelines.js`.

## Repository structure
```text
Day6_Set1_Retail_Sales_Reporting_Ayyappa_GitHub/
├── README.md
├── Day6_Set-1_Ayyappa.docx
├── sql/
│   └── retail_sales_functions_and_nulls.sql
├── mongodb/
│   └── review_aggregation_pipelines.js
└── evidence/
    └── evidence_01 ... evidence_16 (embedded assignment screenshots)
```

## How to run
1. Open the SQL file in SQL Server Management Studio (SSMS).
2. Ensure `RetailSalesDB` exists and has the `Customers`, `Orders`, `Products`, and `Payments` tables referenced by the script.
3. Review/adapt the optional NULL insert to the actual `Payments` table schema before executing it.
4. Open the JavaScript file in MongoDB Compass Aggregations or `mongosh`.
5. Select database `RetailInventoryDB` and confirm the `reviews` collection has fields `Rating`, `SKU`, and `CustomerName`.

## Note
Evidence images are embedded screenshots from the supplied assignment document. They are included as supporting evidence; they do not replace verifying queries against your own local database environment.
