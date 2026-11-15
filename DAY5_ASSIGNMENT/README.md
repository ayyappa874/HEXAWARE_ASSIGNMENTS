# Day 5 – Set 1: Retail Inventory and Product Reviews
**Prepared for: Ayyappa**

This repository contains the source assignment, raw dataset, original SQL file, and organized SQL Server and MongoDB implementation files.

## Assignment scope
1. Normalize retail inventory data to 3NF; discuss anomalies, entities, and ER relationships.
2. Create SQL Server schema and integrity constraints.
3. Insert seed records and demonstrate deliberate constraint failures.
4. Perform UPDATE and DELETE with SELECT verification.
5. Create MongoDB ProductReviews with JSON Schema validation and CRUD operations.
6. Compare SQL Server and MongoDB and summarize the conclusion.

## Repository structure
- `source-files/` — original assignment PDF, dataset workbook, and original SQL script.
- `sql-server/` — database schema, seed data, constraint tests, and UPDATE/DELETE verification.
- `mongodb/` — collection validator and CRUD operations (mongosh scripts).
- `diagrams/` — ER diagram image.
- `screenshots/` — reserved for genuine evidence screenshots captured from SQL Server Management Studio / MongoDB Compass.

## How to run
### SQL Server
Run scripts in order in SQL Server Management Studio:
1. `sql-server/01_create_database_and_schema.sql`
2. `sql-server/02_seed_data.sql`
3. `sql-server/03_constraint_failure_tests.sql` — run each marked failure individually; expected to error by design.
4. `sql-server/04_update_delete_verification.sql`

### MongoDB
Open `mongosh` connected to your MongoDB instance and run:
1. `mongodb/01_create_validator.js`
2. `mongodb/02_crud_operations.js`

## Data and evidence note
The supplied assignment PDF states that the Supplier table result has 11 records (S01–S11). The uploaded `query.sql` seed section initially contains S01–S10; this package's seed script adds the PDF's representative S11 row (`New Supplier`) to align with the assignment narrative. The package does not claim screenshots are real; capture your own application screenshots and place them in `screenshots/`.

## Author
Ayyappa
