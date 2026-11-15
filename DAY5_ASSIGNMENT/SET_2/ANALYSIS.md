# Day 5 – Set 2 Analysis
## Bank Branch Accounts and Customer Activity

### Source
Analysis is based on the supplied `Day5_Set-2.docx` (11 pages).

### Task 1 — Normalization to 3NF / BCNF and ER diagram
The denormalized scenario has customer identity/name/address, account number/type, branch, relationship manager, balance and last-transaction text. The assignment identifies the normalized relations:
- Customer(Customer_ID PK, Customer_Name, Address)
- Branch(Branch_ID PK, Branch_Name unique)
- Manager(Manager_ID PK, Manager_Name, Branch_ID FK)
- Account(Account_No PK, Account_Type, Branch_ID FK, Manager_ID FK, Balance)
- AccountHolder(Customer_ID + Account_No composite PK; both FKs)
- Transactions(Transaction_ID PK, Account_No FK, Transaction_Type, Transaction_Date, Amount)

The AccountHolder bridge resolves the many-to-many customer/account relationship. Branch and Manager descriptions are stored in their own relations. Transaction data is separated by Transaction_ID. The assignment says each account is assigned to one branch and one relationship manager; a customer may hold multiple accounts and accounts may be jointly held.

### Task 2 — SQL Server DDL
The assignment requests database `BankBranchDB` and six normalized tables. IDs use IDENTITY where applicable. Account_No is the account primary key. CHECK constraints protect Balance >= 0 and Amount > 0. Branch/Manager references on Account are restrictive; dependent association and transaction rows cascade as specified.

### Task 3 — DELETE / TRUNCATE / DROP / ROLLBACK
A separate IdentityDemo table is used:
- DELETE removes rows but identity sequence continues (the example next ID is 4).
- TRUNCATE removes all rows and resets identity (the example next ID is 1).
- ROLLBACK restores the row deleted inside the transaction.
- DROP removes table definition and data.

### Task 4 — Customer DML and account filters
The assignment executes customer inserts for Harshith (Chennai), Rahul (Bangalore), and Priya (Hyderabad), selects a customer, updates Rahul's address to Coimbatore, and deletes Priya. It also asks for AND, OR, IN, BETWEEN filters and accounts opened in the previous calendar quarter with Balance > 50,000. `Opened_Date` is added as a query extension in the source.

### Task 5 — MongoDB capped collection and login activity
Create capped `LoginEvents` with size 100,000 bytes and max 20 documents. Generate 20 events with user_id, username, login_time, status alternating Success/Failed, and IP address. Query all events, successful/failed events, countDocuments(), and latest five events for user_id 1 sorted newest first.

### Notes on package contents
The SQL sample seed file supplies plausible example branch/manager/account rows to let the queries be demonstrated. These are sample implementation data and are not claimed to be source-provided records. The assignment's actual evidence screenshots are embedded in the supplied DOCX; the `screenshots/` folder is reserved for user-captured standalone evidence.
