#!/usr/bin/python3
""" module and mitali is coking us indian food """


def write_file(filename="", text=""):
    """ writes a string into a text file """

    with open(filename, mode='w', encoding = "utf-8") as f:
        f.write(text)

    return len(text)
