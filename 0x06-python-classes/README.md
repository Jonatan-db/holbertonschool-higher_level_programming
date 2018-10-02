


What is OOP
4 principles of OOP which are encapsulation, abstraction, inheritance, and polymorphism.


what is “first-class everything”
Everything in python is a class. there are no restrictions to their use. the object can be dynamically created, destroyed, passed to a function, returned, and stored.
Mainly can be used as arguments or return them.


What is a class
It keeps relative things together. A class is a template for creating objects. 
an object is created when using the constructor of the class and the object will then be called the instance of the class.


What is an object and an instance
read above. here is an example though- Instance = class(arguments). To make an object I could have used dog = DOG() and i had previously made a class named DOG. If we printed(dog) then the output would have been <\_\_main\_\_.DOG object at 0xMEMORYaddress>.


What is the difference between a class and an object or instance
A blueprint is a class. All the houses built from the blueprint are objects of that class. Any specific house is an instance.
Class >> Object >> Instance.


What is an attribute
An instance is a copy of the class with actual values. All objects have attributes which are it's characteristic. 
Use \_\_init\_\_ to initialize the objects initial default values or state.


What are and how to use public, protected and private attributes
Use of no \_ is public. One \_ is protected. And \_\_ is private.


What is self
Like Java's this. Self refers to the newly created object and in other class methods, it will refer to the instance that called it via a method.
Link to Guido van Rossum's post about keeping self http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html.


What is a method
A function.


What is the special \_\_init\_\_ method and how to use it
It is a special method in Python and it is the constructor for a class.
It initializes attributes. init is called when an object is constructed.
When we create the object, self points to the current object.

What is Data Abstraction, Data Encapsulation, and Information Hiding
Encapsulation is achieved when each object keep its state private inside a class.
Other objects cammot access it. They can only call on public methods. 

Abstraction is an extension of encapsulation. Each object should only expose a high level mechanism. You should hide internal lower level details. Only reveal operations relevant for other objects. Kind of like a car. You hit gas and break and steer but wtf goes on? I dunno.

Inheritance, when rich old people die and give their money to spoiled brats. JK. This is for when we want to reuse common logic and form a hierarchy. The child class reuses all fields and methods of the parent. Can implement its own unique methods. We can have a human class but not all humans are doctors, students, or sociopaths.

Polymorphism means many shapes. Inheriting some traits from some classes. It is inheritance on a bigger scale and more complicated. We can use a class exactly like it's parent but each child can keep their methods.

What is a property
@property. Helpful with backwards compatibility. Property is a builtin that creates and returns a property object. 
Property objects have 3 mothods, getter, setter, and deleter. It specifies fset, fget, fdel.
property(fget=None, fset=None, fdel=None, doc=None) is the signature of a property.


What is the difference between an attribute and a property in Python
Properties are special attributes. If the instance has a get, set, or delete method, it is a property.


What is the Pythonic way to write getters and setters in Python
https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters


advanced:


How to dynamically create arbitrary new attributes for existing instances of a class
setattr(e, name, value)


How to bind attributes to object and classes
One trick is to dynamically define the function to be added, nested within the function that applies the patch like so:

https://rosettacode.org/wiki/Add\_a\_variable\_to\_a\_class\_instance\_at\_runtime#Python
Scroll down to python


What is and what does contain \_\_dict\_\_ of a class and of an instance of a class


How does Python find the attributes of an object or class


How to use the getattr function
