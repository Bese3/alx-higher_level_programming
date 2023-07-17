#!/usr/bin/python3
"""square module test cases"""
from models.square import Square
import json
import unittest


class TestSquare(unittest.TestCase):
    """TestSquare is module for testing the square script"""
    def test_init(self):
        """
        The function tests the initialization and
        string representation of a Square object.
        """
        s = Square(3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        s.update(4, 8, 1, 2)
        self.assertEqual("[Square] (4) 1/2 - 8", s.__str__())
        s.__del__()

    def test_getter_setter(self):
        """
        The function `test_getter_setter` tests the getter
        and setter methods of the `Square` class.
        """
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError) as context:
            s.size = "w"
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.size = 0
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.size = -1
        self.assertTrue("width must be > 0" in str(context.exception))
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_update(self):
        """
        The `test_update` function tests the `update`
        method of the `Square` class by checking the
        behavior when passing arguments and keyword arguments.
        """
        # checking *args
        s = Square(8)
        s.update(12)
        self.assertEqual("[Square] (12) 0/0 - 8", s.__str__())
        s.update(7, 18, 2, 4, 5, 6, 7, 8, 9)
        self.assertEqual("[Square] (7) 2/4 - 18", s.__str__())
        s.update(7, 8)
        self.assertEqual("[Square] (7) 2/4 - 8", s.__str__())
        s.update(7, 8, 3)
        self.assertEqual("[Square] (7) 3/4 - 8", s.__str__())
        # checking **kwargs
        s.update(id=10)
        self.assertEqual("[Square] (10) 3/4 - 8", s.__str__())
        s.update(x=10)
        self.assertEqual("[Square] (10) 10/4 - 8", s.__str__())
        s.update(y=10)
        self.assertEqual("[Square] (10) 10/10 - 8", s.__str__())
        s.update(size=20)
        self.assertEqual("[Square] (10) 10/10 - 20", s.__str__())
        # checking both
        s.update(7, size=5)
        self.assertEqual("[Square] (7) 10/10 - 20", s.__str__())
        with self.assertRaises(ValueError) as context:
            s.update(x=9, y=-1)
        self.assertTrue("y must be >= 0" in str(context.exception))

    def test_to_dictionary(self):
        """
        The function `test_to_dictionary` tests the
        `to_dictionary` method of the `Square` class.
        """
        r = Square(2, 1, 1)
        self.assertEqual(r.to_dictionary(), {"id": 1, "size": 2, "x": 1,
                                             "y": 1})

        r1 = Square(1, 1)
        r1.update(**r.to_dictionary())
        self.assertEqual(r1.to_dictionary(), {"id": 1, "size": 2, "x": 1,
                                              "y": 1})

    def test_str(self):
        """
        The function tests the __str__ method of
        the Square class and checks if the output matches
        the expected string representation of the square object.
        """
        r1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Square] (4) 2/3 - 1")
        r2 = Square(1, 2)
        self.assertEqual(r2.__str__(), "[Square] (1) 2/0 - 1")
        r1.__del__()
        r2.__del__()


if __name__ == '__main__':
    unittest.main()
