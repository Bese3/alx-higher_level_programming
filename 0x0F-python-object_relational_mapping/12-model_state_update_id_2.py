#!/usr/bin/python3
"""Module 12-model_state_update_id_2
Changes the name of a state with id equal to 2, to 'New Mexico'
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Loads a State object with id equal to 2, updates its name to 'New Mexico'
    and saves it to the database. If the state couldn't be found, the program
    exits."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).get(2)
    #  Update object (row) only if it exists
    if state:
        state.name = 'New Mexico'
        session.commit()

    session.close()


if __name__ == "__main__":
    main()
