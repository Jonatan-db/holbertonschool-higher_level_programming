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



What are set and how to use them
a set is a unordered collection with no duplicates. basic usage include members and eliminating duplicate entries. math can be used with sets. make sets with curly braces {} or set(). 
What are the most common methods of set and how to use them

When to use sets versus lists
sets are faster when seeing if there is a duplicate. lists are faster when iterating.

How to iterate into a set
a = {x for x in 'abracadabra' if x not in 'abc'}

What are dictionary and how to use them
basically like an array but instead of 1 index holding 1 value, the index holds a key which holds a value. key: value. keys are immutable. values can be changed. key : value pairs in an unordered set are dictionaries. {} creates an empty dic. put commas between pairs. Can use del on a key. doing a list(d.keys()) will return a list of all the keys in the dictionary. use in to test if a key is in a dic. 

When to use dictionaries versus lists or sets
when to use a dictionary is a kay and a value, so like name and string or age and int. lists is an ordered type. set is when items can be hashable. dictionaries have unique keys that map to values. so kinda like sets and lists combined. 

What is a key in a dictionary
a key is a unique. it must be quoted. keys map to values. dictionaries map keys which map values. dictionaries and the key values are mutable. dictionaries are unordered. 

How to iterate into a dictionary
dictionary.key() syntax. look at this example : for key, val in released,.items():
print key, "=>", val

What is a lambda function
an anonomous function. short. "lambda arguments: expression" so we can write something like
"double = lambda x: x\*2"

What is map, reduce and map functions
map() returns an iterator in python3, before it returned a list. map(function,list) basically pushes a list through a function. filter() will filter out anything that passes the expression as True. reduce() was removed in new python and is now in the functools module. reduce will iterate through a list and apply a function. https://www.python-course.eu/python3\_lambda.php

