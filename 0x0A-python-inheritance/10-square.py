#!/usr/bin/python3
"""File name: 10-square.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherence"""
    def __init__(self, size):
        """initialize the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
