CREATE TABLE bank_accounts (CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    balance INTEGER,    balance INTEGER,
    name TEXT,    name TEXT,
    status TEXT    status TEXT
););

INSERT INTO bank_accounts (balance, name) VALUESINSERT INTO bank_accounts (balance, name) VALUES
(8000, 'Alice'),(8000, 'Alice'),
(9000, 'Bob'),(9000, 'Bob'),
(12000, 'Charlie'),(12000, 'Charlie'),
(40000, 'David'),(40000, 'David'),
(5000, 'Eve'),(5000, 'Eve'),
(60000, 'Frank');(60000, 'Frank');
-- Do not modify above this line. ---- Do not modify above this line. --

UPDATE bank_accountsUPDATE bank_accounts




SET status = VIPSET status = VIP
WHERE balance >10000 AND <100000WHERE balance >10000 AND <100000
RETURN id, balance, status;RETURN id, balance, status;
