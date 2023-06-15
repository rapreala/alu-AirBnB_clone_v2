import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(test_basemodel):
    """
    TestAmenity class to test the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestAmenity object
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skip("Skipping test_save")
    def test_save(self):
        """
        Test the save method of Amenity
        """
        pass

    @unittest.skip("Skipping test_name2")
    def test_name2(self):
        """
        Test the name attribute of Amenity
        """
        pass

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of Amenity
        """
        pass


if __name__ == '__main__':
    unittest.main()
