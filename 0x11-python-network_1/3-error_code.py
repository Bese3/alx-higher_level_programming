#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
from urllib import error, request
from sys import argv


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    try:
        if argv[1] is None:
            return
    except IndexError:
        return
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            read = response.read()
            print(read)
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)


if __name__ == '__main__':
    main()
