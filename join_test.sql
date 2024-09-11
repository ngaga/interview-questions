/* debug this

CoderPad provides a basic SQL sandbox with the following schema.
You can also use commands like '\dt;' and '\d employees;'

employees                             projects
+---------------+---------+           +---------------+---------+
| id            | int     |<----+  +->| id            | int     |
| first_name    | varchar |     |  |  | title         | varchar |
| last_name     | varchar |     |  |  | start_date    | date    |
| salary        | int     |     |  |  | end_date      | date    |
| department_id | int     |--+  |  |  | budget        | int     |
+---------------+---------+  |  |  |  +---------------+---------+
                             |  |  |
departments                  |  |  |  employees_projects
+---------------+---------+  |  |  |  +---------------+---------+
| id            | int     |<-+  |  +--| project_id    | int     |
| name          | varchar |     +-----| employee_id   | int     |
+---------------+---------+           +---------------+---------+


SELECT  projects.title, employees.first_name, EMPLOYEES_PROJECTS.project_id, EMPLOYEES_PROJECTS.employee_id
FROM EMPLOYEES, EMPLOYEES_PROJECTS, PROJECTS
JOIN EMPLOYEES_PROJECTS
ON employees.id = employees_projects.employee_id;
FROM EMPLOYEES_PROJECTS
JOIN PROJECTS
ON EMPLOYEES_PROJECTS.PROJECTS_ID = PROJECTS.ID
*/

SELECT projects.title, employees.first_name
FROM employees
JOIN employees_projects ON employees.id = employees_projects.employee_id
JOIN projects ON employees_projects.project_id = projects.id;
