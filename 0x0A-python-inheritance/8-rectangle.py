#!/usr/bin/python3
""" module that inherits from basegeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from the imported module """

    def __init__(self, width, height):
        """ setter method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
