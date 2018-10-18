#!/usr/bin/python3
""" module and base of all other classes """


class Base:
    """ BaseClass of all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiator """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            __nb_objects = id
