-- Do not modify above this line. ---- Do not modify above this line. --

UPDATE bank_accountsUPDATE bank_accounts
SET status = 'VIP'SET status = 'VIP'
WHERE balance > 10000 AND balance < 100000WHERE balance > 10000 AND balance < 100000
RETURNING id, balance, status;RETURNING id, balance, status;



(60000, 'Frank');(60000, 'Frank');