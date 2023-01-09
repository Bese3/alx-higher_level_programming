#!/usr/bin/python3
"""Module 101-relationship_states_cities_list.py
Lists all State objects, and corresponding City objects from the
database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def main():
    """Program starts here.
    All tables from hbtn_0e_100_usa are loaded by SQLAlchemy. By querying,
    the all State objects are fetched. The City objects under each State is
    also fetched with the help of relationship() set up in State. Each
    State object and all of the cities under it are printed.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State)

    for state in all_states:
        print(str(state.id) + ": " + state.name)
        for city in state.cities:
            print("\t" + str(city.id) + ": " + city.name)

    session.close()


if __name__ == '__main__':
    main()
