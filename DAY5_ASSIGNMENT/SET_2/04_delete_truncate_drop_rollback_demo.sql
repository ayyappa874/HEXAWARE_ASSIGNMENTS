USE BankBranchDB;
GO
-- Isolated identity demonstration table, separate from banking tables
CREATE TABLE IdentityDemo (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50)
);
INSERT INTO IdentityDemo (Name) VALUES ('Harshith'), ('Rahul'), ('Priya');
SELECT * FROM IdentityDemo;

-- DELETE: rows removed; identity does not reset
DELETE FROM IdentityDemo;
INSERT INTO IdentityDemo (Name) VALUES ('Arun');
SELECT * FROM IdentityDemo; -- expected ID = 4

-- TRUNCATE: removes all rows and resets identity
TRUNCATE TABLE IdentityDemo;
INSERT INTO IdentityDemo (Name) VALUES ('Kiran');
SELECT * FROM IdentityDemo; -- expected ID = 1

-- ROLLBACK: restores deleted row within transaction
BEGIN TRANSACTION;
DELETE FROM IdentityDemo;
SELECT * FROM IdentityDemo; -- empty inside transaction
ROLLBACK TRANSACTION;
SELECT * FROM IdentityDemo; -- Kiran restored

-- DROP: removes table and its data
DROP TABLE IdentityDemo;
GO
