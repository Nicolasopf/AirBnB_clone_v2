#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        options = {"cascade": "all, delete-orphan", "backref": "state"}
        cities = relationship("City", **options)
    else:
        @property
        def cities(self):
            objs = FileStorage.all()
            cities_list = []
            for k, v in objs:
                if v.state_id == self.id:
                    cities_list.append(v)
            return cities_list
