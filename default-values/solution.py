CREATE TABLE videos (CREATE TABLE videos (







-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO videos (id, name, is_published) INSERT INTO videos (id, name, is_published) 
VALUES (1, 'My Video', true),VALUES (1, 'My Video', true),
       (2, 'Another Video', false);       (2, 'Another Video', false);

INSERT INTO videos (id)INSERT INTO videos (id)
VALUES (3),VALUES (3),
       (4);       (4);

INSERT INTO videos (name)INSERT INTO videos (name)
VALUES ('Video with no ID');VALUES ('Video with no ID');

    id INTEGER,    id INTEGER,
););
SELECT * FROM videos;SELECT * FROM videos;
    name TEXT DEFAULT 'untitled',    name TEXT DEFAULT 'untitled',
    is_published BOOLEAN DEFAULT 'false'    is_published BOOLEAN DEFAULT 'false'