#!/usr/bin/python3
"""Def the unittest for the Review class"""
import models
import unittest
from datetime import datetime
from time import sleep
import os
from models.place import Review


class TestReview_values(unittest.TestCase):
    """test the Review class values"""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_stored_values(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(Review.id))

    def test_place(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_text(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_user_id(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_is", rev.__dict__)

    def uni_id(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def deff_updated_at(self):
        rev1 = Review()
        sleep(1)
        rev2 = Review()
        self.assertNotEqual(rev1.updated_at, rev2.updated_at)

    def deff_created_at(self):
        rev1 = Review()
        sleep(1)
        rev2 = Review()
        self.assertNotEqual(rev1.created_at, rev2.created_at)

if __name__ == "__main__":
    unittest.main()
