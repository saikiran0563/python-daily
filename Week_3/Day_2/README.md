Week 3 - Day 2 SQL

Topics Covered

SELECT and FROM

WHERE

AND / OR

IN

BETWEEN

ORDER BY

LIMIT

DISTINCT

LIKE

NULL / IS NULL / IS NOT NULL

Aggregate functions: COUNT, SUM, AVG, MIN, MAX

GROUP BY

HAVING

CASE expressions

OFFSET

Combined filtering and aggregation patterns

Practice File

day2_queries.sql contains the SQL queries practiced during Week 3 Day 2.

Important Patterns

WHERE vs HAVING

WHERE filters individual rows before grouping.

HAVING filters groups after GROUP BY.

Aggregate Functions

COUNT(*) - counts rows

SUM() - total

AVG() - average

MIN() - minimum

MAX() - maximum

Top-N Pattern

SELECT ...
FROM employees
ORDER BY salary DESC
LIMIT 2;

Second-Highest Distinct Value

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

CASE

CASE
    WHEN condition THEN result
    ELSE result
END
