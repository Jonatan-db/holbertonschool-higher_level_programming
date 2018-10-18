#!/usr/bin/python3
""" rectangle module """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @classmethod
    def typeChecker(self, name, value):
        """ integer validation check """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @classmethod
    def valueWHChecker(self, name, value):
        """ width and height validation check """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @classmethod
    def valueXYChecker(self, name, value):
        """ x and y validation check """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter, gets validated """
        self.typeChecker("width", value)
        self.valueWHChecker("width", value)
        self.__width = value


    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        """ height setter, gets validated """
        self.typeChecker("height", value)
        self.valueWHChecker("height", value)
        self.__height = value


    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, value):
        """ X setter, gets validated """
        self.typeChecker("x", value)
        self.valueXYChecker("x", value)
        self.__x = value


    @property
    def y(self):
        return self.__y
        
    @y.setter
    def y(self, value):
        """ Y setter, gets validated """
        self.typeChecker("y", value)
        self.valueXYChecker("y", value)
        self.__y = value

    @classmethod
    def area(self):
        return self.width * self.height
