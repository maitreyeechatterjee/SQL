CREATE TABLE three_column_table (CREATE TABLE three_column_table (






-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO three_column_table (id, is_active, is_admin) INSERT INTO three_column_table (id, is_active, is_admin) 
  VALUES (1, TRUE, FALSE),  VALUES (1, TRUE, FALSE),
         (2, true, false),         (2, true, false),
         (3, 't', 'f'),         (3, 't', 'f'),
         (4, 'y', 'n'),         (4, 'y', 'n'),
         (5, 'yes', 'no'),         (5, 'yes', 'no'),
         (6, 'on', 'off'),         (6, 'on', 'off'),
         (7, '1', '0');         (7, '1', '0');

    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
SELECT * FROM three_column_table;SELECT * FROM three_column_table;
    is_active BOOLEAN,    is_active BOOLEAN,
    is_admin BOOLEAN    is_admin BOOLEAN
