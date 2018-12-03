-- Write a script that lists the number of records with the same score in the table 
-- find number of occurances
SELECT score, count(*) 'number' from second_table GROUP BY score DESC
