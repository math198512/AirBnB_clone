#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class test_User(test_basemodel):
    """ """
    

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

        def test_email(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.email), str)
