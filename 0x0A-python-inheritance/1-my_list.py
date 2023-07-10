#!/usr/bin/python3
"""
The class `MyList` is a subclass of `list`
that adds a method `print_sorted` to print a sorted
list
"""


class MyList(list):
    """
    Inherits list and adds a method print_sorted that
    """
    def __init__(self):
        """
        Calls the super class's init, nothing more
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints a sorted version of the class's instance
        """
        print(sorted(self))
