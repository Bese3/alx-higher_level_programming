#!/usr/bin/python3
"""Module 100-relationship_states_cities
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def main():
    """Program starts here.
    Loads the database hbtn_0e_14_usa and loads all the City rows
    in the table cities. Then each City is printed, with its state's name.
    If a State gets deleted, all Cities under it get deleted as well since
    there is a cascading deleteion relationship in State.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_california = State(name="California")
    session.add(state_california)
    session.commit()

    san_francisco = City(name="San Francisco", state=state_california)
    session.add(san_francisco)
    session.commit()


if __name__ == '__main__':
    main()
