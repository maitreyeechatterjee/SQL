CREATE TABLE students (CREATE TABLE students (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
    name TEXT,    name TEXT,
    age INTEGER    age INTEGER
););

INSERT INTO students (id, name, age) VALUESINSERT INTO students (id, name, age) VALUES
(1, 'Alice', 20),(1, 'Alice', 20),
(2, 'Bob', NULL),(2, 'Bob', NULL),
(3, 'Charlie', 30);(3, 'Charlie', 30);
-- Do not modify above this line. ---- Do not modify above this line. --

UPDATE students UPDATE students 
SET age = 'NULL';SET age = 'NULL';



-- Do not modify below this line. ---- Do not modify below this line. --
SELECT * FROM students;SELECT * FROM students;
