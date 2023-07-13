#!/usr/bin/python3
import unittest
from models.base import Base

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
