#!/usr/bin/python3
"""Module 10-model_state_my_get_state
Prints the id of the name of the state passed as argument,
searched for in the table states
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Using SQLAlchemy, the 'states' table is loaded and the 4th argument
    passed, the name, is looked for in the database. If a matching name
    is found, the id of that State is printed. If not, "Not found" is printed.

    If an SQL Injection is detected, program exits."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    #  Stop program if SQL injection risky characters are
    #  in the state name argument
    state_name = argv[4]
    escape_strings = ["\x00", "\n", "\r", "\\", "'", '\"', r"\xla"]
    for i in escape_strings:
        if i in state_name:
            exit()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_found = session.query(State).filter(State.name == argv[4]).all()

    print(states_found[0].id) if len(states_found) else print("Not found")
    session.close()


if __name__ == "__main__":
    main()
