SELECT first_name, YEAR(salaries.from_date), MONTH(salaries.from_date), salary
FROM employees
INNER JOIN salaries 
USING(emp_no)
WHERE employees.emp_no = 11935
AND YEAR(salaries.from_date) >= 1999
ORDER BY first_name
LIMIT 10;