#!/usr/bin/python3

"""4-inherits_from
Contains function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False.
    """

    x = False
    for i in a_class.__mro__:
        if i.__name__ == obj.__class__.__name__:
            x = True
    instance_and_subclass = isinstance(obj, a_class) and issubclass(
        obj.__class__, a_class)
    return instance_and_subclass and not x
