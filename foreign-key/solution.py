););
    department_id INTEGER REFERENCES departments(id)    department_id INTEGER REFERENCES departments(id)
    name TEXT,    name TEXT,
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
CREATE TABLE employess (CREATE TABLE employess (

););
    name TEXT    name TEXT
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
CREATE TABLE departments (CREATE TABLE departments (









-- Do not modify below this line ---- Do not modify below this line --
SELECT SELECT 
    c.table_name,    c.table_name,
    c.column_name,     c.column_name, 
    c.data_type,    c.data_type,
    CASE     CASE 