#!/usr/bin/python3
from test_base import BaseTest
from test_rectangle import RectangleTest

test_obj_base = BaseTest()
test_obj_rect = RectangleTest()

test_obj_base.test_1_None_id()
test_obj_base.test_2_passed_id()
test_obj_base.test_3_None_and_passed_mix()

test_obj_rect.test_getters_setters()
test_obj_rect.test_import_works_correctly()
test_obj_rect.test_invalid_initialization_and_setting_values()
test_obj_rect.test_rectangle_area()
