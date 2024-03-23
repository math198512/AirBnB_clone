#!/usr/bin/python3
"""
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
