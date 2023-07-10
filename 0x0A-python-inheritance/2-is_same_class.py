#!/usr/bin/python3
"""
a method to determine the class of an object
"""


def is_same_class(obj, a_class):
    """
    The function checks if an object is an instance of a specific class.
    :param obj: The object that you want to check the class of
    :param a_class: The `a_class` parameter is
    the class that we want to check if the `obj` belongs to
    """
    if type(obj) == a_class:
        return True
    return False
