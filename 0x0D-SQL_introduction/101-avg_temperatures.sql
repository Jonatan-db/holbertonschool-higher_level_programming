-- Import in hbtn_0c_0 database this table dump
-- imports and averages stuff
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC
