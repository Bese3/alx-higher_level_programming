#!/usr/bin/python3
"""
Module 1-filter_states
Takes 3 arguments: username, password and database name to connect to the mysql
serve running on localhost port 3306.
"""

from sys import argv
import MySQLdb


def main():
    """
    Program starts here. Lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE  name LIKE BINARY 'N%' ORDER BY id")
    for i in c.fetchall():
        print(i)


if __name__ == "__main__":
    main()
