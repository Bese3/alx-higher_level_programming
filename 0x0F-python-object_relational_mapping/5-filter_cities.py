#!/usr/bin/python3
"""
Module 5-filter_cities
Takes 4 arguments: username, password and database name to connect to the mysql
serve running on localhost port 3306, and the name of
the state to list which cities it has.
"""

from sys import argv
import MySQLdb


def main():
    """
    Program starts here. Lists cities that are in
    the state passed as the 4th argument,
    from the database hbtn_0e_0_usa
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
        "SELECT cities.id, cities.name FROM cities INNER JOIN " +
        "states WHERE cities.state_id = states.id AND " +
        "states.name='" + state_name + "' ORDER BY cities.id")

    cities = c.fetchall()

    for i in cities:
        print(i[1], end="")
        if cities.index(i) != len(cities) - 1:
            print(", ", end="")
        else:
            print()
    # Print a new line if cities is empty
    if not len(cities):
        print()


if __name__ == "__main__":
    main()
