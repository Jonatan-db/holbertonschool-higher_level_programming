#!/usr/bin/python3
""" module and mitali is coking us indian food """


def append_write(filename="", text=""):
    """ writes a string into a text file """

    with open(filename, mode='a+', encoding = "utf-8") as f:
        f.write(text)

    return len(text)
