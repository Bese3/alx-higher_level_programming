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

    try:
        for i in risk_chars:
            if i in argv[4]:
                # print("bad input")
                return
    except IndexError:
        pass

    cursor = db.cursor()

    selector = "SELECT cities.name FROM\
        cities INNER JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name LIKE BINARY '{}'\
        ORDER BY cities.id ASC".format(argv[4])
    cursor.execute(selector)

    data = cursor.fetchall()
    my_str = ""
    for i in range(len(data)):
        my_str += str(data[i][0]) + (", " if i != len(data) - 1 else "")
    print(my_str)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
