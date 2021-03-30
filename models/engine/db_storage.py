#!/usr/bin/python3
""" Create the new engine, in Database """

from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy import create_engine
from models.base_model import Base
from os import getenv
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.user import User


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """ Create the engine for the database """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dic = {}
        if cls is None:
            classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            for clas in classes:
                query = self.__session.query(clas)
                first_dic = clas + "." + query.id
                setattr(dic, first_dic, query)
        else:
            query = self.__session.query(cls)
            for item in query:
                first_dic = type(item).__name__ + "." + obj.id
                setattr(dic, first_dic, item)
        return objDict

    def new(self, obj):
        """ Add the obj to the current db session """
        self.__session.add(obj)

    def save(self):
        """ Save the current changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an object """
        self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy) (WARNING: all
        classes who inherit from Base must be imported before calling
        Base.metadata.create_all(engine))
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(session)
        self.__session = Session()
