#!/usr/bin/python3
"""Defining the square"""


class Square:
    """represent the square"""

    def __init__(self, size=0):
        """Initialize the sqare

        size: the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """obtain the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square"""
        return self.__size ** 2
