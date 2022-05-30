#!/usr/bin/python3
"""File name: 1-my_list.py"""


class MyList(list):
    """print list in acending order"""

    def print_sorted(self):
        print(sorted(self))
