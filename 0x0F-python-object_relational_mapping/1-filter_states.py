#!/usr/bin/python3
"""
Takes 3 arguments: username, password and database name to connect to the mysql
serve running on localhost port 330
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name\
                    LIKE BINARY 'N%' ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
