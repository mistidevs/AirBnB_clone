#!/usr/bin/python3
""" Testing the BaseModel class """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Nitty gritties """
    def test_dif_and_type_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertEqual(type(bm1.id), str)

    def test_other_attributes(self):
        bm3 = BaseModel()
        self.assertEqual(type(bm3.updated_at), datetime)
        self.assertEqual(type(bm3.created_at), datetime)

    def test_create_from_dict(self):
        bm4 = BaseModel()
        bm4.name = "4th_model"
        bm4.my_number = 89
        json_dict = bm4.to_dict()
        bm5 = BaseModel(**json_dict)
        self.assertEqual(bm5.id, bm4.id)
        self.assertEqual(bm5.created_at, bm4.created_at)
        self.assertEqual(bm5.updated_at, bm4.updated_at)
        self.assertEqual(bm5.name, bm4.name)
        self.assertEqual(bm5.my_number, bm4.my_number)

    def test_to_dict(self):
        bm6 = BaseModel()
        json_dict = bm6.to_dict()
        self.assertEqual(type(json_dict), dict)
        self.assertEqual(bm6.id, json_dict['id'])

    def test_str(self):
        bm7 = BaseModel()
        self.assertEqual(type(bm7.__str__()), str)

    def test_save(self):
        bm8 = BaseModel()
        old_time = bm8.updated_at
        bm8.save()
        self.assertNotEqual(old_time, bm8.updated_at)


if __name__ == '__main__':
    unittest.main()
