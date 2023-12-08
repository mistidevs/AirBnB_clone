#!/usr/bin/python3
"""FileStorage class that stores models in JSON format for persistence"""
import copy
import json
import datetime
from models.base_model import BaseModel
from models.user import User


def str_to_datetime(s):
    """Convert a string in ISO format to a datetime object"""
    return datetime.datetime.fromisoformat(s)

class FileStorage:
    """The nitty gritties of how it does this"""
    __objects = {}
    __file_path = "file.json"

     @property
    def objects(self):
        """Return the __objects dictionary"""
        return self.__objects

     def all(self):
        """Return all the objects made"""
        return self.__objects

    def new(self, obj):
        """Adding a new instance"""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

     def save(self):
        """Saving all the objects to a JSON file"""
        json_opt = {}
        for key, value in self.__objects.items():
            json_opt[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(json_opt, f)

    def reload(self):
        """Converting JSON file to objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                cls_name = value["__class__"]
                cls = eval(cls_name)
                self.__objects[key] = cls(**value)

        except FileNotFoundError:
            pass
