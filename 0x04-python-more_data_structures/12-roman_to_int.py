#!/usr/bin/python3
def helper(i):
    if i is "I":
        return 1
    elif i is "V":
        return 5
    elif i is "X":
        return 10
    elif i is "L":
        return 50
    elif i is "C":
        return 100
    elif i is "D":
        return 500
    elif i is "M":
        return 1000
    else:
        return 0


def roman_to_int(roman_string):
    count = 0
    past = 0
    number = 0

    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in roman_string:
        number = helper(i)
        if number is 0:
            return 0
        if count is 0:
            count += number
        elif past < number:
            count -= number
        elif past >= number:
            count += number
        past = number
    return abs(count)
