););

INSERT INTO comments (author, body) VALUESINSERT INTO comments (author, body) VALUES
    ('NeetCode', 'This problem should be marked as easy.. haha'),    ('NeetCode', 'This problem should be marked as easy.. haha'),
    ('Lee', 'This problem is too hard for an easy tag');    ('Lee', 'This problem is too hard for an easy tag');

SELECT author, bodySELECT author, body



FROM comments;FROM comments;
-- Do not modify above this line. ---- Do not modify above this line. --

SELECT author AS comment_author, body AS comment_bodySELECT author AS comment_author, body AS comment_body
FROM comments;FROM comments;
