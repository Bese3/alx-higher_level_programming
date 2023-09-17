#!/usr/bin/python3
"""Module model_city
Defines a City class that will be written to a database"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """
    The City class represents a city in a database table,
    with attributes for id, name, and state_id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # states = relationship("State", back_populates="cities")
