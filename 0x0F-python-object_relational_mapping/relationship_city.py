#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """ class state """

    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column(
            'state_id', Integer, ForeignKey(State.id), nullable=False)
