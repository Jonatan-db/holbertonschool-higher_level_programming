#!/usr/bin/python3
""" rectangle module """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def typeChecker(self, name, value):
        """ integer validation check """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def valueWHChecker(self, name, value):
        """ width and height validation check """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

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

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.width + self.x):
                if x >= self.x:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()

    def __str__(self):
        return("[{}] ({}) {}/{} - {}/{}".format(
            str(self.__class__.__name__), self.id, self.x,
            self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        if args is not None and len(args):
            for index, value in enumerate(args):
                if index is 0:
                    self.id = value
                elif index is 1:
                    self.width = value
                elif index is 2:
                    self.height = value
                elif index is 3:
                    self.x = value
                elif index is 4:
                    self.y = value
                elif index >= 6:
                    raise Exception("Too many arguments")

            """ This wont work for anything other than 5 args
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

            elif len(args):
                raise Exception("Need 5 args:  id, width, height, x, y")
            """
        else:
            for key in kwargs:
                if key is "id":
                    self.id = kwargs["id"]
                elif key is "width":
                    self.width = kwargs["width"]
                elif key is "height":
                    self.height = kwargs["height"]
                elif key is "x":
                    self.x = kwargs["x"]
                elif key is "y":
                    self.y = kwargs["y"]
