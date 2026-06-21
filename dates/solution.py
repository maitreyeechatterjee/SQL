CREATE TABLE events (CREATE TABLE events (







-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO events (id, event_date, event_time, event_timestamp) INSERT INTO events (id, event_date, event_time, event_timestamp) 
  VALUES (1, '2000-01-01', '12:30:10', '2000-01-01 12:30:10');  VALUES (1, '2000-01-01', '12:30:10', '2000-01-01 12:30:10');

SELECT SELECT 
    e.*,    e.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type, ', ')    (SELECT STRING_AGG(column_name || ' ' || data_type, ', ')
     FROM information_schema.columns      FROM information_schema.columns 
     WHERE table_name = 'events') AS column_types     WHERE table_name = 'events') AS column_types
FROM FROM 
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
    events e;    events e;
    event_date DATE,    event_date DATE,
    event_time TIME,    event_time TIME,
    event_timestamp TIMESTAMP    event_timestamp TIMESTAMP
