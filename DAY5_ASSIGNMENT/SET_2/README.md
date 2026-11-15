# Day 5 – Set 2: Bank Branch Accounts and Customer Activity
**Prepared for: Samberapu Ayyappa**

Repository prepared from the supplied `Day5_Set-2.docx` assignment.

## Assignment summary
1. Normalize bank branch/customer/account data to 3NF/BCNF and provide an ER diagram.
2. Create the SQL Server `BankBranchDB` with six normalized tables and constraints.
3. Demonstrate `DELETE`, `TRUNCATE`, `DROP`, and `ROLLBACK` using a separate identity-demo table.
4. Demonstrate customer `INSERT`, `SELECT`, `UPDATE`, `DELETE`, plus AND/OR/IN/BETWEEN and previous-quarter account filters.
5. Create MongoDB capped `LoginEvents` collection, insert 20 events, query Success/Failed events and the latest five events for a user.
6. Discuss why MongoDB suits semi-structured activity logs.

## Repository structure
- `source-files/Day5_Set-2_Assignment.docx` — original assignment file.
- `ANALYSIS.md` — task-by-task source analysis and implementation notes.
- `sql-server/` — SQL Server schema, example seed data, DML/filter queries, transaction behavior demo.
- `mongodb/` — capped collection creation, 20 login events, filters and recent-events query.
- `diagrams/` — ER diagram.
- `screenshots/` — placeholder folder for real screenshots captured from your own tools.

## Run instructions
### SQL Server (SSMS)
Execute in order:
1. `sql-server/01_create_database_schema.sql`
2. `sql-server/02_sample_seed_data.sql`
3. `sql-server/03_customer_dml_and_account_filters.sql`
4. `sql-server/04_delete_truncate_drop_rollback_demo.sql`

The demo script uses a separate `IdentityDemo` table and drops it at the end, as described in the assignment. Read the comments and run scripts in a test database.

### MongoDB (mongosh)
Run:
1. `mongodb/01_capped_login_events.js`
2. `mongodb/02_login_event_queries.js`

The first MongoDB script drops/recreates the `LoginEvents` collection to make its capped configuration reproducible.

## Evidence note
The source assignment contains screenshots evidencing SQL Server table creation, identity behavior, customer DML, and MongoDB capped collection count. This repository does not claim any newly generated screenshots are live evidence. Add your own authentic screenshots in `screenshots/` if your GitHub submission requires them.

## Author
Samberapu Ayyappa
