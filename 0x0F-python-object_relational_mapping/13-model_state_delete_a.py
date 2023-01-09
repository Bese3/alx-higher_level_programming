#!/usr/bin/python3
"""Module 13-model_state_delete_a.py
Deletes all rows in table states which contain 'a' in their names."""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Load the 'states' table using SQLAlchemy. Then, find all rows in
    the table which contain 'a' in their names. If any is found, it
    is deleted."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like("%a%")).all()

    #  Delete all states_with_a objects
    for state in states_with_a:
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
