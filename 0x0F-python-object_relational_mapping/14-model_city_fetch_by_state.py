#!/usr/bin/python3
"""
    A script that lists all State objects from the database hbtn_0e_6_usa
    Username, password and dbname wil be passed as arguments to the script.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    try:
        for i in risk_chars:
            if i in argv[4]:
                # print("bad input")
                return
    except IndexError:
        pass

    Session = session()
    my_states = Session.query(State.name, City).filter(State.id ==
                                                       City.state_id).all()
    # print(states.City.name for states in my_states)
    for i in my_states:
        print(f"{i.name}: ({i.City.id}) {i.City.name}")
    Session.commit()


if __name__ == '__main__':
    main()
