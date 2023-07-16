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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The function `save_to_file` saves a
        list of objects to a JSON file.
        """
        new = []
        # print(cls.__name__ + ".json")
        with open(cls.__name__ + ".json", mode="w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            for i in range(len(list_objs)):
                if i == 0:
                    first = "["
                else:
                    first = ""
                if i != len(list_objs) - 1:
                    last = ", "
                else:
                    last = "]"
                f.write(first + Base.to_json_string
                        (cls.to_dictionary(list_objs[i])) + last)

    def from_json_string(json_string):
        """
        The function `from_json_string`
        converts a JSON string into a Python object.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    def __del__(self):
        """
        The __del__ function decreases the value
        of Base.__nb_objects by 1 and deletes the instance.
        """
        if Base.__nb_objects > 0:
            Base.__nb_objects -= 1
        del self
