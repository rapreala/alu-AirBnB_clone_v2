import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """
    TestPlace class to test the Place class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestPlace object
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skip("Skipping test_city_id")
    def test_city_id(self):
        """
        Test the city_id attribute of Place
        """
        pass

    @unittest.skip("Skipping test_name")
    def test_name(self):
        """
        Test the name attribute of Place
        """
        pass

    @unittest.skip("Skipping test_description")
    def test_description(self):
        """
        Test the description attribute of Place
        """
        pass

    @unittest.skip("Skipping test_number_rooms")
    def test_number_rooms(self):
        """
        Test the number_rooms attribute of Place
        """
        pass

    @unittest.skip("Skipping test_number_bathrooms")
    def test_number_bathrooms(self):
        """
        Test the number_bathrooms attribute of Place
        """
        pass

    @unittest.skip("Skipping test_max_guest")
    def test_max_guest(self):
        """
        Test the max_guest attribute of Place
        """
        pass

    @unittest.skip("Skipping test_price_by_night")
    def test_price_by_night(self):
        """
        Test the price_by_night attribute of Place
        """
        pass

    @unittest.skip("Skipping test_latitude")
    def test_latitude(self):
        """
        Test the latitude attribute of Place
        """
        pass

    @unittest.skip("Skipping test_longitude")
    def test_longitude(self):
        """
        Test the longitude attribute of Place
        """
        pass

    @unittest.skip("Skipping test_amenity_ids")
    def test_amenity_ids(self):
        """
        Test the amenity_ids attribute of Place
        """
        pass

    @unittest.skip("Skipping test_user_id")
    def test_user_id(self):
        """
        Test the user_id attribute of Place
        """
        pass

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of Place
        """
        pass


if __name__ == '__main__':
    unittest.main()
