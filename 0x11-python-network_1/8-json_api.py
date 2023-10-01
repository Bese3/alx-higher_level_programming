#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
import requests
import sys


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    q = sys.argv[1] if len(sys.argv) >= 2 else ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={'q': q})
    try:
        json_data = r.json()
        if json_data == {}:
            print("No result")
            return
        print(f"[{json_data['id']}] {json_data['name']}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
