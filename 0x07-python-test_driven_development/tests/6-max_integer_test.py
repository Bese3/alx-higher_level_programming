#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
   The TestMaxInteger class contains multiple
   test methods that test the functionality of the
   max_integer function with different types of input lists.
"""


class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        """
        The function `test_none` tests if the
        `max_integer` function returns `None` when an empty list
        is passed as an argument.
        """
        self.assertEqual(max_integer([]), None)

    def test_pos(self):
        """
        The test_pos function tests the
        max_integer function by asserting
        that it returns the correct
        maximum value for different input lists.
        """
        self.assertEqual(max_integer([2, 5, 7]), 7)
        self.assertNotEqual(max_integer([5, 6, 7]), 5)
        self.assertEqual(max_integer([12, 34, 56, 1000, 200, 50]), 1000)

    def test_neg(self):
        """
        The function `test_neg` tests the `max_integer`
        function with negative numbers and checks if the
        maximum value returned is correct.
        """
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertNotEqual(max_integer([-4, -3, -2, -1]), -4)
        self.assertEqual(max_integer([-78, -65, -54, -43]), -43)

    def test_duplicate(self):
        """
        The function `test_duplicate` tests the `max_integer`
        function by asserting that it returns the
        correct maximum value for lists with duplicate elements.
        """
        self.assertEqual(max_integer([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([9, 9, 9, 9, 9, 9]), 9)
