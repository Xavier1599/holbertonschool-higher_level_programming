#!/usr/bin/python3
"""File name: 2-rectangle.py
Rectingle: defining the class and atributes of the class
"""


class Rectangle:
    """represent the rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the rectsangle

        Args:
            width: the width of the rectangle
            heigth: the heigth of the triangle
        """
        self.width = width
        self.height = height

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
        self.__width = value

    @property
    def height(self):
        """set the heigth of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def arena(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the primeter of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))
