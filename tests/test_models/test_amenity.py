#!/usr/bin/python3
"""Def the unittest for the Amenity class"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
import os
from models.amenity import Amenity


class Testamenity_values(unittest.TestCase):
    """Test the amenity class values"""

    def test_no_args(self):
        self.assertEqual(Amenity(), type(Amenity()))

    def test_id_str(self):
        self.assertEqual(str, type(Amenity.id))

    def test_uniq_id(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def deff_created_at(self):
        am1 = Amenity()
        sleep(1)
        am2 = Amenity()
        self.assertNotEqual(am1.created_at, am2.craeted_at)

    def deff_updated_at(self):
        am1 = Amenity()
        sleep(1)
        am2 = Amenity()
        self.assertNotEqual(am1.updated_at, am2.updated_at)

if __name__ == "__main__":
    unittest.main()
