-- Do not modify above this line. ---- Do not modify above this line. --

DELETE FROM bank_accountsDELETE FROM bank_accounts
WHERE balance < 0 AND last_transaction_date < '2024-01-01'WHERE balance < 0 AND last_transaction_date < '2024-01-01'
RETURNING id, name;RETURNING id, name;



    ('David', -500, '2024-01-04'),    ('David', -500, '2024-01-04'),
    ('Eve', 1500, '2024-01-05');    ('Eve', 1500, '2024-01-05');