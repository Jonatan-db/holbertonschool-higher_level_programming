#!/usr/bin/python3
""" module that returns true or false"""


def is_same_class(obj, a_class):
    """ tests if obj is an instance of a_class """

    if type(obj) is a_class:
        return True
    return False
