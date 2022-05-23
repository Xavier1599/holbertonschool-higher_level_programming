#!/usr/bin/python3
"""File name: 1-rectangle.py
Rectangle: class that defines a rectangle
"""


class Rectangle:
    """Rectangle: defining the class"""
    def __init__(self, width=0, height=0):
        """Initialie the rectangle
        Args:
                width: the width of the rectangle set to 0
                heigth: the heigth of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the heigth of the rectangle"""
        return self.__heigth

    @height.setter
    def height(self, value):
        if not type(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
