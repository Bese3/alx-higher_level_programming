#!/usr/bin/python3
"""
a method to determine if an object is class or subclassed
"""


def is_kind_of_class(obj, a_class):
    """
    The function checks if an object is an instance of a given class.
    :param obj: The object that you want to check the class of
    :param a_class: The `a_class` parameter is the class that
     you want to check if the `obj` belongs to
    or is a subclass of

    """
    if isinstance(obj, a_class):
        return True
    return False
