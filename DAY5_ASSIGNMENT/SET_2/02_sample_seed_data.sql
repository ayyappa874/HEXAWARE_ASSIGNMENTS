USE BankBranchDB;
GO
-- Sample implementation data (example values, not records specified in the assignment)
INSERT INTO Branch (Branch_Name) VALUES
('Chennai Main'), ('Bengaluru Central'), ('Hyderabad City');

INSERT INTO Manager (Manager_Name, Branch_ID) VALUES
('Manager One', 1), ('Manager Two', 2), ('Manager Three', 3);

INSERT INTO Customer (Customer_Name, Address) VALUES
('Harshith', 'Chennai'),
('Rahul', 'Bangalore'),
('Priya', 'Hyderabad'),
('Ayyappa', 'Kakinada');

INSERT INTO Account (Account_No, Account_Type, Branch_ID, Manager_ID, Balance) VALUES
('ACC1001', 'Savings', 1, 1, 75000.00),
('ACC1002', 'Current', 2, 2, 45000.00),
('ACC1003', 'Savings', 3, 3, 120000.00),
('ACC1004', 'Current', 1, 1, 15000.00);

INSERT INTO AccountHolder (Customer_ID, Account_No) VALUES
(1, 'ACC1001'),
(2, 'ACC1002'),
(3, 'ACC1003'),
(1, 'ACC1004'),
(4, 'ACC1001'); -- joint account example

INSERT INTO Transactions (Account_No, Transaction_Type, Transaction_Date, Amount) VALUES
('ACC1001', 'Deposit', '2026-10-02', 5000.00),
('ACC1001', 'Withdrawal', '2026-10-07', 1000.00),
('ACC1002', 'Deposit', '2026-09-19', 8000.00),
('ACC1003', 'Transfer', '2026-11-01', 15000.00);

-- Join example
SELECT C.Customer_Name, A.Account_No, A.Account_Type, B.Branch_Name, M.Manager_Name, A.Balance
FROM Customer C
JOIN AccountHolder AH ON C.Customer_ID = AH.Customer_ID
JOIN Account A ON AH.Account_No = A.Account_No
JOIN Branch B ON A.Branch_ID = B.Branch_ID
JOIN Manager M ON A.Manager_ID = M.Manager_ID;
