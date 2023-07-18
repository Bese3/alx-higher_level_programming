#!/usr/bin/python3

"""Base class for all project to be done"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        The function `to_json_string` converts
        a list of dictionaries into a JSON string.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the list of objects to a file with cls' class name (
        clsName.json) in JSON format"""

        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            for i in range(len(list_objs)):
                if i == 0:
                    f.write("[")
                if i + 1 != len(list_objs):
                    eof = ", "
                else:
                    eof = "]"
                f.write(Base.to_json_string(list_objs[i].to_dictionary()) +
                        eof)

    @staticmethod
    def from_json_string(json_string):
        """
        The function `from_json_string`
        converts a JSON string into a Python object.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        The function creates an instance of
        a class and updates its attributes using a dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                this = cls(1, 1)
            else:
                this = cls(1)
            this.update(**dictionary)
            return this
        return []

    @classmethod
    def load_from_file(cls):
        """
        The function `load_from_file` loads data from
        a JSON file and creates instances of a class based
        on the data.
        """
        try:
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
                new = []
                pyth_obj = Base.from_json_string(f.read())
                for i in pyth_obj:
                    new.append(cls.create(**i))
                # return new
        except FileNotFoundError:
            return []
        return new

    def __del__(self):
        """
        The __del__ function decreases the value
        of Base.__nb_objects by 1 and deletes the instance.
        """
        if Base.__nb_objects > 0:
            Base.__nb_objects -= 1
        del self
