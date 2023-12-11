#!/usr/bin/python3
"""Def the unittest for the city class"""
import models
import unittest
from datetime import datetime
from time import sleep
import os
from models.city import City


class TestCity_value(unittest.TestCase):
    """tast the city clas value"""

    def test_no_args(self):
        self.assertEqual(City(), model.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(City.id))

    def test_name(self):
        city1 = City()
        self.assertEqual(str, type(City.name))
        self.assertNotIn("name", city1.__dict__)
        self.assertIn("name", dir(city1))

    def test_state_id(self):
        city1 = City()
        self.assertEqual(str, type(City().state_id))
        self.assertNotIn("state_id", dir(city1))
        self.assertIn("state_id", city1.__dict__)

    def id_uniq(self):
        city1 =  City()
        sleep(1)
        city2 = City()
        self.assetNotEqual(city1.id, city2.id)

    def deff_created_at(self):
        city1 = City()
        sleep(1)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def deff_updated_at(self):
        city1 = City()
        sleep(1)
        city2 = City()
        self.assertNotEqual(city1.updated_at, city2.updated_at)

if __name__ == "__main__":
    unittest.main()
