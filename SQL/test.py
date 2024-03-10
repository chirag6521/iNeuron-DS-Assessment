# Answer 1

'''
The subquery (SELECT winner_id FROM race) retrieves all winner_id values from the race table since both rows in the race_win table have NULL as the winner_id, the subquery effectively returns an empty result set
The main query selects all rows from the runner table where the id is not in the result set obtained from the subquery in other words  it fetches all runners who did not win any race.
Since there are no matching winner_id values in the subquery, the result of the entire query will be the same as selecting all rows from the runner table 
Alternative vversion of the query: To avoid the issue of an empty subquery, we can use a LEFT JOIN to achieve the same result without relying on the subquery:
'''


SELECT r.*
FROM runners r
LEFT JOIN races ra ON r.id = ra.winner_id
WHERE ra.winner_id IS NULL;




# Answer 2 

SELECT test_a.id
FROM test_a
LEFT JOIN test_b ON test_a.id = test_b.id
WHERE test_b.id IS NULL;


# ANswer 3


SELECT
    u.username,
    td.training_id,
    COUNT(*) AS lesson_count
FROM
    users u
JOIN
    training_details td ON u.user_id = td.user_id
GROUP BY
    u.username,
    td.training_id
HAVING
    COUNT(*) > 1
ORDER BY
    MAX(td.training_date) DESC;
    
    
# Answer 4


SELECT
    Manager_Id,
    Emp_name AS Manager,
    AVG(Salary) AS Average_Salary_Under_Manager
FROM Employee
WHERE Manager_Id IS NOT NULL
GROUP BY Manager_Id, Emp_name
ORDER BY Manager_Id;