#!/usr/bin/python3
""" module returns true or false """


def inherits_from(obj, a_class):
    """ returns true if object is instance of a class """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
