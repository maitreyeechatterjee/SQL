    name TEXT    name TEXT
););

CREATE TABLE employees (CREATE TABLE employees (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
    name TEXT,    name TEXT,
    department_id INTEGER REFERENCES departments(id)    department_id INTEGER REFERENCES departments(id)
););

