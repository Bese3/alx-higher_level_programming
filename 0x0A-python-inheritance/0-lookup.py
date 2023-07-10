#!/usr/bin/python3
"""
a method to know all available attributes and methods
"""


def lookup(obj):
    """
    The function "lookup" returns a list of
    all the attributes and methods of an object.
    :param obj: The `obj` parameter is an object
    """
    return dir(obj)
