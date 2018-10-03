#!/usr/bin/python3
def add_integer(a, b=98):
    """
    A function that adds two integers, b is default 98
    a and b  should be an int, if not throw error.
    b has a default of 98
    """

    def __init__(self, a, b):
        """
        sets the values of the attributes by calling on the setter functions
        """
        self.a = a
        self.b = b

    @property
    def a(self):
        """ a getter function for a """
        return self.__a
    
    @a.setter
    def a(self, value):
        """ a setter function for a """
        if type(a) is int or type(a) is float:     
            self.__a = value
        else:
            raise TypeError("a must be an integer")

    @property
    def b(self):
        """ a getter for b """
        return self.__b

    @b.setter
    def b(self, value):
        """ a setter for b """
        if type(b) is int or type(b) is float:
            self.__b = value
        else:
            raise TypeError("b must be an integer")
   
    def __repr__(self):
        """ return the addition """
        return self.__a + self.__b
