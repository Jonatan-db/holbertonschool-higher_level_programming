#!/usr/bin/python3
""" more practice with classes!!! """


class Rectangle:
    """ initialize with the width and height with value checks

    Args:
        width: how phat dis 4polygon gon be
        height: how tall dis box is

    Return: nonezo
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the area of this rekt """
        return self.width * self.height

    def perimeter(self):
        """ calculates the perimeter of this rect """
        if self.width is 0 or self.height is 0:
            return 0
        return (self.width * 2) + (self.height * 2)
