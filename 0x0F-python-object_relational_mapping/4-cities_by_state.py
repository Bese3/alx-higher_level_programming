#!/usr/bin/python3
"""
Module 4-cities_by_state
Takes 3 arguments: username, password and database name to connect to the mysql
server running on localhost port 3306"""

from sys import argv
import MySQLdb


def main():
    """
    Program starts here. Lists cities with their matching states from
    the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name," +
              "states.name FROM cities INNER JOIN states " +
              "WHERE cities.state_id = states.id ORDER BY cities.id;")
    for i in c.fetchall():
        print(i)


if __name__ == "__main__":
    main()
