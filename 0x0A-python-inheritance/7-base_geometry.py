#!/usr/bin/python3
"""File name: 7-base_geometry.py
Represent BaseGeometry Class"""


class BaseGeometry:
    def area(self):
        """Represent the area"""
        raise Exception("area () is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be grater than 0".format(name))
