#!/usr/bin/python3
"""File name: 8-class_to_json.py"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
