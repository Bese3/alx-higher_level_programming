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
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url)
    json_data = r.json()
    for i, j in zip(json_data, range(10)):
        print(f"{i['sha']}: {i['commit']['author']['name']}")


if __name__ == '__main__':
    main()
