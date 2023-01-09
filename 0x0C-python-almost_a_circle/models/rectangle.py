#!/usr/bin/python3
"""Module rectangle
Contains class Rectangle, which inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Inherits and extends from Base
    Calculates the area of a Rectangle, prints a Rectangle based on its
    width and height
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes all attributes passed with their respective arguments"""
        super().__init__(id)
        # Validate width before assignment
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        # Validate height before assignment
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        #  Validate x before assignment
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Calculates the area of the Rectangle
        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Prints a Rectangle with sides width and height, with the '#' char
        The x and y coordinates are also used to push the Rectangle in the x
        and y directions when printing"""
        rectangle_repr = ""

        rectangle_repr += "\n" * self.__y
        for i in range(self.__height):
            rectangle_repr += self.__x * " "
            for j in range(self.__width):
                rectangle_repr += "#"
            rectangle_repr += "\n" if i != self.__height - 1 else ""

        print(rectangle_repr)
        return rectangle_repr

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
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key in kwargs.keys():
                self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """Returns a key-value pair of all attributes and their values"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width to value, raises exception if value is
        not an integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the Rectangle's height to value, raises exception if value is
        not an integer"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x position of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x to value, raises exception if value is
        not an integer"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the x position of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y to value, raises exception if value is
        not an integer"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
