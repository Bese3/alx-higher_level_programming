#!/usr/bin/python3
"""
Takes 3 arguments: username, password and database name to connect to the mysql
serve running on localhost port 330
"""
import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)
    risk_chars = ["\x00", "\n", "\r", "\\",
                  "'", '\"', "\0", "\'"
                  "\"", "\b", "\n", "\t"
                  "\r", "Z", "\\", "%"
                  "_", "*"]
    for i in risk_chars:
        if i in argv[4]:
            # print("bad input")
            return

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE\
                  name LIKE BINARY '{}' ORDER BY id ASC".format(argv[4]))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
