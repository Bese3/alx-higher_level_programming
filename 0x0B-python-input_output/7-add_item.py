#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    """
    Main code to run in the terminal
    """
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    new = []
    try:
        new = load_from_json_file("add_item.json")
        new.extend(sys.argv[1:])
        save_to_json_file(new, "add_item.json")
    except FileNotFoundError:
        with open("add_item.json", mode="w") as f:
            f.write("[]")
            if len(sys.argv) != 1:
                f.seek(1)
                save_to_json_file(sys.argv[1:], "add_item.json")
