#!/usr/bin/python3
"""Def the unittest for the place class"""
import models
import unittest
from datetime import datetime
from time import sleep
import os
from models.place import Place


class PlaceTest_value(unittest.TestCase):
    """Unittest for tha palce class's values"""

    def test_no_args(self):
        self.assertEqual(Place, type(place()))

    def test_stored_value(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Place.id))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Place.updated_at))

    def test_created_at_datetime(self):
        seld.assertequal(datetime, type(place.created_at))

    def test_city_id(self):
        place1 = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place1))
        self.assertNotIn("city_id", place1.__dict__)

    def test_descri(self):
        place1 = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place1))
        self.assertNotIn("description", place1.dict__)

    def test_name(self):
        place1 = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place1))
        self.assertNotIn("name", place1.__dict__)

    def test_user_id(self):
        place1 = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place1))
        self.assertNotIn("user_id", place1.__dict__)

    def test_numb_rooms(self):
        place1 = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place1))
        self.assertNotIn("number_rooms", place1.__dict__)

    def test_number_bathrooms(self):
        place1 = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(palce1))
        self.assertNotIn("number_bathrooms", place1.__dict__)

    def test_price(self):
        place1 = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place1))
        self.assertNotIn("price_by_night", place1.__dict__)

    def test_max_guest(self):
        place1 = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place1))
        self.assertNotIn("max_guest", place1.__dict__)

    def test_latitude(self):
        place1 = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place1))
        self.assertNotIn("latitude", place1.__dict__)

    def test_longitude(self):
        place1 = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place1))
        self.assertNotIn("longitude", place1.__dict__)

    def test_id_uniq(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_diff_created_at(self):
        p1 = Place()
        sleep(1)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_diff_updated_at(self):
        p1 = Place()
        sleep(1)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)
