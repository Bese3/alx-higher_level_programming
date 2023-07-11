#!/usr/bin/python3
"""
method to save json file  from python script
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Arg:
      my_obj: obj to JSON
      filename: name of the file to save to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f, sort_keys=False)
