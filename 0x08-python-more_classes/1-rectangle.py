#!/usr/bin/python3
"""File name: 1-rectangle.py
Rectangle: class that defines a rectangle
"""


class Rectangle(object):
    """Rectangle: defining the class"""
    def __init__(self, width=0, heigth=0):
        """Initialie the rectangle
        
        Args:
                width: the width of the rectangle set to 0
                heigth: the heigth of the rectangle
        """
        self.width = width
        self.height = heigth

    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__heigth

    @property
    def heigth(self):
        """set the heigth of the rectangle"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value
