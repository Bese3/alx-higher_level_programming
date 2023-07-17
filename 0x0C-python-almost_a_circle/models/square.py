#!/usr/bin/python3

"""
Module square
Contains class Square, which inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """By inheriting the characteristics of Rectangle, defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes all attributes passed with their respective arguments"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get width of Rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """Set width to value, raises exception if value is
        not an integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates some or all of the attributes based on how many arguments
        are passed
        If args' list index gets out of range i.e. it gets to the end of the
        list, the updating of the attributes gets done

        If args is empty, the values in kwargs are used to update the
        attributes' values"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key in kwargs.keys():
                try:
                    if key == "size":
                        self.__setattr__("width", kwargs[key])
                        self.__setattr__("height", kwargs[key])
                        continue
                    self.__setattr__(key, kwargs[key])
                except AttributeError:
                    pass

    def to_dictionary(self):
        """Returns a key-value pair of all attributes and their values"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
