#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx is 0 or my_list is None:
        return my_list
    del my_list[idx]
