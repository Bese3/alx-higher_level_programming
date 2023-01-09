#!/usr/bin/python3
"""
This unittest module tests the class Base in models/base.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """This class has a battery of functions that test every functionality of
    the class Base in module models/base"""

    def test_None_id(self):
        """Tests if id is set correctly to the number of objects
        instantiated when id is None"""
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base(None)
        self.assertEqual(2, b2.id)
        b3 = Base()
        self.assertEqual(3, b3.id)
        b4 = Base(None)
        self.assertEqual(4, b4.id)
        b5 = Base()
        self.assertEqual(5, b5.id)
        b1.__del__()
        b2.__del__()
        b3.__del__()
        b4.__del__()
        b5.__del__()

    def test_passed_id(self):
        """Tests if value passed as id is set correctly"""
        b1 = Base(12)
        self.assertEqual(12, b1.id)
        b2 = Base(0)
        self.assertEqual(0, b2.id)
        b3 = Base(1000)
        self.assertEqual(1000, b3.id)
        b4 = Base(9876544)
        self.assertEqual(9876544, b4.id)
        b1.__del__()
        b2.__del__()
        b3.__del__()
        b4.__del__()

    def test_None_and_passed_mix(self):
        """Mixes value and None passed initializations of Base"""
        b1 = Base(12)
        self.assertEqual(12, b1.id)
        b2 = Base(0)
        self.assertEqual(0, b2.id)
        b3 = Base(-12)
        self.assertEqual(-12, b3.id)
        b4 = Base()
        # Since 6 objects will have been made by the previous functions
        self.assertEqual(1, b4.id)
        b5 = Base(None)
        self.assertEqual(2, b5.id)
        b1.__del__()
        b2.__del__()
        b3.__del__()
        b4.__del__()
        b5.__del__()

    def test_to_json_string(self):
        """Tests the to_json_string method from Base"""
        r = Rectangle(2, 8)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         "[{\"id\": 1, \"width\": 2, \"height\": 8, \"x\": "
                         "0, \"y\": 0}]")
        r.update(x=10, y=90)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         "[{\"id\": 1, \"width\": 2, \"height\": 8, \"x\": "
                         "10, \"y\": 90}]")
        self.assertEqual(r.to_json_string([]), "[]")
        self.assertEqual(r.to_json_string(None), "[]")

    def test_save_to_file(self):
        """Tests if lists of objects are saved successfully into their class
        name with the .json extension. Tests the save_to_file() class method"""

        Square.save_to_file(None)
        with open(Square.__name__ + ".json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([])
        with open(Square.__name__ + ".json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rectangles = [Rectangle(1, 2, 3, 4),
                      Rectangle(5, 6, 7, 8),
                      Rectangle(9, 10, 11, 12),
                      Rectangle(13, 14, 15, 16),
                      Rectangle(17, 18, 19, 20)]
        Rectangle.save_to_file(rectangles)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),
                             "[{\"id\": 1, \"width\": 1, \"height\": 2, "
                             "\"x\": 3, \"y\": 4}, "
                             "{\"id\": 2, \"width\": 5, \"height\": 6, "
                             "\"x\": 7, \"y\": 8}, "
                             "{\"id\": 3, \"width\": 9, \"height\": 10, "
                             "\"x\": 11, \"y\": 12}, "
                             "{\"id\": 4, \"width\": 13, \"height\": 14, "
                             "\"x\": 15, \"y\": 16}, "
                             "{\"id\": 5, \"width\": 17, \"height\": 18, "
                             "\"x\": 19, \"y\": 20}]")
        for rectangle in rectangles:
            rectangle.__del__()
        squares = [Square(1, 3, 4),
                   Square(5, 7, 8),
                   Square(9, 11, 12),
                   Square(13, 15, 16),
                   Square(17, 19, 20)]
        Square.save_to_file(squares)

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             "[{\"id\": 1, \"size\": 1, "
                             "\"x\": 3, \"y\": 4}, "
                             "{\"id\": 2, \"size\": 5, "
                             "\"x\": 7, \"y\": 8}, "
                             "{\"id\": 3, \"size\": 9, "
                             "\"x\": 11, \"y\": 12}, "
                             "{\"id\": 4, \"size\": 13, "
                             "\"x\": 15, \"y\": 16}, "
                             "{\"id\": 5, \"size\": 17, "
                             "\"x\": 19, \"y\": 20}]")
        for square in squares:
            square.__del__()
        #  Remove the two lines below to see the files created by save_to_file
        #  Doing so will break the unittests from running correctly, since
        #  test_load_from_file() will check for non-existing files.
        __import__("os").remove("Rectangle.json")
        __import__("os").remove("Square.json")

    def test_from_json_string(self):
        """Tests the method from_json_string that converts a JSON string to
        a list object"""
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

        r = Rectangle(2, 8)
        self.assertEqual(Base.from_json_string("[{\"id\": 1, \"width\": 2, "
                                               "\"height\": 8, \"x\": " "0, "
                                               "\"y\": 0}]"),
                         [r.to_dictionary()])
        r.update(x=10, y=90)
        self.assertEqual(Base.from_json_string("[{\"id\": 1, \"width\": 2, "
                                               "\"height\": 8, \"x\": "
                                               "10, \"y\": 90}]"),
                         [r.to_dictionary()])

    def test_create(self):
        """Tests the class method create if it works correctly"""
        r1 = Rectangle.create(id=1, width=2, height=4, x=1, y=1)
        self.assertEqual(r1.to_dictionary(), Rectangle(2, 4, 1, 1,
                                                       1).to_dictionary())
        r2 = Rectangle.create(**{"id": 1, "width": 2, "height": 4, "x": 1,
                                 "y": 1})
        self.assertEqual(r2.to_dictionary(), Rectangle(2, 4, 1, 1,
                                                       1).to_dictionary())
        s1 = Square.create(**Square(8, 12, 14, 8).to_dictionary())
        self.assertEqual(s1.to_dictionary(), Square(8, 12, 14,
                                                    8).to_dictionary())

    def test_load_from_file(self):
        """Tests if the class method load_from_file works correctly"""
        l1 = Rectangle.load_from_file()
        self.assertEqual(l1, [])
        l2 = Square.load_from_file()
        self.assertEqual(l2, [])

        rectangles = [Rectangle(1, 2, 3, 4),
                      Rectangle(5, 6, 7, 8),
                      Rectangle(9, 10, 11, 12),
                      Rectangle(13, 14, 15, 16),
                      Rectangle(17, 18, 19, 20)]
        Rectangle.save_to_file(rectangles)
        file_loaded_rectangles = Rectangle.load_from_file()
        for i, j in zip(rectangles, file_loaded_rectangles):
            self.assertEqual(i.__str__(), j.__str__())

        squares = [Square(1, 3, 4),
                   Square(5, 7, 8),
                   Square(9, 11, 12),
                   Square(13, 15, 16),
                   Square(17, 19, 20)]
        Square.save_to_file(squares)
        file_loaded_squares = Square.load_from_file()
        for i, j in zip(squares, file_loaded_squares):
            self.assertEqual(i.__str__(), j.__str__())


if __name__ == '__main__':
    unittest.main()
