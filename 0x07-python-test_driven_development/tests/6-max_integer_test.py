"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains tests for the function max_integer in the module
    6-max_integer
    """

    def test_None(self):
        """
        Test for empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_positive(self):
        """
        Test for positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertNotEqual(max_integer([1, 2, 3]), 2)
        self.assertNotEqual(max_integer([1, 2, 3]), 1)
        self.assertEqual(max_integer([1, 2, 3, 4, 56, 8, 0]), 56)

    def test_negative(self):
        """
        Test for negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, 0]), 0)
        self.assertNotEqual(max_integer([-1, -2, -3, -4, 0]), -1)
        self.assertNotEqual(max_integer([-1, -2, -3, -4, 0]), -2)
        self.assertNotEqual(max_integer([-1, -2, -3, -4, 0]), -3)
        self.assertNotEqual(max_integer([-1, -2, -3, -4, 0]), -4)

        self.assertEqual(max_integer([-1, -20, -30, -40, 2]), 2)

    def test_duplicate(self):
        """
        Test for duplicate numbers
        """
        self.assertEqual(max_integer([0, 0, 0, 0, 0, 0, 0, 0]), 0)
        self.assertNotEqual(max_integer([0, 0, 0, 0, 0, 0, 0, 0]), 8)

        self.assertEqual(max_integer([0, 0, 1, 1, 2, 2, -2, -2, -3, -3, -4,
                                      -4, -4, -4, -4, -4, -4, -4, -4, -4,
                                      -4, -4, 0]), 2)
