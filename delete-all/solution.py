CREATE TABLE students (CREATE TABLE students (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,    name TEXT,
    age INTEGER    age INTEGER
););

INSERT INTO students (name, age)INSERT INTO students (name, age)
  VALUES ('John Doe', 20),  VALUES ('John Doe', 20),
         ('Jane Doe', 21),         ('Jane Doe', 21),
         ('John Smith', 22),         ('John Smith', 22),
         ('Jane Smith', 23);         ('Jane Smith', 23);
-- Do not modify above this line. ---- Do not modify above this line. --

DELETE FROM students;DELETE FROM students;



-- Do not modify below this line. ---- Do not modify below this line. --
SELECT * FROM students;SELECT * FROM students;
