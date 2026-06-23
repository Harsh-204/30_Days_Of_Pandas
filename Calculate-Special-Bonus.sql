1# Write your MySQL query statement below
2SELECT
3    employee_id,
4    CASE
5        WHEN employee_id % 2 != 0
6             AND name NOT LIKE 'M%'
7        THEN salary
8        ELSE 0
9    END AS bonus
10FROM Employees
11ORDER BY employee_id;
12