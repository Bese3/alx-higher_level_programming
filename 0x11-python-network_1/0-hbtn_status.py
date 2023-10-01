#!/usr/bin/python3
import urllib.request

"""
 The `if __name__ == '__main__':` block is a common idiom
 in Python that allows a script to be executed as a standalone
 program or imported as a module.
"""
if __name__ == '__main__':
    """
    requesting for alx status
    """
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        print("Body response:")
        print(f"\t- type: {type(response.read())}")
        print(f"\t- content: {response.read()}")
        print(f"\t- utf8 content: {str(response.read())[2:-1]}")
