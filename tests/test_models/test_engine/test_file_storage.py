#!/usr/bin/python3
""" Testing FileStorage class """
import models
import copy
import json
import unittest
from unittest.mock import patch
from unittest.mock import mock_open
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime


class TestFileStorage(unittest.TestCase):
    """ Nitty gritties """
    def setUp(self):
        self.file_storage = FileStorage()

    @patch("models.engine.file_storage.FileStorage.save")
    def test_new_method(self, mock_save):
        user = User()
        user.email = "test@example.com"
        user.password = "123456"
        self.file_storage.new(user)
        key = type(user).__name__ + "." + user.id
        self.assertIn(key, self.file_storage.objects)
        self.assertEqual(self.file_storage.objects[key], user)
        self.assertEqual(self.file_storage.objects,
                         self.file_storage.all())

    def test_objects(self):
        bm1 = BaseModel()
        json_dict = bm1.to_dict()
        bm2 = BaseModel(**json_dict)
        self.assertEqual(self.file_storage.file_path, "file.json")

    def test_save_empty(self):
        with patch("builtins.open", mock_open()) as mock_file:
            self.file_storage.save()
            mock_file.assert_called_once_with("file.json",
                                              mode="w", encoding="utf-8")
            self.assertEqual(mock_file().write.call_args[0][0],
                             '}')

    def test_reload_different_objects(self):
        user = User()
        state = State()
        self.file_storage.new(user)
        self.file_storage.new(state)
        self.file_storage.save()
        self.file_storage.reload()
        key1 = type(user).__name__ + "." + user.id
        key2 = type(state).__name__ + "." + state.id
        self.assertIn(key1,
                      self.file_storage.objects)
        self.assertIn(key2,
                      self.file_storage.objects)
        self.assertIsInstance(self.file_storage.objects[key1],
                              User)
        self.assertIsInstance(self.file_storage.objects[key2],
                              State)

if __name__ == "__main__":
    unittest.main()
