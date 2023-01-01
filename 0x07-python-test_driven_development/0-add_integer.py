#!/usr/bin/python3

"""0-add_integer.py
Holds the function add_integer(a, b) and used to test the function using
tests/0-add_integer.txt
"""


def add_integer(a, b=98):
    """
    Adds the parameters and returns their sum. If a or b is neither integer nor
    float, a TypError with exception with the message a must be an integer
    or b must be an integer is returned.

    Args:
        a (int, float): first number to be added
        b (int, float): second number to be added, 98 by default
    Returns:
        a + b, the sum of the arguments
    """

    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if b is None or type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return a + b
