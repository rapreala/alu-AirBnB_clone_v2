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

    def test_place_id(self):
        """
        Test the place_id attribute of Review
        """
        review = Review()
        review.place_id = "abc123"
        self.assertEqual(review.place_id, "abc123")

    def test_user_id(self):
        """
        Test the user_id attribute of Review
        """
        review = Review()
        review.user_id = "xyz456"
        self.assertEqual(review.user_id, "xyz456")

    def test_text(self):
        """
        Test the text attribute of Review
        """
        review = Review()
        review.text = "This is a review."
        self.assertEqual(review.text, "This is a review.")

    def test_str(self):
        """
        Test the __str__ method of Review
        """
        review = Review()
        review.place_id = "abc123"
        review.user_id = "xyz456"
        review.text = "This is a review."
        string = str(review)
        self.assertEqual(string, f"[{self.name}] ({review.id}) {review.__dict__}")


if __name__ == '__main__':
    unittest.main()
