#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
            "Place", backref="cities", cascade="all, delete-orphan")
    else:
        @property
        def places(self):
            """Getter attribute in case of file storage"""
            place_list = []
            for place in models.storage.all(Place).values():
                if place.city_id == self.id:
                    place_list.append(place)
            return place_list
