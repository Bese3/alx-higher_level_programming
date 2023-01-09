#!/usr/bin/python3

"""2-is_same_class
Contains function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is instance of a_class

    Args:
        obj (object): object to be check if is instance of a_class
        a_class (object): class blueprint to check if obj is made from it

    Returns:
        True if the object is exactly an instance of the specified class,
        otherwise False.
    """
    return obj.__class__.__name__ == a_class.__name__
