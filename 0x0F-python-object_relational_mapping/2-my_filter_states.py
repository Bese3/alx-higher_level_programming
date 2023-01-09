#!/usr/bin/python3
"""
Module 2-my_filter_states
Takes 4 arguments: username, password and database name to connect to the mysql
serve running on localhost port 3306, and the name of
the state being looked for.
"""

from sys import argv
import MySQLdb


def main():
    """
    Program starts here. Lists states with matching name passed as
    the 4th argument from the database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute(
        "SELECT * FROM states WHERE name " +
        "LIKE BINARY '{}' ORDER BY id".format(argv[4]))
    for i in c.fetchall():
        print(i)


if __name__ == "__main__":
    main()
