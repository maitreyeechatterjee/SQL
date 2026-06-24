CREATE TABLE comments (CREATE TABLE comments (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    author TEXT,    author TEXT,
    body TEXT,    body TEXT,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
););

INSERT INTO comments (author, body) VALUESINSERT INTO comments (author, body) VALUES
    ('NeetCode', 'This problem should be marked as easy.. haha'),    ('NeetCode', 'This problem should be marked as easy.. haha'),
    ('Lee', 'This problem is too hard for an easy tag');    ('Lee', 'This problem is too hard for an easy tag');

  
SELECT author AS comment_author, body AS comment_bodySELECT author AS comment_author, body AS comment_body
FROM comments;FROM comments;



-- Do not modify above this line. ---- Do not modify above this line. --

SELECT author AS comment_author, body AS comment_body;SELECT author AS comment_author, body AS comment_body;


