# Assignment Analysis – Day 5 Set 1
## Retail Inventory and Product Reviews

### Source materials inspected
- `Day5_Set-1_Assignment.pdf` (10 pages)
- `retail_inventory_raw_data.xlsx`
- `original_query.sql`

### Requirements
- Task 1: 3NF normalization, functional dependencies, anomalies, normalized tables, ER diagram.
- Task 2: SQL Server database and PK/FK/UNIQUE/NOT NULL/CHECK/DEFAULT constraints.
- Task 3: Seed records and demonstrate duplicate key/unique, missing mandatory value, negative quantity, and invalid parent reference.
- Task 4: UPDATE supplier phone using WHERE and verify; DELETE discontinued SKU inventory rows using WHERE and verify.
- Task 5: MongoDB ProductReviews collection, JSON Schema validator, insertMany/find/updateOne/deleteOne.
- Task 6: SQL Server vs MongoDB comparison and conclusion.

### Relational design from assignment
- Supplier(Supplier_ID PK, Supplier_Name, Supplier_Phone UNIQUE)
- Product(SKU PK, Product_Name, Category, Supplier_ID FK)
- Inventory((SKU, Warehouse) composite PK, SKU FK, Quantity CHECK >= 0, Reorder_Level DEFAULT 0 and CHECK >= 0)
- ProductReview(Review_ID PK, SKU FK, Customer_Name, Rating CHECK 1–5, Review_Text)

### Raw spreadsheet summary
The workbook has 20 records and columns for SKU, product name, category, supplier name, supplier phone, warehouse, quantity, reorder level, and customer review. The assignment frames the normalized design and its constraints.

### SQL source review
The uploaded query.sql creates Supplier, Product, and Inventory, inserts supplier/product/inventory data, includes a joined SELECT, deliberate constraint failures, an UPDATE, and a DELETE with verification. The assignment PDF additionally defines ProductReview and MongoDB implementation requirements. Organized scripts in this repository include those elements.

### MongoDB role
ProductReviews is suited to flexible document storage for product review text and rating data. SearchActivity is described in the assignment as an event-like collection with optional changing metadata.

### Evidence
The screenshots folder is intentionally empty as a staging area. Insert authentic screenshots from your own SQL Server / MongoDB environment; do not represent illustrative images as live evidence.
