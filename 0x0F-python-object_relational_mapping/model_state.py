#!/usr/bin/python3
"""Module model_state
Defines a State class that will be written to a database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State
    Inherits from class Base to define what the table State
    looks like in a database.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
