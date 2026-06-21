CREATE TABLE orders (CREATE TABLE orders (






-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO orders (id, items, total_price) INSERT INTO orders (id, items, total_price) 
    VALUES (1, ARRAY['apple', 'banana'], 100),    VALUES (1, ARRAY['apple', 'banana'], 100),
          (2, ARRAY['orange', 'grape'], 200),          (2, ARRAY['orange', 'grape'], 200),
          (3, ARRAY['watermelon', 'pineapple'], 300);          (3, ARRAY['watermelon', 'pineapple'], 300);

    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
SELECT * FROM orders;SELECT * FROM orders;
    items TEXT,    items TEXT,
    total_price INTEGER    total_price INTEGER
