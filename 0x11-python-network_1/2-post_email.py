#!/usr/bin/python3
"""
block is a common idiom in Python that allows
a script to be executed as a standalone
program or imported as a module.
"""
from urllib import parse, request
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
    email = argv[2]
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    print((req.get_full_url()))
    with request.urlopen(req) as response:
        print(parse.urldecode(response.read()))


if __name__ == '__main__':
    main()
