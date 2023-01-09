#!/usr/bin/python3
"""Module 14-model_city_fetch_by_state
Prints all City objects from the database hbtn_03_14_usa that's
passed as an argument"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Program starts here.
    Loads the database hbtn_0e_14_usa and loads all the City rows
    in the table cities. Then each City is printed, with its state's name.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(City).order_by('id').all()

    for city in all_cities:
        city_state = session.query(State).get(city.state_id)
        print("{}: ({}) {}".format(city_state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    main()
