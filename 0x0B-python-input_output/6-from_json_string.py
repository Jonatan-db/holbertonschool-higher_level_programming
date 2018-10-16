#!/usr/bin/python3
""" go from JSON to python object """


def from_json_string(my_str):
    """ from JSON string to python obj """

    import json

    return json.loads(my_str)
