#!/usr/bin/python3
"""
    tests for FileStorage
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_FileStorage(unittest.TestCase):
    """
        Base test class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy

    def test_attrs(self):
        """
            attribute tests
        """
        self.assertTrue(hasattr(self.dummy, "_FileStorage__objects"))
        self.assertTrue(isinstance(self.dummy._FileStorage__objects, dict))
        self.assertTrue(hasattr(self.dummy, "_FileStorage__file_path"))
        self.assertTrue(isinstance(self.dummy._FileStorage__file_path, str))

class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

if __name__ == "__main__":
    unittest.main()
