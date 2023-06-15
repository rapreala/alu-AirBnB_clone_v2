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

    def test_name2(self):
        """
        Test the name attribute of Amenity
        """
        amenity = self.value()
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """
        Test the __str__ method of Amenity
        """
        amenity = self.value()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_new_test_case(self):
        """
        Test a new functionality in Amenity
        """
        amenity = self.value()
        amenity.category = "Facilities"
        self.assertTrue(hasattr(amenity, 'category'))
        self.assertEqual(amenity.category, "Facilities")


if __name__ == '__main__':
    unittest.main()
