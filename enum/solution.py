








-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO bank_accounts (id, account_type, balance) VALUES INSERT INTO bank_accounts (id, account_type, balance) VALUES 
  (1, 'checking', 1000),  (1, 'checking', 1000),
  (2, 'savings', 2000),  (2, 'savings', 2000),
  (3, 'cd', 3000),  (3, 'cd', 3000),
  (4, 'money_market', 4000);  (4, 'money_market', 4000);

SELECT SELECT 
    ba.*,    ba.*,
CREATE TABLE bank_accounts (CREATE TABLE bank_accounts (

CREATE TYPE account_type AS ENUM ('checking','savings','cd','money_market');CREATE TYPE account_type AS ENUM ('checking','savings','cd','money_market');
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
    account_type ACCOUNT_TYPE,    account_type ACCOUNT_TYPE,
    balance INTEGER    balance INTEGER