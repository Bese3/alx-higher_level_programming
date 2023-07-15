#!/usr/bin/python3
import json

"""Base class for all projec to be done"""

class Base:
    """
    The `Base` class initializes objects with
    an optional id, and if no id is provided, it assigns a
    unique id to the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The function initializes an object with an optional id,
        and if no id is provided, it assigns a
        unique id to the object.

        :param id: The `id` parameter is an optional
        parameter that can be passed to the `__init__`
        method.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        The function `to_json_string` converts
        a list of dictionaries into a JSON string.
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    def __del__(self):
        """
        The __del__ function decreases the value
        of Base.__nb_objects by 1 and deletes the instance.
        """
        if Base.__nb_objects > 0:
            Base.__nb_objects -= 1
        del self
