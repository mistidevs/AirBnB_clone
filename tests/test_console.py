#!/usr/bin/python3
""" Testing the functionalities of the console """
import unittest
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestConsole(unittest.TestCase):
    """ Testing the console functions """
    def test_show(self):
        pass


if __name__ == "__main__":
    unittest.main()
