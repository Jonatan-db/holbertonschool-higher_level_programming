How to create a new MySQL user
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

How to manage privileges for a user to a database or table
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
ALL PRIVILEGES, CREATE, DROP, DELETE, INSERT, SELECT, UPDATE, GRANT OPTION
Lots of other command exist http://www.mysqltutorial.org/mysql-grant.aspx.
GRANT type\_of\_permission ON database\_name.table\_name TO ‘username’@'localhost’;
REVOKE type\_of\_permission ON database\_name.table\_name FROM ‘username’@‘localhost’;
SHOW GRANTS username;
DROP USER ‘username’@‘localhost’;
To test quit the CLI, and try to log back in as the user. mysql -u [username] -p


What’s a PRIMARY KEY
A constraint that uniquly identidies each record in a database table. Primary keys cannot be NULL, unique keys can be. Primary keys are the only one in a table. They are important when desgining the database tables. Primary keys are unique ids and we use the, to refer to table rows. 
Primary keys become foreign keys in other tables when creating relations among them.
mysql> CREATE TABLE Brands(Id INTEGER PRIMARY KEY, BrandName VARCHAR(30) UNIQUE);


What’s a FOREIGN KEY
A foreign key in one table points to a primary key in another table. It is a referential constraint between 2 tables. The foreign key identidies a cplimn or a set of column in one table that references a solumn or set in another table.

mysql> CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name VARCHAR(70))
    -> type=InnoDB;

mysql> CREATE TABLE Books(BookId INTEGER PRIMARY KEY, Title VARCHAR(50),
    -> AuthorId INTEGER, FOREIGN KEY(AuthorId) REFERENCES Authors(AuthorId))
    -> type=InnoDB;

How to use NOT NULL and UNIQUE constraints
A column with a NOT NULL constraint, cannot have NULL values.
mysql> CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL,
    ->                     FirstName TEXT NOT NULL, City VARCHAR(55));

For unique, it makes sure all data is unique in a column.
mysql> CREATE TABLE Brands(Id INTEGER, BrandName VARCHAR(30) UNIQUE);


How to retrieve datas from multiple tables in one request
Join. Natural join will specify the attributes whose values are matched with the names. 
Inner join. Most common. Returns all rows where the 2 or more tables overlap. uses ON.
LEFT OUTER JOIN is all A including overlap.
LEFT OUTER JOIN WHERE B.columnName IS NULL will exclude the overlap.
RIGHT OUTER JOIN is same concept.
FULL JOIN or entire outer join basically returns all rows.
FULL JOIN where A.column IS NULL or B.column IS NULL is everything but the overlap.



What are subqueries
A query in a query. Subqueries can also be used when we need more than a single value as part of a larger query. Ususally encloded in parenthesis after the WHERE. 

What are JOIN and UNION
Union included members of both sets with no duplicates and minus includes the members of the set on the left that are not contained in the set on the right side. Join joins. 
