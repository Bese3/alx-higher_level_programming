#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""testing modlue for Base class"""


class TestBase(unittest.TestCase):
    """
    The TestBase class tests the creation and deletion of
    instances of the Base class
    """
    def test_none(self):
        """
        The function tests the creation and deletion
        of instances of the Base class, checking their id
        values.
        """
        a = Base()
        self.assertEqual(a.id, 1)
        self.assertNotEqual(a.id, 2)
        b = Base()
        self.assertEqual(b.id, 2)
        self.assertNotEqual(b.id, 3)
        c = Base(None)
        self.assertEqual(c.id, 3)
        self.assertNotEqual(c.id, 4)
        del a
        del b
        del c

    def test_id(self):
        """
        Tests the functionality of the `Base` class
        by creating instances with different arguments.
        """
        d = Base(1)
        self.assertEqual(d.id, 1)
        e = Base(12)
        self.assertEqual(e.id, 12)
        f = Base(12332)
        self.assertEqual(f.id, 12332)
        del d
        del e
        del f

    def test_mixed(self):
        """
        The function `test_mixed` tests the behavior
        of the `Base` class by creating instances with
        different arguments and asserting that their
        `id` attributes have the expected values.
        """
        a = Base(12)
        self.assertEqual(a.id, 12)
        b = Base(13)
        self.assertEqual(b.id, 13)
        c = Base()
        self.assertEqual(c.id, 1)
        d = Base(None)
        self.assertEqual(d.id, 2)
        del a
        del b
        del c
        del d

    def test_to_json(self):
        """
        The function `test_to_json` tests the `to_json_string`
        method of the `Base` class by checking
        its behavior with different input dictionaries and lists.
        """
        # if empty
        dict1 = None
        a = Base(12)
        self.assertEqual(a.to_json_string(dict1), "[]")
        self.assertNotEqual(a.to_json_string(dict1), [1])
        # non empty dict
        dict1 = {'id': 1, 'x': 0, 'y': 0, 'height': 2, 'width': 2}
        self.assertEqual(a.to_json_string(dict1),
                         '{"id": 1, "x": 0, "y": 0, "height": 2, "width": 2}')
        self.assertEqual(eval(a.to_json_string(dict1)),
                         {"id": 1, "x": 0, "y": 0, "height": 2, "width": 2})
        dict1 = [1, 2, 3, 4]
        self.assertEqual(a.to_json_string(dict1), '[1, 2, 3, 4]')
        a = Rectangle(10, 7)
        self.assertEqual(a.to_json_string(a.to_dictionary()),
                         '{"x": 0, "y": 0, "id": 1, "height": 7, "width": 10}')
        a.update(x=10, y=9)
        string = '{"x": 10, "y": 9, "id": 1, "height": 7, "width": 10}'
        self.assertEqual(a.to_json_string(a.to_dictionary()), string)
        self.assertEqual(a.to_json_string([]), "[]")
        self.assertEqual(a.to_json_string(None), "[]")
        del a

    def test_save_to_file(self):
        """
        The function `test_save_to_file` tests the
        `save_to_file` method of the `Rectangle` and `Square`
        classes.
        """
        Rectangle.save_to_file(None)
        with open(Rectangle.__name__ + ".json",
                  mode="r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([])
        with open(Rectangle.__name__ + ".json",
                  mode="r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")
        a = Rectangle(2, 4)
        my_list = [a]
        Rectangle.save_to_file(my_list)
        with open(Rectangle.__name__ + ".json",
                  mode="r", encoding="utf-8") as f:
            string = '[{"x": 0, "y": 0, "id": 1, "height": 4, "width": 2}]'
            self.assertEqual(f.read(), string)
        a.__del__()
        rectangles = [Rectangle(1, 2, 3, 4),
                      Rectangle(5, 6, 7, 8),
                      Rectangle(9, 10, 11, 12),
                      Rectangle(13, 14, 15, 16),
                      Rectangle(17, 18, 19, 20)]
        Rectangle.save_to_file(rectangles)

        # with open("Rectangle.json", "r") as file:
        #     self.assertEqual(file.read(),
        #                      "[{\"id\": 1, \"width\": 1, \"height\": 2, "
        #                      "\"x\": 3, \"y\": 4}, "
        #                      "{\"id\": 2, \"width\": 5, \"height\": 6, "
        #                      "\"x\": 7, \"y\": 8}, "
        #                      "{\"id\": 3, \"width\": 9, \"height\": 10, "
        #                      "\"x\": 11, \"y\": 12}, "
        #                      "{\"id\": 4, \"width\": 13, \"height\": 14, "
        #                      "\"x\": 15, \"y\": 16}, "
        #                      "{\"id\": 5, \"width\": 17, \"height\": 18, "
        #                      "\"x\": 19, \"y\": 20}]")
        for rectangle in rectangles:
            rectangle.__del__()
        squares = [Square(1, 3, 4),
                   Square(5, 7, 8),
                   Square(9, 11, 12),
                   Square(13, 15, 16),
                   Square(17, 19, 20)]
        Square.save_to_file(squares)

        # with open("Square.json", "r") as file:
        #     self.assertEqual(file.read(),
        #                      "[{\"id\": 1, \"size\": 1, "
        #                      "\"x\": 3, \"y\": 4}, "
        #                      "{\"id\": 2, \"size\": 5, "
        #                      "\"x\": 7, \"y\": 8}, "
        #                      "{\"id\": 3, \"size\": 9, "
        #                      "\"x\": 11, \"y\": 12}, "
        #                      "{\"id\": 4, \"size\": 13, "
        #                      "\"x\": 15, \"y\": 16}, "
        #                      "{\"id\": 5, \"size\": 17, "
        #                      "\"x\": 19, \"y\": 20}]")
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
