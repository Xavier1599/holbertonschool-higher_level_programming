#!/usr/bin/python3
"""File name: 8-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from class BaseGeometry

    Atributtes:

        width: The rectangles width
        heigth the rectangle height
    """

    def __init__(self, width, height):
        """private atributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
