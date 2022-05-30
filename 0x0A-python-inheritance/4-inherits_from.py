#!/usr/bin/python3
"""File name: 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """define if obj is isistance of the class"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
