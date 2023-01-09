#!/usr/bin/python3
"""Module 11-model_state_insert
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
(database name is passed as argument)"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Using SQLAlchemy, the 'states' table is loaded. A new State object
    is created with name "Louisiana" and it's added to the states table."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="Louisiana"))
    session.commit()
    print(session.query(State).filter(State.name == "Louisiana").all()[-1].id)

    session.close()


if __name__ == "__main__":
    main()
