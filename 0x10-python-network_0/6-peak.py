#!/usr/bin/python3
""" script that does binary search on an array to find peak """


def find_peak(list_of_integers):
    """
    if list_of_integers is None or list_of_integers is []:
        return None
    if len(list_of_integers) is 1 or len(set(list_of_integers)) is 1:
        return list_of_integers[0]
    mid = int(len(list_of_integers) / 2)

    if list_of_integers >= 3:
        if list_of_integers[mid-1] < list_of_integers[mid] and
                list_of_integers[mid] > list_of_integers[mid+1]:
            return list_of_integers[mid]
    elif (s > 3):
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            find_peak(list_of_integers[int(s):])
            find_peak(list_of_integers[:int(s)-1])
    else:
        return None
    """

    if list_of_integers is None or len(list_of_integers) is 0:
        return None
    return max(list_of_integers)
