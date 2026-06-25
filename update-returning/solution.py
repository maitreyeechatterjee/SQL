-- Do not modify above this line. ---- Do not modify above this line. --

UPDATE bank_accountsUPDATE bank_accounts
SET status = 'VIP'SET status = 'VIP'
WHERE balance > 10000 AND < 100000WHERE balance > 10000 AND < 100000
RETURN id, balance, status;RETURN id, balance, status;


(60000, 'Frank');(60000, 'Frank');
(5000, 'Eve'),(5000, 'Eve'),