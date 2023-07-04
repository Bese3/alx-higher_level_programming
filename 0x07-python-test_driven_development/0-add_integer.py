#!/usr/bin/python3

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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)
    return(a + b)
