  name TEXT,  name TEXT,
  transaction_dates DATE[]  transaction_dates DATE[]
););
INSERT INTO stocks (transaction_dates, id, name) VALUESINSERT INTO stocks (transaction_dates, id, name) VALUES
(ARRAY['2007-02-09', '2007-02-10', '2007-02-11']::DATE[], 1, 'AAPL'),(ARRAY['2007-02-09', '2007-02-10', '2007-02-11']::DATE[], 1, 'AAPL'),
(ARRAY['2004-12-15', '2004-12-16']::DATE[], 2, 'GOOG');(ARRAY['2004-12-15', '2004-12-16']::DATE[], 2, 'GOOG');
  
-- Do not modify above this line ---- Do not modify above this line --

