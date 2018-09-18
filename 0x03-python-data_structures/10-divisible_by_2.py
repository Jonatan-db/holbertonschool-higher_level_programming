#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None
    array = []
    for i in my_list:
        if i % 2 is 0:
            array.append(True)
        else:
            array.append(False)
    return array
