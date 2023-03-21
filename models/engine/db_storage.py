#!/usr/bin/python3
'''DBStorage'''
from sqlalchemy import create_engine as ce, MetaData as md
from sqlalchemy.orm import sessionmaker as sm, relationship as rm
from os import getenv as ge


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = ge('HBNB_MYSQL_USER')
        pwrd = ge('HBNB_MYSQL_PWD')
        host = ge('HBNB_MYSQL_HOST')
        dtbs = ge('HBNB_MYSQL_DB')
        self.__engine = ce(f'mysql+mysqldb://{user}:{pwrd}@{host}/{dtbs}', pool_pre_ping=True)
        if ge('HBNB_ENV') == 'test':
            metadata = md()
            metadata.reflect(bind=engine)
            metadata.drop_all(bind=engine)

    def all(self, cls=None):
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = [User, Place, State, City, Amenity, Review]
        Session = sm(self.__engine)
        DBStorage.__session = Session()
        all_results = {}
        if cls and cls in classes:
            instances = DBStorage.__session.query(cls).all()
        else if cls is None:
            instances = []
            for i in classes:
                instances.extend(DBStorage.__session.query(i).all())
        for obj in instances:
            key = f"{obj.__class__.___name__}"."{obj.id}"
            all_results[key] = obj
        DBStorage.__session.close()
        return all_results
