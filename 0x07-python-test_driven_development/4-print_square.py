#!/usr/bin/python3
"""
python code
"""


def print_square(size):
    """
    The function `print_square` prints a square
    made of "#" characters with a given size.
    """
    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for rows in range(size):
        for i in range(size):
            print("#", end="")  # prints '#'
        print()
