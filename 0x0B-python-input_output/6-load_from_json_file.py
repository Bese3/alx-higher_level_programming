#!/usr/bin/python3
"""
from json file object to python string
"""
import json


def load_from_json_file(filename):
    """
    Arg:
      filename: file to take json string from
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
