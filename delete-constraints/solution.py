
DELETE FROM enrollments;DELETE FROM enrollments;

-- Do not modify above this line. ---- Do not modify above this line. --
INSERT INTO enrollments (id, student_id, class_id) VALUES (1, 1, 1);INSERT INTO enrollments (id, student_id, class_id) VALUES (1, 1, 1);
INSERT INTO classes (id, name) VALUES (1, 'Math');INSERT INTO classes (id, name) VALUES (1, 'Math');
INSERT INTO students (id, name) VALUES (1, 'Alice');INSERT INTO students (id, name) VALUES (1, 'Alice');

DELETE FROM students;DELETE FROM students;




-- Do not modify below this line. ---- Do not modify below this line. --
SELECT * FROM enrollments;SELECT * FROM enrollments;
DELETE FROM classes;DELETE FROM classes;