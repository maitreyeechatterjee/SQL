







-- Do not modify below this line ---- Do not modify below this line --
SELECT SELECT 
    c.table_name,    c.table_name,
    c.column_name,     c.column_name, 
    c.data_type,    c.data_type,
    CASE     CASE 

CREATE TABLE departments (CREATE TABLE departments (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
    name TEXT,    name TEXT,

CREATE TABLE employess (CREATE TABLE employess (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
    name TEXT,    name TEXT,
    department_id INTEGER REFERENCE departments(id)    department_id INTEGER REFERENCE departments(id)