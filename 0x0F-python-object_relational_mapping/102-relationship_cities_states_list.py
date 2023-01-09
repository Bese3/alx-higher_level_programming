#!/usr/bin/python3
"""Module 102-relationship_states_cities_list.py
Lists all City objects, and corresponding State object from the
database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def main():
    """Program starts here.
    All tables from hbtn_0e_100_usa are loaded by SQLAlchemy. By querying,
    the all City objects are fetched. Each City is printed and
    with the help of the relationship established in State, each
    City's State is printed as well.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(City)

    for city in all_cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()


if __name__ == '__main__':
    main()
