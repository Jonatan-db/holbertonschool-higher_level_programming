-- Import in hbtn_0c_0 database this table dump
-- imports and averages stuff
SELECT state, MAX(value) 'max_temp' FROM temperatures GROUP BY state
