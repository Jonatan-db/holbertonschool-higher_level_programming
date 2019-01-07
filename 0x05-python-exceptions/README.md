# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---   

**?**  
*.*  


**?**  
*.*  


**?**  
*.*  


**?**  
*.*  


## Each scripts and their output  
* Script 0 - .    
* Script 1 - .  
* Script 2 - .  
* Script 3 - .  
* Script 4 - .  
* Script 5 - .  
* Script 6 - .  
* Script 7 - .  
* Script 8 - .  
* Script 9 - .  
* Script 10 - .  
* Script 11 - .  
* Script 12 - .  
* Script 13 - .  
* Script 14 - .  
* Script 15 - .  
* Script 16 - .  
* Script 17 - .  
* Script 18 - .  
* Script 19 - .  
* Script 20 - .  
* Script 21 - .  
* Script 100 - .    
* Script 101 - .    
* Script 102 - .    
* Script 103 - .    



What’s the difference between errors and exceptions
Syntax, parsing errors are bad code. Cannot compile. all these are fatal.


exceptions are when syntax is correct and a program can compile but when
executed, now the error happens. They all are not fatal. Lots of python
exceptions are named somethingError which confuses me. What precedes Error is
usually the detail of the type of exception and what caused it. 


What are exceptions and how to use them
They are test code and catch cases. Use them with a try statement. execute the
code between the try and the except keywords. if no exception then except is
skipped and try execution is finished.
if an exception occurs during the try then the rest of the clause is skipped
and if the type matches the except keyWord value, then execute the except
clause.
if an exception does occur but it doesnt match the type, then it will pass onto
the outer try and if no handler is found it will be an unhandled exception and
execution will stop with a message.


When do we need to use exceptions
to know what happened when something broke. have tons of info on what went
wrong.
with exceptions, a programmer must throw errors up a level or handle it.
with error-codes like returning errors, the programer just ignores the errors.
exception allows cleaner code and all cases are covered. Error codes promote
switch case errors in all functions up the stack


How to correctly handle an exception
try and except clauses. Final except doesnt need a name. it is like the last
else in an elif. it is a wild card. Use this with caution cause it can mask a
real problem. else can be used after except to be run after no exceptions.


What’s the purpose of catching exceptions
helps to not crash the program. helps handle edge cases or special conditions.


How to raise a builtin exception
use the raise exception statment. raising exceptions breaks the current code
and returns the exception back until it is handled
Can force a specific error and re-raise exceptions


When do we need to implement a clean-up action after an exception
finally clause is executed always, before leaving the try statement. Finally
will be reraised after finally clause and also on the way out of any other
statements that use break, continue, return, etc. 
Finally is useful for releasing any external resources. 



