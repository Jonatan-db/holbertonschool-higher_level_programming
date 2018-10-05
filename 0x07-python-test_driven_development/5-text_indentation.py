#!/usr/bin/python3
""" function that prints a text with new lines """


def text_indentation(text):
    """ After each . ? and : print 2 new lines

    Args:
        text: the wall of text that we are given

    Return: none, just print
    """
    flag = 0
    if text is "":
        print()
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i is ' ':
            flag = 1
        if i is '.' or i is '?' or i is ':':
            flag = 1
            print(i)
            print()
        elif flag is 1 and i is ' ':
            pass
        else:
            print(i, end='')
            flag = 0
