CREATE TABLE coding_problems (CREATE TABLE coding_problems (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,    name TEXT,
    difficulty TEXT,    difficulty TEXT,
    description TEXT    description TEXT
););

INSERT INTO coding_problems (name, difficulty, description) VALUESINSERT INTO coding_problems (name, difficulty, description) VALUES
    ('Dynamic Array', 'Easy', 'Implement a dynamic array in C++'),    ('Dynamic Array', 'Easy', 'Implement a dynamic array in C++'),
    ('Binary Search Tree', 'Medium', 'Implement a binary search tree in C++'),    ('Binary Search Tree', 'Medium', 'Implement a binary search tree in C++'),
    ('Graph Traversal', 'Hard', 'Implement depth-first search and breadth-first search in C++');    ('Graph Traversal', 'Hard', 'Implement depth-first search and breadth-first search in C++');



SELECT * FROM coding_problems;SELECT * FROM coding_problems;

-- Do not modify above this line. ---- Do not modify above this line. --
