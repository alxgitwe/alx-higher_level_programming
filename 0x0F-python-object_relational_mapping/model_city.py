#!/usr/bin/python3
"""
    script class City.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class City(Base):
    """
    class city.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"City(id={self.id}, name={self.name}, state_id={self.state_id})"
