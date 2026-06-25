(5000, 'Eve', 'Normal'),(5000, 'Eve', 'Normal'),
(60000, 'Frank', 'VIP');(60000, 'Frank', 'VIP');
-- Do not modify above this line. ---- Do not modify above this line. --


UPDATE bank_accountsUPDATE bank_accounts
SET balance = 0, name = 'Anonymous', account_status = 'VIP'SET balance = 0, name = 'Anonymous', account_status = 'VIP'
RETURNING *;RETURNING *;
