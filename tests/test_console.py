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

    def test_emptyline(self):
        HBNBCommand().onecmd("")

    def test_quit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" help show")
            a = 'Showing the instance of a class of an id\n'
            self.assertEqual(a, f.getvalue())

    def test_help_clear(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help clear")
            a = 'clear the screen\n'
            self.assertEqual(a, f.getvalue())

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            a = 'Showing the instance of a class of an id\n'
            self.assertEqual(a, f.getvalue())

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            a = ' Updating class attributes \n'
            self.assertEqual(a, f.getvalue())

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            a = 'Exit when quit command is given\n'
            self.assertEqual(a, f.getvalue())


if __name__ == "__main__":
    unittest.main()
