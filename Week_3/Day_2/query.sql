-- Week 3 - Day 2 SQL Practice
-- Topics: Filtering, Sorting, Limiting, DISTINCT, LIKE, NULL,
-- Aggregate Functions, GROUP BY, HAVING, CASE, OFFSET

-- Sample table used during practice:
-- employees(id, name, department, salary, email)

-- 1. Employees with salary greater than 60000
SELECT *
FROM employees
WHERE salary > 60000;

-- 2. Name and salary for employees earning more than 50000
SELECT name, salary
FROM employees
WHERE salary > 50000;

-- 3. IT employees earning more than 60000
SELECT *
FROM employees
WHERE department = 'IT'
  AND salary > 60000;

-- 4. Employees in IT or HR
SELECT *
FROM employees
WHERE department IN ('IT', 'HR');

-- 5. Employees with salary between 50000 and 70000
SELECT *
FROM employees
WHERE salary >= 50000
  AND salary <= 70000;

-- Equivalent using BETWEEN
SELECT *
FROM employees
WHERE salary BETWEEN 50000 AND 70000;

-- 6. Employees sorted by salary from highest to lowest
SELECT *
FROM employees
ORDER BY salary DESC;

-- 7. Top 3 highest-paid employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- 8. Unique departments
SELECT DISTINCT department
FROM employees;

-- 9. Names starting with A
SELECT name
FROM employees
WHERE name LIKE 'A%';

-- 10. Names ending with e
SELECT name
FROM employees
WHERE name LIKE '%e';

-- 11. Names containing 'ar'
SELECT name
FROM employees
WHERE name LIKE '%ar%';

-- 12. Employees whose email is missing
SELECT name
FROM employees
WHERE email IS NULL;

-- 13. Employees whose email is available
SELECT name
FROM employees
WHERE email IS NOT NULL;

-- 14. IT employees earning > 60000 with an email
SELECT *
FROM employees
WHERE department = 'IT'
  AND salary > 60000
  AND email IS NOT NULL;

-- =========================
-- Aggregate Functions
-- =========================

-- 15. Total number of employees
SELECT COUNT(id)
FROM employees;

-- 16. Total salary
SELECT SUM(salary)
FROM employees;

-- 17. Average salary
SELECT AVG(salary)
FROM employees;

-- 18. Lowest and highest salary
SELECT MIN(salary), MAX(salary)
FROM employees;

-- 19. Number of employees in each department
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- 20. Total salary for each department
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- 21. Average salary for each department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- 22. Departments whose average salary is greater than 60000
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

-- 23. Departments whose total salary is greater than 100000
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 100000;

-- 24. Filter rows first, then group, then filter groups
SELECT department, AVG(salary) AS avg_sal
FROM employees
WHERE salary >= 50000
GROUP BY department
HAVING AVG(salary) > 50000;

-- 25. Departments with at least 2 employees
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2;

-- 26. Departments with at least 2 employees and total salary > 100000
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2
   AND SUM(salary) > 100000;

-- 27. Highest salary in each department
SELECT department, MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

-- 28. Lowest salary in each department
SELECT department, MIN(salary) AS lowest_salary
FROM employees
GROUP BY department;

-- 29. Average salary and employee count for each department
SELECT department,
       AVG(salary) AS avg_salary,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- 30. Departments with avg salary > 55000 and at least 2 employees
SELECT department,
       AVG(salary) AS avg_salary,
       COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING AVG(salary) > 55000
   AND COUNT(*) >= 2;

-- =========================
-- CASE
-- =========================

-- 31. Categorize employees by salary
SELECT name,
       salary,
       CASE
           WHEN salary >= 70000 THEN 'High'
           WHEN salary >= 50000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM employees;

-- 32. Salary level: Senior / Mid / Junior
SELECT name,
       salary,
       CASE
           WHEN salary >= 70000 THEN 'Senior'
           WHEN salary >= 50000 THEN 'Mid'
           ELSE 'Junior'
       END AS salary_level
FROM employees;

-- 33. Count employees in each salary category
SELECT
    CASE
        WHEN salary >= 70000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category,
    COUNT(*) AS employee_count
FROM employees
GROUP BY
    CASE
        WHEN salary >= 70000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END;

-- 34. Employees per department with salary >= 50000
SELECT department,
       COUNT(*) AS employee_count
FROM employees
WHERE salary >= 50000
GROUP BY department;

-- 35. Departments with >= 2 employees after filtering salary >= 50000
SELECT department,
       COUNT(*) AS employee_count
FROM employees
WHERE salary >= 50000
GROUP BY department
HAVING COUNT(*) >= 2;

-- =========================
-- Top / Bottom / OFFSET
-- =========================

-- 36. Top 2 highest-paid employees in IT
SELECT name, salary
FROM employees
WHERE department = 'IT'
ORDER BY salary DESC
LIMIT 2;

-- 37. Top 2 highest-paid employees company-wide
SELECT name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 2;

-- 38. Second-highest salary (second row after sorting)
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1
OFFSET 1;

-- 39. Third-highest salary (third row after sorting)
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1
OFFSET 2;

-- 40. Second-highest DISTINCT salary
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1
OFFSET 1;

-- 41. Department with highest average salary
SELECT department,
       AVG(salary) AS avg_sal
FROM employees
GROUP BY department
ORDER BY avg_sal DESC
LIMIT 1;

-- 42. Department with highest average salary among departments
-- having at least 2 employees
SELECT department,
       AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY avg_sal DESC
LIMIT 1;

-- 43. Top 2 departments by average salary
SELECT department,
       AVG(salary) AS avg_sal
FROM employees
GROUP BY department
ORDER BY avg_sal DESC
LIMIT 2;

-- 44. Department with lowest total salary
SELECT department,
       SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary ASC
LIMIT 1;
