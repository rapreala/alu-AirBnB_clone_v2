#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv

# Import all models
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

storage_type = getenv('HBNB_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
