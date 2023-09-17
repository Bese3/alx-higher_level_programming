#!/usr/bin/python3
"""Module model_state
Defines a State class that will be written to a database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class State(Base):
    """Class State
    Inherits from class Base to define what the table State
    looks like in a database.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
