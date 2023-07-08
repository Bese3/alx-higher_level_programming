#!/usr/bin/python3
import traceback
import sys


def safe_function(fct, *args):
    try:
        result = fct(args)
        return result
    except Exception as e:
        sys.stderr.write('Exception: '.join(e.__str__())
