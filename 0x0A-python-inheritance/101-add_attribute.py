#!/usr/bin/python3

"""101-add_attribute
Contains function add_attribute
"""


def add_attribute(obj, attr_name, attr_value):
    """Adds attribute to object if possible
    Args:
        obj (object): any kind of object to add attribute to
        attr_name (str): name of new attribute
        attr_value (object): value of new attribute
    """
    if type(attr_name) is not str or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
