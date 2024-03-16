#!/usr/bin/python3
"""
This module serializes instances to a JSON file and
deserializes JSON file to instances
"""

import os
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns a dictionary containing every object
        """
        return self.__objects
    
    def new(self, obj):
        """
        """

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

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

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r",
                    encoding="UTF-8") as js_file:
                try:
                    dict_objs = json.load(js_file)
                    for key, value in dict_objs.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        inst = cls(**values)
                        FileStorage.__objects__[key] = inst
                except Exception:
                    pass
