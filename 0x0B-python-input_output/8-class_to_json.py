#!/usr/bin/python3

"""8-class_to_json
Contains function class_to_json
"""


def class_to_json(obj):
    """Serializes obj's attributes in JSON format

    Args:
        obj (object): Object's attributes to be serialized

    Returns:
        JSON formatted attributes of obj
    """
    return obj.__dict__
