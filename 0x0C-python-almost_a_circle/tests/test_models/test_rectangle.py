#!/usr/bin/python3
"""importing everything"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
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
        r.__del__()
        r2.__del__()
        r3.__del__()

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
        r2.__del__()

    def test_setter(self):
        """
        The function tests the setter methods of the Rectangle
        class by setting the width and height
        """
        r5 = Rectangle(5, 5, id=12)
        r5.width = 10
        self.assertEqual(r5.width, 10)
        r5.height = 10
        self.assertEqual(r5.height, 10)
        r5.__del__()

    def test_validators(self):
        """
        The function `test_validators` tests the validators
        in the `Rectangle` class to ensure that the
        attributes are of the correct type and value.
        """
        with self.assertRaises(TypeError) as err:
            Rectangle("1", 2, 3, 4, 5)
        self.assertTrue("width must be an integer" in str(err.exception))
        with self.assertRaises(TypeError) as err:
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
        r6.__del__()

    def test_area(self):
        """
        The function tests the area calculation of a rectangle
        object with different dimensions and positions.
        """
        r7 = Rectangle(10, 10, id=12)
        self.assertEqual(r7.area(), 100)
        r7.width = 12
        r7.height = 12
        self.assertEqual(144, r7.area())
        r7.x = 20
        r7.y = 20
        self.assertEqual(144, r7.area())
        r7.__del__()

    def test_display(self):
        """
        The test_display function tests the display method
        of the Rectangle class by creating different
        instances of Rectangle and checking if the display
        output matches the expected output.
        """
        r1 = Rectangle(2, 2)
        r1_dis = r1.display()
        self.assertEqual(r1_dis, "##" + "\n" + "##" + "\n")
        r1 = Rectangle(2, 2, 1, 2)
        r1_dis = r1.display()
        self.assertEqual(r1_dis, "\n\n ##\n ##\n")
        r1.width = 4
        r1.height = 3
        r1_dis = r1.display()
        self.assertEqual(r1_dis, "\n\n ####\n ####\n ####\n")
        r1.__del__()

    def test_str(self):
        """
        The function tests the __str__ method of
        the Rectangle class and checks if the output matches
        the expected string representation of the rectangle object.
        """
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 3/4 - 1/2")
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.__str__(), "[Rectangle] (2) 0/0 - 1/2")
        r3 = Rectangle(6, 8, 1, 2, 10)
        self.assertEqual("[Rectangle] (10) 1/2 - 6/8", r3.__str__())
        r1.__del__()
        r2.__del__()
        r3.__del__()

    def test_update(self):
        """
        The function `test_update` tests the `update` method
        of the `Rectangle` class by checking the
        behavior when passing arguments as both `*args` and `**kwargs`.
        """
        # checking *args
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        # checking **kwargs
        r1.__del__()
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(id=89, width=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(id=89, width=2, height=3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(id=89, width=2, height=3, x=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.__del__()
        # checking both
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(12, width=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 10/10 - 10/10")
        r1.update(12, width=2, height=3)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 10/10 - 10/10")
        r1.__del__()

    def test_to_dictionary(self):
        """
        The function tests the `to_dictionary` method of the
        `Rectangle` class by creating instances of `Rectangle`
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        first = {'x': r1.x, 'y': r1.y, 'id': r1.id}
        second = {'height': r1.height, 'width': r1.width}
        first.update(second)
        self.assertEqual(r1.to_dictionary(), eval(str(first)))
        r1 = Rectangle(1, 2, 3, 4)
        first = {'x': r1.x, 'y': r1.y, 'id': r1.id}
        second = {'height': r1.height, 'width': r1.width}
        first.update(second)
        self.assertEqual(r1.to_dictionary(), eval(str(first)))


if __name__ == '__main__':
    unittest.main()
