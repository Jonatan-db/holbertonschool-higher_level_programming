#!/usr/bin/python3
""" module that reads files """


def read_file(filename=""):
    """ reads files """

    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end='')
