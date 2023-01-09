#!/usr/bin/python3
"""Module 8-model_state_fetch_first
Fetches the first row in the states table
of the database passed as argument
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Using SQLAlchemy, the 'states' table is loaded and
    the first entry in the table is printed. If there's no row,
    'Nothing' is printed"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()

    if first_state:
        print(str(first_state.id) + ": " + first_state.name)
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
