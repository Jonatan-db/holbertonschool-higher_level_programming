#!/usr/bin/python3
def search_replace(my_list, search, replace):
#    return [replace if i == search else i for i in my_list]
    for index, i in enumerate(my_list):
        print(i , index)
        if i == search:
            my_list.insert(index, search)
    return my_list
