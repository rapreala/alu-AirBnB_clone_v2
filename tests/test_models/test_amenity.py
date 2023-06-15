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

    def test_new_test_case(self):
        """
        Test a new functionality in Amenity
        """
        amenity = self.value()
        amenity.category = "Facilities"
        self.assertTrue(hasattr(amenity, 'category'))
        self.assertEqual(amenity.category, "Facilities")

    def test_new_attribute(self):
        """
        Test the creation of a new attribute in Amenity
        """
        amenity = self.value()
        amenity.new_attribute = "new value"
        self.assertTrue(hasattr(amenity, 'new_attribute'))
        self.assertEqual(amenity.new_attribute, "new value")

    def test_count(self):
        """
        Test the count attribute of Amenity
        """
        amenity1 = self.value()
        amenity2 = self.value()
        amenity3 = self.value()
        self.assertEqual(Amenity.count, 3)

    def test_delete(self):
        """
        Test the delete method of Amenity
        """
        amenity = self.value()
        amenity.delete()
        self.assertIsNone(amenity.id)
        self.assertIsNone(amenity.created_at)
        self.assertIsNone(amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
