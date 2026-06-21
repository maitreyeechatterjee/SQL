




-- Do not modify below this line ---- Do not modify below this line --
SELECT SELECT 
    c.table_name,    c.table_name,
    c.column_name,     c.column_name, 
    c.data_type,     c.data_type, 
    CASE     CASE 
        WHEN kcu.column_name IS NOT NULL THEN         WHEN kcu.column_name IS NOT NULL THEN 
            CASE             CASE 
                WHEN COUNT(*) OVER (PARTITION BY kcu.constraint_name) > 1 THEN 'YES (Composite)'                WHEN COUNT(*) OVER (PARTITION BY kcu.constraint_name) > 1 THEN 'YES (Composite)'
                ELSE 'YES'                ELSE 'YES'
            END            END

CREATE TABLE orders(CREATE TABLE orders(
        

    product_id INTEGER,    product_id INTEGER,
    quantity INTEGER,    quantity INTEGER,
    order_id INTEGER,    order_id INTEGER,
););
    PRIMARY KEY (order_id, product_id)    PRIMARY KEY (order_id, product_id)