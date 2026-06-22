CREATE TABLE users (CREATE TABLE users (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 18),    age INTEGER CHECK (age >= 18),
    status status    status status
););
-- Do not modify above this line ---- Do not modify above this line --

INSERT INTO users (id, name, age, status) VALUESINSERT INTO users (id, name, age, status) VALUES

-- Do not modify below this line ---- Do not modify below this line --
SELECT * FROM users;SELECT * FROM users;
CREATE TYPE status AS ENUM ('active', 'inactive', 'pending');CREATE TYPE status AS ENUM ('active', 'inactive', 'pending');


(1, 'John Doe', 20, 'active'),(1, 'John Doe', 20, 'active'),
(2, 'Jane Doe', 27, 'pending'),(2, 'Jane Doe', 27, 'pending'),
(3, 'John Smith', 28, 'active'),(3, 'John Smith', 28, 'active'),
(4, 'Jane Smith', 30, 'inactive');(4, 'Jane Smith', 30, 'inactive');
