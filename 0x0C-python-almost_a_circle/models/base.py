#!/usr/bin/python3

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

    def __del__(self):
        if Base.__nb_objects > 0:
            Base.__nb_objects -= 1
        del self