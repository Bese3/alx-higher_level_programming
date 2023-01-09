#!/usr/bin/python3
"""Module 7-model_state_fetch_all
Uses sqlalchemy to fetch all rows and
generate objects from them from the table 'state'
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Program starts here. Using SQLAlchemy, connection to the
    database is established and all rows in the table 'states'
    are fetched and displayed.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by('id').all()

    for state in all_states:
        print(str(state.id) + ": " + state.name)
    session.close()


if __name__ == '__main__':
    main()
