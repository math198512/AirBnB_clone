#!/usr/bin/python3
"""
This module serializes instances to a JSON file and
deserializes JSON file to instances
"""

import os
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(self, cls=None):
        """
        returns a dictionary containing every object
        """
        if (not cls):
            return self.__objects
        result = {}
        for key in self.__objects.keys():
            if (key.split(".")[0] == cls.__name__):
                result.update({key: self.__objects[key]})
        return result
    
    def new(self, obj):
        """
        """

        key = obj.__class__.__name__ + "." + obj.id
        __class__.__objects[key] = obj

    def save(self):
        """
        """

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as wr:
            json.dump(new_dict, wr)

    def reload(self):
        """
        """

        try:
            with open(self.__file_path, 'r') as f:
                a_dict = json.load(f)
            for key in a_dict:
                self.__objects[key] = class_list[a_dict[key]["__class__"]](**a_dict[key])
        except:
            pass
