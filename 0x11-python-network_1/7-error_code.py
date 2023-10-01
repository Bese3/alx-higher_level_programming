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
    url = sys.argv[1]
    r = requests.post(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
        return
    body = r.text
    print(body)


if __name__ == '__main__':
    main()
