import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models


class ConsoleTestCase(unittest.TestCase):
    """
    Test for console
    """

    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = StringIO()
        self.storage = models.storage

    def tearDown(self):
        del self.stdout
        del self.storage

    def test_create(self):
        """
        test create basic
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State')
        state_id = self.stdout.getvalue()[:-1]
        self.assertIsNotNone(
            self.storage.all()["State.{}".format(state_id)])

    def test_create_save(self):
        """
        test create save
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        self.assertIsNotNone(
            self.storage.all()["State.{}".format(state_id)])

    def test_create_non_existing_class(self):
        """
        test non-existing class
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create MyModel')
        self.assertEqual("** class doesn't exist **\n", self.stdout.getvalue())

    def test_all(self):
        """
        test all
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('all State')
        self.assertIn("State", self.stdout.getvalue())

    def test_update(self):
        """
        test update
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd(
            'update State {} name "New California"'.format(state_id))
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('show State {}'.format(state_id))
        self.assertIn("New California", self.stdout.getvalue())

    def test_show(self):
        """
        test show
        """
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('show State {}'.format(state_id))
        self.assertIn("California", self.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
