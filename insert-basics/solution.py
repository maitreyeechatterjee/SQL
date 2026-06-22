CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');

CREATE TABLE bank_accounts (CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
    account_type account_type,    account_type account_type,
    balance INTEGER    balance INTEGER
););
INSERT INTO bank_accounts (id, account_type, balance)INSERT INTO bank_accounts (id, account_type, balance)