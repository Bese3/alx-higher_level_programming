#!/usr/bin/python3
"""Module model_city
Defines a City table and its rows using SQLAlchemy
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State, Base


class City(Base):
    """Class City
    Inherits from class Base to define what the table City
    looks like in a database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String, ForeignKey("state.id"), nullable=False)
