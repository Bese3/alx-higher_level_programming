#!/usr/bin/python3
from models.base import Base
"""
The Rectangle class is defined as a subclass of the
Base class, with attributes for width, height,
x, y, and id, and methods for validating and setting these attributes.
"""


class Rectangle(Base):
    """defination of the Rectangle class inerited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The function initializes an object with
        width, height, x, y, and id attributes, and validates
        the input values.
        """
        super().__init__(id)
        # validate width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        # validate height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        # validate x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("width must be >= 0")
        self.__x = x
        # validate y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width to value, raises exception"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the Rectangle's height to value, raises exception"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the X value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the X value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the Y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the Y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This function calculates the area of rectangle
        """
        return self.__height*self.__width

    def display(self):
        """
        This function displays using x,y,width and height
        """
        rectangle = ""
        for k in range(self.__y):
            print()
            rectangle += "\n"
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
                rectangle += " "
            for j in range(self.__width):
                print("#", end="")
                rectangle += "#"
            rectangle += "\n"
            print()
        return rectangle

    def __str__(self):
        """
        The function returns a string representation
        of a Rectangle object, including its id,coordinates,
        width, and height.
        """
        string = F"[Rectangle] ({self.id}) {self.x}/{self.y}" + \
            F" - {self.width}/{self.height}"
        return string

    def update(self, *args, **kwargs):
        """
        The function updates the attributes of an object
        with the values provided in the arguments.
        """
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
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """
        The function `to_dictionary` returns
        a dictionary with the attributes of an object.
        """
        first = {'x': self.x, 'y': self.y, 'id': self.id}
        second = {'height': self.height, 'width': self.width}
        first.update(second)
        return first
