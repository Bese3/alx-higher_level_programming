#!/usr/bin/python3

"""
 The above class is a locked class that only
 allows the attribute 'first_name' to be assigned.
"""


class LockedClass:
    """
    # The `__slots__` attribute is used to explicitly
    define the attributes that a class can have. In
    """
    __slots__ = ['first_name']
