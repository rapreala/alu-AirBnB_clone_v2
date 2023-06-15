import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """
    TestState class to test the State class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestState object
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skip("Skipping test_name3")
    def test_name3(self):
        """
        Test the name attribute of State
        """
        pass

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of State
        """
        pass


if __name__ == '__main__':
    unittest.main()
