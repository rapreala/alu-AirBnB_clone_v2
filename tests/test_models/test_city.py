import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """
    TestCity class to test the City class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestCity object
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skip("Skipping test_state_id")
    def test_state_id(self):
        """
        Test the state_id attribute of City
        """
        pass

    @unittest.skip("Skipping test_name")
    def test_name(self):
        """
        Test the name attribute of City
        """
        pass

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of City
        """
        pass


if __name__ == '__main__':
    unittest.main()
