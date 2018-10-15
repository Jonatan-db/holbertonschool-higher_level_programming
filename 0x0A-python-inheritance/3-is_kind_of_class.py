#!/usr/bin/python3
""" module that returns true or false"""


def is_kind_of_class(obj, a_class):
    """ true if object is an instance of the class """

    if isinstance(obj, a_class):
        return True
    return False
