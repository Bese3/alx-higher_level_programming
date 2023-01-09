#!/usr/bin/python3
"""
This unittest module test_rectangle tests the class Rectangle in
models/rectangle
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """This class has a battery of functions that test every functionality of
    the class Rectangle in module models/rectangle"""

    def test_import_works_correctly(self):
        """Checks if id is set correctly when many objects are instantiated
        from Rectangle (which inherits from Base)"""
        r1 = Rectangle(10, 12)
        self.assertEqual(1, r1.id)
        r2 = Rectangle(8, 9, 2, 3)
        self.assertEqual(2, r2.id)
        r3 = Rectangle(1, 7, 4, 9)
        self.assertEqual(3, r3.id)
        r4 = Rectangle(1, 7, 4, 9, 12)
        self.assertEqual(12, r4.id)
        r5 = Rectangle(1, 7, 4, 9, 897)
        self.assertEqual(897, r5.id)
        r6 = Rectangle(1, 7, 4, 9)
        self.assertEqual(4, r6.id)
        r1.__del__()
        r2.__del__()
        r3.__del__()
        r4.__del__()
        r5.__del__()
        r6.__del__()

    def test_getters_setters(self):
        """Checks if getters and setters work as intended"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r1.x)
        self.assertEqual(4, r1.y)

        r1.width = 20
        self.assertEqual(20, r1.width)
        r1.height = 60
        self.assertEqual(60, r1.height)
        r1.x = 7
        self.assertEqual(7, r1.x)
        r1.y = 8
        self.assertEqual(8, r1.y)
        r1.__del__()

    def test_invalid_initialization_and_setting_values(self):
        """Tests if every exception is correctly raised for each attribute
        in Rectangle
        """

        #  Checks for object initialization

        with self.assertRaises(TypeError) as context:
            Rectangle("w", 1, 2, 3)
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle("1", "1", 2, 3)
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle("1", "1", 2, 3)
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(-2, "1", 2, 3)
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(0, 0, 2, 3)
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "1", 2, 3)
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "1", "2", 3)
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "1", 2, 3)
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(2, -1, 2, 3)
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0, 2, 3)
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(2, 0, 2, 3)
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 1, "2", 3)
        self.assertTrue("x must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 1, -1, 3)
        self.assertTrue("x must be >= 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 1, 2, "3")
        self.assertTrue("y must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 1, 1, -3)
        self.assertTrue("y must be >= 0" in str(context.exception))

        #  Checks for using object's setters
        r = Rectangle(1, 2, 3, 4)

        with self.assertRaises(TypeError) as context:
            r.width = "w"
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.width = 0
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.width = -1
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            r.height = "w"
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.height = 0
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.height = -6
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            r.x = "w"
        self.assertTrue("x must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.x = -6
        self.assertTrue("x must be >= 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            r.y = "w"
        self.assertTrue("y must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.y = -6
        self.assertTrue("y must be >= 0" in str(context.exception))

        r.__del__()

    def test_rectangle_area(self):
        """Tests if the area of a Rectangle is correct"""
        r = Rectangle(2, 4, 1, 2)
        self.assertEqual(8, r.area())
        r.width = 8
        r.height = 10
        self.assertEqual(80, r.area())
        r.width = 10
        self.assertEqual(100, r.area())
        r.x = 8
        r.y = 9
        self.assertEqual(100, r.area())
        r.width = 7
        r.height = 8
        self.assertEqual(56, r.area())
        r.__del__()

    def test_display_rectangle(self):
        """Tests Rectangle is printed to the screen correctly"""
        r = Rectangle(1, 2, 1, 1)
        self.assertEqual(r.display(), "\n #\n #")
        r.width = 5
        r.height = 4
        self.assertEqual(r.display(), "\n #####\n #####\n #####\n #####")
        r.x = 4
        r.y = 3
        r.width = 3
        r.height = 3
        self.assertEqual(r.display(), "\n\n\n    ###\n    ###\n    ###")
        r.x = 0
        r.y = 0
        self.assertEqual(r.display(), "###\n###\n###")
        r.__del__()

    def test_str_representation(self):
        """Tests if __str__ returns the correct string representation for
        the Rectangle class"""
        r1 = Rectangle(2, 3, 1, 2)
        self.assertEqual("[Rectangle] (1) 1/2 - 2/3", r1.__str__())
        r2 = Rectangle(6, 8, 2)
        self.assertEqual("[Rectangle] (2) 2/0 - 6/8", r2.__str__())
        r3 = Rectangle(6, 8, 2, 1, 189)
        self.assertEqual("[Rectangle] (189) 2/1 - 6/8", r3.__str__())
        r1.__del__()
        r2.__del__()
        r3.__del__()
        r4 = Rectangle(6, 8, 2, 1)
        self.assertEqual("[Rectangle] (1) 2/1 - 6/8", r4.__str__())
        r5 = Rectangle(6, 8)
        self.assertEqual("[Rectangle] (2) 0/0 - 6/8", r5.__str__())
        r6 = Rectangle(6, 8, 1, 2, 10)
        self.assertEqual("[Rectangle] (10) 1/2 - 6/8", r6.__str__())
        r7 = Rectangle(6, 8, 2, 3)
        self.assertEqual("[Rectangle] (3) 2/3 - 6/8", r7.__str__())
        r4.__del__()
        r5.__del__()
        r6.__del__()
        r7.__del__()

    def test_update(self):
        """Tests if updating the attributes of Rectangle using update()
        works as intended"""
        r = Rectangle(1, 2, 3, 4)

        #  Using *args only
        r.update()
        r.update(2)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 3/4 - 1/2")
        r.update(3, 3)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 3/4 - 3/2")
        r.update(4, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (4) 3/4 - 3/4")
        r.update(5, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 5/4 - 3/4")
        r.update(6, 3, 4, 5, 6)
        self.assertEqual(r.__str__(), "[Rectangle] (6) 5/6 - 3/4")

        # Using **kwargs, and mixing it with *args
        r.update(x=12, y=24)
        self.assertEqual(r.__str__(), "[Rectangle] (6) 12/24 - 3/4")
        r.update(width=21, height=4)
        self.assertEqual(r.__str__(), "[Rectangle] (6) 12/24 - 21/4")
        r.update(id=8)
        self.assertEqual(r.__str__(), "[Rectangle] (8) 12/24 - 21/4")
        r.update(1, 2, 3, x=0, y=0)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 12/24 - 2/3")
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (1) 12/24 - 2/3")
        r.update(xml=12, ydasf=31)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 12/24 - 2/3")
        r.__del__()

    def test_to_dictionary(self):
        """Tests the to_dictionary method of Rectangle.
        It should let a new Rectangle instance be created from the output"""
        r = Rectangle(2, 4, 1, 1)
        self.assertEqual(r.to_dictionary(), {"id": 1, "width": 2,
                                             "height": 4, "x": 1, "y": 1})

        r1 = Rectangle(1, 1)
        r1.update(**r.to_dictionary())
        self.assertEqual(r1.to_dictionary(), {"id": 1, "width": 2,
                                              "height": 4, "x": 1, "y": 1})
        self.assertEqual(r.__str__(), r1.__str__())
        r.update(10, 20)
        self.assertNotEqual(r.to_dictionary(), r1.to_dictionary())


if __name__ == '__main__':
    unittest.main()
