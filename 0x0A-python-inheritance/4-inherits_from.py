#!/usr/bin/python3
"""
a method to determine if a obj is only subclass of class
"""


def inherits_from(obj, a_class):
    """
    The function `inherits_from` checks if an object
    inherits from a specific class.
    :param obj: The `obj` parameter is an object that
    we want to check if it inherits from a specific
    class
    :param a_class: The `a_class` parameter is the
    class that we want to check if `obj` inherits from

    """
    hold = True
    for i in a_class.__mro__:
        if i.__name__ == obj.__class__.__name__:
            hold = False
    sub = issubclass(obj.__class__, a_class)
    return sub and hold
