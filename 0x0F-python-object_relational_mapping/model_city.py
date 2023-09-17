#!/usr/bin/python3
"""Module model_city
Defines a City class that will be written to a database"""
from model_state import Base, Column, Integer, String, State
from sqlalchemy import ForeignKey


class City(Base):
    """
    The City class represents a city in a database table,
    with attributes for id, name, and state_id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
