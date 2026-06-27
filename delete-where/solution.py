CREATE TABLE students (CREATE TABLE students (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,    name TEXT,
    age INTEGER    age INTEGER
););

INSERT INTO students (name, age)INSERT INTO students (name, age)
  VALUES ('John Doe', 16),  VALUES ('John Doe', 16),
         ('Jane Doe', 19),         ('Jane Doe', 19),
         ('Alice Smith', 22),         ('Alice Smith', 22),
         ('Bob Smith', 23),         ('Bob Smith', 23),
         ('Alice Johnson', 26);         ('Alice Johnson', 26);
-- Do not modify above this line. ---- Do not modify above this line. --





-- Do not modify below this line. ---- Do not modify below this line. --
SELECT * FROM students;SELECT * FROM students;
