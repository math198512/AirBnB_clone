#!/usr/bin/python3
"""
This module defines all attributes/methods for class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a review"""
    place_id = ''
    user_id = ''
    text = ''
