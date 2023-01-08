#!/usr/bin/python3
'''
Module 0-hbtn_status
Fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    url = 'https://alx-intranet.hbtn.io/status'
    if len(__import__('sys').argv) != 1:
        url = __import__('sys').argv[1]

    with urllib.request.\
            urlopen(url) as response:
        response_read = response.read()
        print("Body response:")
        print("\t- type:", type(response_read))
        print("\t- content:", response_read)
        print("\t- utf8 content:", str(response_read)[2:-1])


if __name__ == '__main__':
    main()
