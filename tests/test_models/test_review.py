#!/usr/bin/python3
""" test description for function """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import os


@unittest.skipIf((os.getenv("HBNB_TYPE_STORAGE") == "db"),
                 "Reason usage of DBStorage")
class test_review(test_basemodel):
    """ test description for function """

    def __init__(self, *args, **kwargs):
        """ test description for function """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test description for function """
        new = self.value()
        self.assertEqual(type(new.text), str)

if __name__ == "__main__":
    unittest.main()
