#!/usr/bin/python3
""" writes an object into a text file using JSON """


def save_to_json_file(my_obj, filename):
    """ the function """

    import json

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
