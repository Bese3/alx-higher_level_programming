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

    selector = "SELECT cities.id, cities.name, states.name FROM\
         states INNER JOIN\
         cities ON states.id = cities.state_id\
         ORDER BY cities.id"
    cursor.execute(selector)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
