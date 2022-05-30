#!/usr/bin/python3
"""File name: 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """define if a obj is instance of class"""
    if isinstance(obj, a_class):
        return True
    return False
