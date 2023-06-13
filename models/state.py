#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models import storage


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances
           with state_id equals to the current State.id"""
        city_instances = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                city_instances.append(city)
        return city_instances
