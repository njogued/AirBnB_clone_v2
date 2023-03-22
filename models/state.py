#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class
    name = ""
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if ge("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            '''return list of cities if not using a database'''
            return [city for city in self.cities]
