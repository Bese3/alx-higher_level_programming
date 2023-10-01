#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
import urllib.request


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url)\
         as response:
        read = response.read()
        print("Body response:")
        print("\t- type:", type(ead))
        print("\t- content:", read)
        print("\t- utf8 content:", str(read)[2:-1])


if __name__ == '__main__':
    main()
