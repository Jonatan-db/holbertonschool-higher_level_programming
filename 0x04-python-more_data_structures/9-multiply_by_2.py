#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    newDic.update((key, value * 2) for key, value in newDic.items())
    return newDic
