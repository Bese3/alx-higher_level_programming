#!/usr/bin/python3

"""7-add_item
Write a script that adds all arguments to a Python list, and then save them
to a file"""


def main():
    """Program starts here"""
    filename = "add_item.json"
    argv = __import__("sys").argv
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:

        py_objs = load_from_json_file(filename)

        for i in range(len(argv)):
            if i == 0:
                continue
            py_objs.append(argv[i])

        save_to_json_file(py_objs, filename)
    except FileNotFoundError:
        with open(filename, "w") as f:
            f.write("[]")
            return


if __name__ == "__main__":
    main()
