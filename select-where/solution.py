CREATE TABLE athletes (CREATE TABLE athletes (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,    name TEXT,
    sport TEXT    sport TEXT
););

INSERT INTO athletes (name, sport) VALUESINSERT INTO athletes (name, sport) VALUES
  ('LeBron James', 'Basketball'),  ('LeBron James', 'Basketball'),
  ('Serena Williams', 'Tennis'),  ('Serena Williams', 'Tennis'),
  ('Michael Jordan', 'Basketball'),  ('Michael Jordan', 'Basketball'),
  ('Kobe Bryant', 'Basketball'),  ('Kobe Bryant', 'Basketball'),
  ('Cristiano Ronaldo', 'Soccer'),  ('Cristiano Ronaldo', 'Soccer'),
  ('Lionel Messi', 'Soccer'),  ('Lionel Messi', 'Soccer'),
  ('Tom Brady', 'Football'),  ('Tom Brady', 'Football'),
  ('Usain Bolt', 'Track and Field');  ('Usain Bolt', 'Track and Field');
-- Do not modify above this line. ---- Do not modify above this line. --


SELECT name , sport FROM athletes WHERE sport='Basketball';SELECT name , sport FROM athletes WHERE sport='Basketball';


    
