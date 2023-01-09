-- lists all records of the table second_table who have scores greater than
-- 10 of the database hbtn_0c_0 in the MySQL server
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY (score) DESC;