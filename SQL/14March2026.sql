CREATE DATABASE joins_example;
USE joins_example;

CREATE TABLE students (
student_id INT PRIMARY KEY,
student_name VARCHAR(50),
dept_id INT
);

INSERT INTO students VALUES
(1,'Aman',101),
(2,'Riya',102),
(3,'Rahul',103),
(4,'Sneha',101),
(5,'Arjun',104),
(6,'Pooja',102),
(7,'Karan',105),
(8,'Neha',103),
(9,'Vikas',106),
(10,'Anjali',107);

CREATE TABLE departments (
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50)
);

INSERT INTO departments VALUES
(101,'Computer Science'),
(102,'Mechanical'),
(103,'Electrical'),
(104,'Civil'),
(105,'Information Tech'),
(106,'AI'),
(108,'Biotech'),
(109,'Chemical'),
(110,'Aerospace'),
(111,'Automobile');

SELECT * FROM students as s
INNER JOIN department as d
ON s.dept_id = d.dept_id;