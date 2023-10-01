#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
import requests


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")


if __name__ == '__main__':
    main()
