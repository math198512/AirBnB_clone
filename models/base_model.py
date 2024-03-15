#!/usr/bin/python3
"""
This module defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        string representation
        """

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """

        """

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        """

        self_dict = self.__dict__.copy()
        self_dict["__class__"] = self.__class__.__name__
        self_dict["created_at"] = self.created_at.isoformat()
        self_dict["updated_at"] = self.updated_at.isoformat()

        return (self_dict)
