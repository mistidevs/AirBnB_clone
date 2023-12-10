#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):
    def test_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.__dict__, {"id": bm1.id,
                                       "created_at": bm1.created_at, "updated_at": bm1.updated_at})

    def test_created(self):
        bm3 = BaseModel()
        self.assertEqual(type(bm3.created_at), datetime)
        self.assertEqual(type(bm3.updated_at), datetime)

    def test_create_from_dictionary(self):
        bm4 = BaseModel()
        bm4_id = bm4.id
        bm4.name = "dictionary_check"
        bm4.my_number = 89
        bm4_json = bm4.to_dict()
        self.assertEqual(type(bm4_json), dict)
        bm4 = BaseModel(**bm4_json)
        self.assertEqual(bm4.id, bm4_id)
        self.assertEqual(type(bm4.created_at), datetime)
        self.assertEqual(type(bm4.updated_at), datetime)

    def test_save(self):
        bm6 = BaseModel()
        time_create = bm6.updated_at
        bm6.save()
        self.assertNotEqual(bm6.updated_at, time_create)

    def test_str(self):
        bm7 = BaseModel()
        bm_str = f"[{type(bm7).__name__}] ({bm7.id}) {bm7.__dict__}"
        self.assertEqual(str(bm7), bm_str)

    def test_to_dict(self):
        bm8 = BaseModel()
        bm_dict = bm8.to_dict()
        self.assertEqual(bm_dict["__class__"], type(bm8).__name__)
        self.assertEqual(bm_dict["id"], bm8.id)
        self.assertEqual(bm_dict["created_at"], str(bm8.created_at.isoformat()))
        self.assertEqual(bm_dict["updated_at"], str(bm8.updated_at.isoformat()))


if __name__ == '__main__':
    unittest.main()
