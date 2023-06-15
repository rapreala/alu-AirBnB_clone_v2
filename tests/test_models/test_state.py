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

    def test_name3(self):
        """
        Test the name attribute of State
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_str(self):
        """
        Test the __str__ method of State
        """
        state = State()
        state.name = "California"
        string = str(state)
        self.assertEqual(string, f"[{self.name}] ({state.id}) {state.__dict__}")


if __name__ == '__main__':
    unittest.main()
