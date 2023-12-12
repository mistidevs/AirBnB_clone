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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" help show")
            a = 'prints the string representation of an instance\n'
            self.assertEqual(a, f.getvalue())

    def test_clear(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help clear")
            a = 'clear the screen\n'
            self.assertEqual(a, f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            a = 'Deletes an instance based on the class name and id\n'
            self.assertEqual(a, f.getvalue())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            a = 'Updates the class\n'
            self.assertEqual(a, f.getvalue())

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            a = 'Quit command to exit the program\n'
            self.assertEqual(a, f.getvalue())

if __name__ == "__main__":
    unittest.main()
