#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """ class state """

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('namne', String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")
