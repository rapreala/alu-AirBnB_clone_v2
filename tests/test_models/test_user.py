import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUser(test_basemodel):
    """
    TestUser class to test the User class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a TestUser object
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User()

    def test_str(self):
        """
        Test the __str__ method of User
        """
        new = self.value
        expected_str = '[User] ({}) {}'.format(new.id, new.__dict__)
        self.assertEqual(str(new), expected_str)

    def test_first_name(self):
        """
        Test the first_name attribute of User
        """
        new = self.value
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test the last_name attribute of User
        """
        new = self.value
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test the email attribute of User
        """
        new = self.value
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test the password attribute of User
        """
        new = self.value
        self.assertEqual(type(new.password), str)

    @unittest.skip("Skipping test_default")
    def test_default(self):
        """
        Test the default attribute values of User
        """
        pass

    @unittest.skip("Skipping test_kwargs")
    def test_kwargs(self):
        """
        Test the instantiation of User with kwargs
        """
        pass

    @unittest.skip("Skipping test_kwargs_int")
    def test_kwargs_int(self):
        """
        Test the instantiation of User with kwargs containing int
        """
        pass

    @unittest.skip("Skipping test_save")
    def test_save(self):
        """
        Test the save method of User
        """
        pass

    @unittest.skip("Skipping test_todict")
    def test_todict(self):
        """
        Test the to_dict method of User
        """
        pass

if __name__ == '__main__':
    unittest.main()
