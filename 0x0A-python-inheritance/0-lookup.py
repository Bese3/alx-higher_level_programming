#!/usr/bin/python3

"""Module 0-lookup
Contains function lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return [x for x in dir(obj)]
