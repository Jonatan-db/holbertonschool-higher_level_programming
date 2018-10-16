#!/usr/bin/python3
""" module that sorts and prints a list """


class MyList(list):
    """ all it does is sort and print"""

    def print_sorted(self):
        """ sorts then prints """
        print(sorted(self))
