#!/usr/bin/python3
""" module that replaces. needle in haystack but in python """


def append_after(filename="", search_string="", new_string=""):
    """ needle in haystack. string in a string """

    prompt = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for i in f:
            prompt += i
            if search_string in i:
                prompt += new_string
    """ could use f.seek(0) to reset instead of reopen file """

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(prompt)
