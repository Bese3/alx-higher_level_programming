#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    json_data = r.json()
    try:
        if json_data['message']:
            print(None)
            return
    except KeyError:
        print(json_data['id'])


if __name__ == '__main__':
    main()
