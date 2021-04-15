#!/usr/bin/python3
"""This module tests console.py file.
Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_console.py"
"""
# from models.engine.file_storage import FileStorage as Storage
from models.__init__ import storage
from unittest.mock import create_autospec, patch
from console import HBNBCommand
from io import StringIO
import unittest
import pep8
import sys
import os


classes = ["User", "State", "City", "Amenity", "Place", "Review"]
# Storage = Storage()


class TestConsole(unittest.TestCase):
    ''' TestCase class for storing the unittests of the console. '''

    @unittest.skipIf((os.getenv("HBNB_TYPE_STORAGE") == "db"),
                     "Reason usage of DBStorage")
    def test_create_00(self):
        ''' Tests for the create command. '''
        # Create console session.
        cons = self.create_session()

        # Tests all classes.
        for className in classes:
            # Test "create {} test='TEST'".
            with patch('sys.stdout', new=StringIO()) as Output:
                cons.onecmd('create {} test=\"TEST\"'.format(className))
                create_stdout = Output.getvalue().strip()
                create_stdout = '{}.{}'.format(className, create_stdout)
                self.assertTrue(create_stdout in storage.all())

    @classmethod
    def tearDown(self):
        ''' Removes the file.json on each test. '''
        try:
            os.remove("file.json")
        except:
            pass

    def setUp(self):
        ''' Sets up the mock stdin and stderr. '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create_session(self, server=None):
        ''' Creates the cmd session. '''
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

if __name__ == "__main__":
    unittest.main()
