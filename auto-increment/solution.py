CREATE SEQUENCE gov_id START WITH 1000 INCREMENT BY 3;CREATE SEQUENCE gov_id START WITH 1000 INCREMENT BY 3;









-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO gov_employee (name) INSERT INTO gov_employee (name) 
  VALUES  VALUES
      ('John Doe'),      ('John Doe'),
      ('Jane Doe'),      ('Jane Doe'),
      ('Jim Beam');      ('Jim Beam');


CREATE TABLE gov_employees (CREATE TABLE gov_employees (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
););
SELECT * FROM gov_employee;SELECT * FROM gov_employee;
    gov_id INTEGER DEFAULT nextval('gov_id'),    gov_id INTEGER DEFAULT nextval('gov_id'),
    name TEXT    name TEXT
