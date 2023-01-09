#!/usr/bin/python3
"""Module 9-model_state_filter_a
Lists objects from database by filtering their names
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Using SQLAlchemy, the 'states' table is loaded and
    all the rows that contain letter 'a' in their
    column name are printed. If there's no row,
    nothing is printed"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_with_a:
        print(str(state.id) + ": " + state.name)
    session.close()


if __name__ == "__main__":
    main()
