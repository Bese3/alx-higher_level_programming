#!/usr/bin/python3
"""
    A script that lists all State objects from the database hbtn_0e_6_usa
    Username, password and dbname wil be passed as arguments to the script.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
    The main function connects to a MySQL database,
    creates tables if they don't exist, retrieves and
    prints all states from the database, and then closes the session.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()
    states = Session.query(State).order_by('id').first()
    # for state in states:
    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")
    Session.close()


if __name__ == '__main__':
    main()
