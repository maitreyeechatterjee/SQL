CREATE TYPE status AS ENUM ('Normal', 'VIP');CREATE TYPE status AS ENUM ('Normal', 'VIP');

CREATE TABLE bank_accounts (CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    balance INTEGER,    balance INTEGER,
    name TEXT,    name TEXT,
    account_status status    account_status status
););

INSERT INTO bank_accounts (balance, name, account_status) VALUESINSERT INTO bank_accounts (balance, name, account_status) VALUES
(8000, 'Alice', 'Normal'),(8000, 'Alice', 'Normal'),
(9000, 'Bob', 'Normal'),(9000, 'Bob', 'Normal'),
(12000, 'Charlie', 'Normal'),(12000, 'Charlie', 'Normal'),
(40000, 'David', 'VIP'),(40000, 'David', 'VIP'),
(5000, 'Eve', 'Normal'),(5000, 'Eve', 'Normal'),
(60000, 'Frank', 'VIP');(60000, 'Frank', 'VIP');
-- Do not modify above this line. ---- Do not modify above this line. --


UPDATE bank_accountsUPDATE bank_accounts
SET balance = 0, name = 'Anonymous', account_status = 'Special'SET balance = 0, name = 'Anonymous', account_status = 'Special'
RETURNING *;RETURNING *;
