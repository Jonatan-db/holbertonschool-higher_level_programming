


What is Unit testing and how to implement it in a large project
Unit testing is testing one specific cast. A unit. How we do dis?
https://www.pythonsheets.com/notes/python-tests.html



How to serialize and deserialize a Class
We can use pickle. Fornat and protocols. Which serialization scheme can
determine many things.
How fast the program is, how secure it is, how much freedom I have while
maintenance, how well it will communicate with other systems.
Use pickle, dump, dumps, load, and loads. 
dump() serializes into a string and load() deserializes from an open file-like
object. 
load() deserializes froma string.
Here is nice resource
https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183
First we load,
variable = pickle.loads("(string)")
Unpickle with assert variable\_name = parameter


How to write and read a JSON file
JSON module also has dumps, dump, load, loads. 
We need to use a CustomEncoder class for Json stuff and json.JSONEncoder.
https://docs.python.org/3/library/json.html


What is \*args and how to use it
args is a magic variable. args is used to send non keyworded variable length
argument list.
args is like ... or variadic functions. eg.
def test\_args(f\_arg, \*argv):
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/


What is \*\*kwargs and how to use it
kwargs allows passed keyworded variable length arguments. Use this if i want to
handle named arguments into a function
eg. 
def greet\_me(\*\*kwargs):
So use this when i ass in some keyword parameters like list and a list or name
stuff.


How to handle named arguments in a function
kwags. 
some\_func(fargs,\*args,\*\*kwargs)









Other info/ concepts this project covers:

Import

Exceptions

Class

Private attribute

getter/setter

class method

static method

inheritance

unittest

read/write file



`
args / kwargs
serialization/ deserialization
JSON


