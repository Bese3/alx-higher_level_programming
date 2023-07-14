#!/usr/bin/python3
"""importing everything"""
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """this class is designed for the test of rectangle module"""

    def test_id(self):
        """
        The function tests the id attribute
        of the Rectangle class.
        """
        r = Rectangle(10, 2)
        self.assertEqual(1, r.id)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        del r
        del r2
        del r3

    def test_getter(self):
        """
        The function tests the getter methods
        of the Rectangle class.
        """
        r2 = Rectangle(10, 2, 2, 1, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)
        del r2

    def test_setter(self):
        """
        The function tests the setter methods of the Rectangle
        class by setting the width and height
        """
        r5 = Rectangle(5, 5)
        r5.width = 10
        self.assertEqual(r5.width, 10)
        r5.height = 10
        self.assertEqual(r5.height, 10)
        del r5

    def test_validators(self):
        """
        The function `test_validators` tests the validators
        in the `Rectangle` class to ensure that the
        attributes are of the correct type and value.
        """
        with self.assertRaises(TypeError) as err:
            Rectangle("1", 2, 3, 4, 5)
        self.assertTrue("width must be an integer" in str(err.exception))
        with self.assertRaises(TypeError)as err:
            Rectangle(1, "2", 3, 4, 5)
        self.assertTrue("height must be an integer" in str(err.exception))
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, "3", 4, 5)
            self.assertTrue("x must be an integer" in str(err.exception))
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, 3, "4", 5)
            self.assertTrue("y must be an integer" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(-1, 2, 3, 4, 5)
            self.assertTrue("width must be > 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(1, -2, 3, 4, 5)
            self.assertTrue("height must be > 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 2, -3, 4, 5)
            self.assertTrue("x must be >= 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 2, 3, -4, 5)
            self.assertTrue("y must be >= 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(-1, "2", 3, 4, 5)
            self.assertTrue("width must be > 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 0, 3, 4, 5)
            self.assertTrue("width must be > 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 0, 3, 4, 5)
            self.assertTrue("height must be > 0" in str(err.exception))
        with self.assertRaises(TypeError) as err:
            Rectangle(1, "2", "3", 4, 5)
            self.assertTrue("height must be > 0" in str(err.exception))
        # using setters
        r6 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError)as err:
            r6.width = "2"
        self.assertTrue("width must be an integer" in str(err.exception))
        with self.assertRaises(TypeError) as err:
            r6.height = "2"
        self.assertTrue("height must be an integer" in str(err.exception))
        with self.assertRaises(TypeError) as err:
            r6.x = "2"
        self.assertTrue("x must be an integer" in str(err.exception))
        with self.assertRaises(TypeError) as err:
            r6.y = "2"
        self.assertTrue("y must be an integer" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            r6.width = 0
        self.assertTrue("width must be > 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            r6.height = 0
        self.assertTrue("height must be > 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            r6.x = -1
        self.assertTrue("x must be >= 0" in str(err.exception))
        with self.assertRaises(ValueError) as err:
            r6.y = -1
        self.assertTrue("y must be >= 0" in str(err.exception))
        del r6
