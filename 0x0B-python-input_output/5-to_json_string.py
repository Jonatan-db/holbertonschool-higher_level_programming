#!/usr/bin/python3
""" converts object to JSON """


def to_json_string(my_obj):
    """ returns object to JSON """
    
    import json

    return json.dumps(my_obj)
