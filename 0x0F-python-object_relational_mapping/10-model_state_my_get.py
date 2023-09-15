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
    risk_chars = ["\x00", "\n", "\r", "\\",
                  "'", '\"', "\0", "\'"
                  "\"", "\b", "\n", "\t"
                  "\r", "Z", "\\", "%"
                  "_", "*"]
    for i in risk_chars:
        if i in argv[4]:
            print("bad input")
            return
    Session = session()
    states = Session.query(State).filter(State.name
                                         == argv[4]).order_by('id').all()
    if states:
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")
    Session.close()


if __name__ == '__main__':
    main()
