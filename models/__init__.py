#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""
from models.engine.db_storage import DBStorage
from os import getenv


storage_type = getenv('HBNB_STORAGE')
if storage_type == 'db':
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
