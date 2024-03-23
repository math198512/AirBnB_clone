#!/usr/bin/python3
"""
This module defines all attributes/methods for class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city"""
    state_id = ''
    name = ''
