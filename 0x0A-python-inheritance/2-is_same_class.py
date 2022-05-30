#!/usr/bin/python3
"""File name: 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """define if obj is instance of the class"""
    if type(obj) == a_class:
        return True
    return False
