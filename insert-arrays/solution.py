CREATE TABLE stocks (CREATE TABLE stocks (
  id INTEGER PRIMARY KEY,  id INTEGER PRIMARY KEY,
  name TEXT,  name TEXT,
  transaction_dates DATE[]  transaction_dates DATE[]
););
INSERT INTO stocks (transaction_dates, id, name) VALUESINSERT INTO stocks (transaction_dates, id, name) VALUES
-- Do not modify above this line ---- Do not modify above this line --







-- Do not modify below this line ---- Do not modify below this line --
SELECT * FROM stocks;SELECT * FROM stocks;
(ARRAY['2007-02-09', '2007-02-10', '2007-02-11'], 1, 'AAPL'),(ARRAY['2007-02-09', '2007-02-10', '2007-02-11'], 1, 'AAPL'),
  
(ARRAY['2004-12-15', '2004-12-16'], 2, 'GOOG');(ARRAY['2004-12-15', '2004-12-16'], 2, 'GOOG');
