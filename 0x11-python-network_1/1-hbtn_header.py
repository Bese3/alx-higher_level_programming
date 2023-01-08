#!/usr/bin/python3
'''Module 1-hbtn_header
Requests a URL and displays value of X-request-Id'''
import urllib.request
from sys import argv


def main():
    '''Program starts here. takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the
    header of the response.'''
    url = argv[1]
    value = 'X-Request-Id'

    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
