-- Week 3 - Day 1
-- SQL: Table Creation, Constraints and CRUD Operations


-- Create Table

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    salary INT CHECK (salary > 0),
    department VARCHAR(50) DEFAULT 'General'
);


-- Insert a Single Row

INSERT INTO employees (
    id,
    name,
    email,
    age,
    salary,
    department
)
VALUES (
    1,
    'Kiran',
    'kiran@email.com',
    22,
    50000,
    'IT'
);


-- Insert Using Default Value

INSERT INTO employees (
    id,
    name,
    email,
    age,
    salary
)
VALUES (
    2,
    'Ravi',
    'ravi@email.com',
    23,
    60000
);


-- Insert Multiple Rows

INSERT INTO employees (
    id,
    name,
    email,
    age,
    salary,
    department
)
VALUES
    (3, 'Sai', 'sai@email.com', 25, 55000, 'HR'),
    (4, 'Anil', 'anil@email.com', 28, 70000, 'Finance'),
    (5, 'Rahul', 'rahul@email.com', 24, 45000, 'IT');


-- View Data

SELECT * FROM employees;


-- Update One Employee

UPDATE employees
SET department = 'HR'
WHERE name = 'Kiran';


-- Update Multiple Employees

UPDATE employees
SET salary = 60000
WHERE department = 'IT';


-- Update Using Existing Value

UPDATE employees
SET salary = salary + 5000
WHERE department = 'HR';


-- Update Multiple Columns

UPDATE employees
SET salary = 70000,
    department = 'Management'
WHERE id = 1;


-- Delete One Row

DELETE FROM employees
WHERE id = 5;


-- Delete Employees Using a Condition

-- DELETE FROM employees
-- WHERE department = 'HR';


-- Delete All Rows

-- DELETE FROM employees;


-- Final View

SELECT * FROM employees;