#!/usr/bin/python3
""" does what wc does but as a module """


def number_of_lines(filename=""):
    """ counds number of lines """

    count = 0
    with open(filename, mode='r', encoding="utf-8") as f:
        while f.readline():
            count += 1
    return count
