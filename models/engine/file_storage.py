#!/usr/bin/python3
"""Def of FileStorage class"""


import json

class FileStorage:
    """serializes instances to a JSON file and deserializes it"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """mothode initializing"""
        pass

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        seri_dict = {}
        for key, value in self.__objects:
            seri_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(seri_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
               di = json.load(f)
        except:
            pass

