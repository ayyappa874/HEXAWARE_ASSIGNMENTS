# Day 6 Assignment Analysis — Ayyappa

**Assignment:** Day 6 – Functions, Aggregation, Grouping and Joins  
**Set:** 1 – Retail Sales Reporting  
**Technology:** SQL Server 2025 and MongoDB 8.0

## Coverage
- Task 1: eight SQL reporting queries — revenue leaders, monthly sales, order count per customer, customers with more than two orders, order/customer JOIN, unpaid orders, category revenue, average order value.
- Task 2: scalar functions `UPPER`, `CONCAT`, `DATEDIFF`, `FORMAT`, `ROUND`.
- Task 3: aggregate NULL behavior with `COUNT(*)`, `COUNT(Amount)`, and `AVG(Amount)`.
- Task 4: three MongoDB aggregation pipelines with `$match`, `$group`, `$sort`.

## Included artifacts
- Original assignment Word document
- SQL script for Task 2 and Task 3 (Task 1 SQL code is supported by embedded screenshots in the source DOCX/evidence)
- MongoDB pipeline script
- 16 embedded evidence images copied from the Word document

## Accuracy / execution caveats
- The Task 1 query code blocks were not completely recovered through document text extraction; original visual evidence is retained for them.
- The NULL insert into `Payments` is intentionally commented until table schema constraints are checked.
- SQL and MongoDB database names are referenced as in the assignment (`RetailSalesDB` and `RetailInventoryDB` respectively); ensure they exist before execution.
