#!/usr/bin/python3
""" module that is a square and imports from rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ is not circle """
    def __init__(self, size):
        """ initializer """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ size squared """
        return(super().area())
