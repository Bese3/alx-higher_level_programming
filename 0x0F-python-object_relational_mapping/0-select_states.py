#!/usr/bin/python3
"""
Takes 3 arguments: username, password and database name to connect to the mysql
serve running on localhost port 330
"""
import MySQLdb
from sys import argv


def main():
    """
    main program starts here
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * FROM state ORDER BY id")
        for i in cursor.fetchall():
            print(i)
    except IndexError:
        pass


if __name__ == '__main__':
    main()
