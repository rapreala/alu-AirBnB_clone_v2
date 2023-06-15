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
        user = User()
        string = str(user)
        self.assertEqual(string, f"[{self.name}] ({user.id}) {user.__dict__}")

    def test_first_name(self):
        """
        Test the first_name attribute of User
        """
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name(self):
        """
        Test the last_name attribute of User
        """
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

    def test_email(self):
        """
        Test the email attribute of User
        """
        user = User()
        user.email = "johndoe@example.com"
        self.assertEqual(user.email, "johndoe@example.com")

    def test_password(self):
        """
        Test the password attribute of User
        """
        user = User()
        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_default(self):
        """
        Test the default attribute values of User
        """
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")

    def test_kwargs(self):
        """
        Test the instantiation of User with kwargs
        """
        kwargs = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password': 'password123'
        }
        user = User(**kwargs)
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertEqual(user.password, "password123")

    def test_kwargs_int(self):
        """
        Test the instantiation of User with kwargs containing int
        """
        kwargs = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'age': 25
        }
        with self.assertRaises(TypeError):
            user = User(**kwargs)

    def test_save(self):
        """
        Test the save method of User
        """
        user = User()
        user.save()
        self.assertIsNotNone(user.updated_at)

    def test_todict(self):
        """
        Test the to_dict method of User
        """
        user = User()
        user.first_name = "John"
        user.last_name = "Doe"
        user.email = "johndoe@example.com"
        user.password = "password123"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['email'], "johndoe@example.com")
        self.assertEqual(user_dict['password'], "password123")

    def test_new_attribute(self):
        """
        Test the creation of a new attribute in User
        """
        user = User()
        user.new_attribute = "new value"
        self.assertTrue(hasattr(user, 'new_attribute'))
        self.assertEqual(user.new_attribute, "new value")

    def test_delete_attribute(self):
        """
        Test the deletion of an attribute in User
        """
        user = User()
        user.new_attribute = "new value"
        self.assertTrue(hasattr(user, 'new_attribute'))
        delattr(user, 'new_attribute')
        self.assertFalse(hasattr(user, 'new_attribute'))


if __name__ == '__main__':
    unittest.main()
