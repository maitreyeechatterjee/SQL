););

CREATE TABLE enrollments (CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),    student_id INTEGER REFERENCES students(id),
    class_id INTEGER REFERENCES classes(id)    class_id INTEGER REFERENCES classes(id)
););

INSERT INTO classes (id, name) VALUES (1, 'Math');INSERT INTO classes (id, name) VALUES (1, 'Math');
INSERT INTO students (id, name) VALUES (1, 'Alice');INSERT INTO students (id, name) VALUES (1, 'Alice');
INSERT INTO enrollments (id, student_id, class_id) VALUES (1, 1, 1);INSERT INTO enrollments (id, student_id, class_id) VALUES (1, 1, 1);
-- Do not modify above this line. ---- Do not modify above this line. --


DELETE FROM classes;DELETE FROM classes;

DELETE FROM enrollments;DELETE FROM enrollments;

DELETE FROM students;DELETE FROM students;


-- Do not modify below this line. ---- Do not modify below this line. --
SELECT * FROM enrollments;SELECT * FROM enrollments;

    name TEXT    name TEXT