import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """
    TestReview class to test the Review class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestReview object
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skip("Skipping test_place_id")
    def test_place_id(self):
        """
        Test the place_id attribute of Review
        """
        pass

    @unittest.skip("Skipping test_user_id")
    def test_user_id(self):
        """
        Test the user_id attribute of Review
        """
        pass

    @unittest.skip("Skipping test_text")
    def test_text(self):
        """
        Test the text attribute of Review
        """
        pass

    @unittest.skip("Skipping test_str")
    def test_str(self):
        """
        Test the __str__ method of Review
        """
        pass


if __name__ == '__main__':
    unittest.main()
