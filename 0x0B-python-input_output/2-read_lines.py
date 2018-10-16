#!/usr/bin/python3
""" does what wc does but as a module """


def read_lines(filename="", nb_lines=0):
    """ prints up to the whole file if directed """
    with open(filename, mode='r', encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read())
        else:
            while nb_lines:
                print(f.readline())
                nb_lines -= 1
