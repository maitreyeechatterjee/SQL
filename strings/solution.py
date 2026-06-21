CREATE TABLE operating_systems (CREATE TABLE operating_systems (







-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO operating_systems (id, name, version, market_share) VALUESINSERT INTO operating_systems (id, name, version, market_share) VALUES
    (1, 'Windows', '10', 75.51),    (1, 'Windows', '10', 75.51),
    (2, 'macOS', '14.5', 20.12),    (2, 'macOS', '14.5', 20.12),
    (3, 'Linux', '5.10', 3.75),    (3, 'Linux', '5.10', 3.75),
    (4, 'Chrome OS', '113', 0.62);    (4, 'Chrome OS', '113', 0.62);

SELECT SELECT 
    os.*,    os.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type || CASE WHEN numeric_precision IS NOT NULL THEN '(' || numeric_precision || ',' || numeric_scale || ')' ELSE '' END, ', ')    (SELECT STRING_AGG(column_name || ' ' || data_type || CASE WHEN numeric_precision IS NOT NULL THEN '(' || numeric_precision || ',' || numeric_scale || ')' ELSE '' END, ', ')
     FROM information_schema.columns      FROM information_schema.columns 
     WHERE table_name = 'operating_systems') AS column_types     WHERE table_name = 'operating_systems') AS column_types
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
    name VARCHAR(225),    name VARCHAR(225),
    version CHAR(10),    version CHAR(10),
    market_share NUMERIC(5,2)    market_share NUMERIC(5,2)