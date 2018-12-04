-- Import in hbtn_0c_0 database this table dump
-- imports and averages stuff
SELECT state, MAX(value) FROM temperatures GROUP BY state
