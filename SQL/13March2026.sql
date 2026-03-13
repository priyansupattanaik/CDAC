CREATE DATABASE IF NOT EXISTS hr;
USE hr;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(20),
    mob_no VARCHAR(10),
    dob DATE,
    sub SET('Math', 'Science', 'Eng'),
    pct FLOAT(5,2)
);

INSERT INTO students VALUES (1, 'Priyansu', 'AB123', '2003-09-15', 'Math', 50.00);
INSERT INTO students VALUES (2, 'A', 'AB123', '2003-10-12', 'Science', 20.00);
INSERT INTO students VALUES (3, 'B', 'AB123', '2003-04-10', 'Eng', 70.00);
INSERT INTO students VALUES (4, 'C', 'AB123', '2003-01-07', 'Math', 90.00);

CREATE TABLE student2(
student_id INT,
student_name VARCHAR(20),
student_address VARCHAR(30));

INSERT INTO student2 VALUES (1, 'D', 'AB123', 'ADD');
INSERT INTO student2 VALUES (1, 'E', 'AB123', 'ADD');
INSERT INTO student2 VALUES (1, 'F', 'AB123', 'ADD');

SHOW TABLES;

SELECT * FROM students;
SELECT * FROM student2;