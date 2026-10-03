-- Week 3 - Day 3
-- SQL JOINs and Subqueries
-- Practice tables used during learning:
-- employees(employee_id, name, department_id, salary)
-- departments(department_id, department_name)

-- 1. INNER JOIN: employee name + department name

SELECT
    e.name,
    d.department_name
FROM employees AS e
INNER JOIN departments AS d
    ON e.department_id = d.department_id;


-- 2. LEFT JOIN: keep all employees, including unmatched ones

SELECT
    e.name,
    d.department_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.department_id = d.department_id;


-- 3. RIGHT JOIN: keep all departments

SELECT
    e.name,
    d.department_name
FROM employees AS e
RIGHT JOIN departments AS d
    ON e.department_id = d.department_id;


-- 4. FULL OUTER JOIN equivalent in MySQL:
-- MySQL does not support FULL OUTER JOIN directly.
-- Combine LEFT JOIN and RIGHT JOIN with UNION.

SELECT
    e.name,
    d.department_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.department_id = d.department_id

UNION

SELECT
    e.name,
    d.department_name
FROM employees AS e
RIGHT JOIN departments AS d
    ON e.department_id = d.department_id;


-- 5. SELF JOIN: employee + manager
-- Assumes employees also has manager_id

SELECT
    e.name AS employee,
    m.name AS manager
FROM employees AS e
LEFT JOIN employees AS m
    ON e.manager_id = m.employee_id;


-- 6. Anti-join pattern: employees without a matching department

SELECT
    e.name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.department_id = d.department_id
WHERE d.department_id IS NULL;


-- 7. Departments with no employees

SELECT
    d.department_name
FROM departments AS d
LEFT JOIN employees AS e
    ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;


-- 8. Employees earning > 50000 with department name

SELECT
    e.name,
    d.department_name,
    e.salary
FROM employees AS e
INNER JOIN departments AS d
    ON e.department_id = d.department_id
WHERE e.salary > 50000;

-- 9. Number of employees in each department

SELECT
    d.department_name,
    COUNT(*) AS employee_count
FROM employees AS e
INNER JOIN departments AS d
    ON e.department_id = d.department_id
GROUP BY d.department_name;


-- 10. Average salary for each department

SELECT
    d.department_name,
    AVG(e.salary) AS avg_salary
FROM employees AS e
INNER JOIN departments AS d
    ON e.department_id = d.department_id
GROUP BY d.department_name;


-- 11. Departments with average salary > 50000

SELECT
    d.department_name,
    AVG(e.salary) AS avg_salary
FROM employees AS e
INNER JOIN departments AS d
    ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 50000;


-- 12. Department with highest total salary

SELECT
    d.department_name,
    SUM(e.salary) AS total_salary
FROM departments AS d
INNER JOIN employees AS e
    ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC
LIMIT 1;


-- 13. Employees above their own department average

SELECT
    e.name,
    e.salary,
    a.avg_salary
FROM employees AS e
INNER JOIN (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) AS a
    ON e.department_id = a.department_id
WHERE e.salary > a.avg_salary;


-- 14. Employees above the overall company average

SELECT
    name,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- 15. Employees below the overall company average

SELECT
    name,
    salary
FROM employees
WHERE salary < (
    SELECT AVG(salary)
    FROM employees
);


-- 16. Employees in the same department as Charlie

SELECT
    name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM employees
    WHERE name = 'Charlie'
);


-- 17. Departments that have at least one employee

SELECT
    d.department_name
FROM departments AS d
WHERE EXISTS (
    SELECT 1
    FROM employees AS e
    WHERE e.department_id = d.department_id
);


-- 18. Departments that have no employees
SELECT
    d.department_name
FROM departments AS d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees AS e
    WHERE e.department_id = d.department_id
);
