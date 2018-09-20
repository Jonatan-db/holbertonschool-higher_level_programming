#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if all(value == None for value in a_dictionary.values()):
        return None
    return max(a_dictionary, key=a_dictionary.get)
