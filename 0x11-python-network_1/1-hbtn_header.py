#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
import urllib.request
import sys


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    if sys.argv[1] is None:
        return
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
