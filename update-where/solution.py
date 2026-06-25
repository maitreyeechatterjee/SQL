CREATE TABLE users (CREATE TABLE users (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username TEXT    username TEXT
););

INSERT INTO users (username) VALUESINSERT INTO users (username) VALUES
  ('Alice'),  ('Alice'),
  ('Bob'),  ('Bob'),
  (NULL),  (NULL),
  ('Charlie'),  ('Charlie'),
  (NULL);  (NULL);

-- Do not modify above this line. ---- Do not modify above this line. --

UPDATE users UPDATE users 
SET username = 'anonymous'SET username = 'anonymous'
WHERE username IS NULL; WHERE username IS NULL; 





-- Do not modify below this line. ---- Do not modify below this line. --
SELECT * FROM users;SELECT * FROM users;
