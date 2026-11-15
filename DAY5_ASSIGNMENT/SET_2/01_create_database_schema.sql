IF DB_ID('BankBranchDB') IS NULL
    CREATE DATABASE BankBranchDB;
GO
USE BankBranchDB;
GO

CREATE TABLE Customer (
    Customer_ID INT IDENTITY(1,1) PRIMARY KEY,
    Customer_Name VARCHAR(100) NOT NULL,
    Address VARCHAR(200) NOT NULL
);

CREATE TABLE Branch (
    Branch_ID INT IDENTITY(1,1) PRIMARY KEY,
    Branch_Name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Manager (
    Manager_ID INT IDENTITY(1,1) PRIMARY KEY,
    Manager_Name VARCHAR(100) NOT NULL,
    Branch_ID INT NOT NULL,
    CONSTRAINT FK_Manager_Branch FOREIGN KEY (Branch_ID)
        REFERENCES Branch(Branch_ID) ON DELETE CASCADE
);

CREATE TABLE Account (
    Account_No VARCHAR(20) PRIMARY KEY,
    Account_Type VARCHAR(20) NOT NULL,
    Branch_ID INT NOT NULL,
    Manager_ID INT NOT NULL,
    Balance DECIMAL(12,2) NOT NULL CHECK (Balance >= 0),
    CONSTRAINT FK_Account_Branch FOREIGN KEY (Branch_ID)
        REFERENCES Branch(Branch_ID),
    CONSTRAINT FK_Account_Manager FOREIGN KEY (Manager_ID)
        REFERENCES Manager(Manager_ID)
);

CREATE TABLE AccountHolder (
    Customer_ID INT NOT NULL,
    Account_No VARCHAR(20) NOT NULL,
    CONSTRAINT PK_AccountHolder PRIMARY KEY (Customer_ID, Account_No),
    CONSTRAINT FK_AccountHolder_Customer FOREIGN KEY (Customer_ID)
        REFERENCES Customer(Customer_ID) ON DELETE CASCADE,
    CONSTRAINT FK_AccountHolder_Account FOREIGN KEY (Account_No)
        REFERENCES Account(Account_No) ON DELETE CASCADE
);

CREATE TABLE Transactions (
    Transaction_ID INT IDENTITY(1,1) PRIMARY KEY,
    Account_No VARCHAR(20) NOT NULL,
    Transaction_Type VARCHAR(30) NOT NULL,
    Transaction_Date DATE NOT NULL,
    Amount DECIMAL(12,2) NOT NULL CHECK (Amount > 0),
    CONSTRAINT FK_Transactions_Account FOREIGN KEY (Account_No)
        REFERENCES Account(Account_No) ON DELETE CASCADE
);

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
GO
