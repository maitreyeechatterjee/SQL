-- Do not modify above this line. ---- Do not modify above this line. --

UPDATE bank_accountsUPDATE bank_accounts
SET status = 'VIP'SET status = 'VIP'
WHERE balance > 10000 AND < 100000WHERE balance > 10000 AND < 100000
RETURNING id, balance, status;RETURNING id, balance, status;



