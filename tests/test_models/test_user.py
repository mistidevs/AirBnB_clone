#!/usr/bin/python3
"""Def unittest for User"""
import unittest
from time import sleep
from models.user import User
import models
import os
from datetime import datetime


class TestUser(unittest.TestCase):
     """Unittests for User class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_value_stored(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_is_str(self):
        self.assertEqual(str, type(User().password))

    def test_last_name_is_str(self):
        self.assertEqual(str, type(User().last_name))

    def test_created_at_value(self):
        User1 = User()
        sleep(1)
        User2 = User()
        self.assertNotEqual(User1.created_at, User2.created_at)

    def test_updated_at_value(self):
        user1 = User()
        sleep(1)
        user2 = User()
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_id_unique(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)
