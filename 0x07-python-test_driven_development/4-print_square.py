#!/usr/bin/python3
"""File name: 4-print_square.py
Print Square: prints a square with the character #
Prototype: def print_square(size):
"""


def print_square(size):
    """finction to print a square with the character #
    size the number of # to be printed
    Rises:
        TypeError: size must be an integer
        ValueError:
    """

    if (not isinstance(size, int) or
            isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        else:
            print("")
