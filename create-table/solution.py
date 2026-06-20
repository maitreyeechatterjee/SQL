 CREATE TABLE videos ( CREATE TABLE videos (
  id INTEGER,  id INTEGER,
  name TEXT,  name TEXT,
  created_at DATE,  created_at DATE,
  published BOOLEAN  published BOOLEAN
););

-- Do not modify below this line ---- Do not modify below this line --
SELECT table_name, column_name, data_typeSELECT table_name, column_name, data_type
FROM information_schema.columnsFROM information_schema.columns
WHERE table_name = 'videos';WHERE table_name = 'videos';