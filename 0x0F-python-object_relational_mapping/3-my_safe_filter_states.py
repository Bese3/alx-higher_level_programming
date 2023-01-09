#!/usr/bin/python3
"""
Module 3-my_safe_filter_states
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

    #  Stop program if SQL injection risky characters are
    #  in the state name argument
    state_name = argv[4]
    escape_strings = ["\x00", "\n", "\r", "\\", "'", '\"', r"\xla"]
    for i in escape_strings:
        if i in state_name:
            return

    c.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id".format(argv[4]))
    for i in c.fetchall():
        print(i)


if __name__ == "__main__":
    main()
