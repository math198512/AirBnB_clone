#!/usr/bin/python3
"""
This module defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.uctnow()

    def __str__(self):
        """
        """

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """

        """

        self.updated_at = datetime.utcnow()

    def to_dict():
        """
        """

        self_dict = self.__dict__.copy()
        self_dict["__class__"] = slef.__class__.__name__
        self_dict["created_at"] = self.created_at.isoformat()
        self_dict["updated_at"] = self.updated_at.isoformat()

        return (slef_dict)
