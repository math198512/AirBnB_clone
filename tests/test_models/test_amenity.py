#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.user import User
from models.amenity import Amenity

class test_Amenity(TestBaseModel):
    """ """
    

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

if __name__ == "__main__":
    unittest.main()
