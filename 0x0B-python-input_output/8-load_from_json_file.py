#!/bin/bash/python3
""" a function that creates an object form a json file """


def load_from_json_file(filename):
    """ loads from JSON file """

    import json

    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
