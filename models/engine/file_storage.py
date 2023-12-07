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
