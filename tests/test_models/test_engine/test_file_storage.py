#!/usr/bin/python3
""" Testing FileStorage class """
import models
import json
import unittest
from unittest.mock import patch
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


if __name__ == "__main__":
    unittest.main()
