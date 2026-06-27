CREATE TABLE students (CREATE TABLE students (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,    name TEXT,
    age INTEGER    age INTEGER
););

INSERT INTO students (name, age)INSERT INTO students (name, age)
  VALUES ('John Doe', 20),  VALUES ('John Doe', 20),
         ('Jane Doe', 21),         ('Jane Doe', 21),