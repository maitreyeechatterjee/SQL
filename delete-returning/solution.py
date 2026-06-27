CREATE TABLE bank_accounts (CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,    name TEXT,
    balance INTEGER,    balance INTEGER,
    last_transaction_date DATE    last_transaction_date DATE
););

INSERT INTO bank_accounts (name, balance, last_transaction_date) VALUESINSERT INTO bank_accounts (name, balance, last_transaction_date) VALUES
    ('Alice', 1000, '2023-11-30'),    ('Alice', 1000, '2023-11-30'),
    ('Bob', -100, '2023-12-31'),    ('Bob', -100, '2023-12-31'),
    ('Charlie', 2000, '2024-01-03'),    ('Charlie', 2000, '2024-01-03'),
    ('David', -500, '2024-01-04'),    ('David', -500, '2024-01-04'),
    ('Eve', 1500, '2024-01-05');    ('Eve', 1500, '2024-01-05');
-- Do not modify above this line. ---- Do not modify above this line. --





