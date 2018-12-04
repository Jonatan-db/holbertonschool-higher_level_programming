-- Write a script that lists all cities contained in the database
SELECT cities.id, cities.name 'name', states.name 'name'
FROM cities
JOIN states
ON cities.id = states.id
