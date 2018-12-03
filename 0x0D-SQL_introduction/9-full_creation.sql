-- Write a script that creates a table second_table
-- Creates a second new table
CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL,
name VARCHAR(256),
score INT);
-- inserts data into the table
INSERT INTO second_table VALUES (1, "John", 10);
-- inserts data into the table
INSERT INTO second_table VALUES (2, "Alex", 3);
-- inserts data into the table
INSERT INTO second_table VALUES (3, "Bob", 14);
-- inserts data into the table
INSERT INTO second_table VALUES (4, "George", 8);
