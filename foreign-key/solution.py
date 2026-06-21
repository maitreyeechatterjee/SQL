););

CREATE TABLE employess (CREATE TABLE employess (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
    name TEXT,    name TEXT,
    department_id INTEGER REFERENCE departments(id)    department_id INTEGER REFERENCE departments(id)
    name TEXT    name TEXT
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
CREATE TABLE departments (CREATE TABLE departments (