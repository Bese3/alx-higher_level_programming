#!/usr/bin/python3
from test_base import TestBase
from test_rectangle import TestRectangle

test_obj_base = TestBase()
test_obj_rect = TestRectangle()

test_obj_base.test_id()
test_obj_base.test_getter()
test_obj_base.test_setter()

# test_obj_rect.test_getters_setters()
# test_obj_rect.test_import_works_correctly()
# test_obj_rect.test_invalid_initialization_and_setting_values()
# test_obj_rect.test_rectangle_area()
