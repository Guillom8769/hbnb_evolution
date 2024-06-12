import unittest
from app.models.user import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", password="password", first_name="Test", last_name="User")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    def test_user_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['first_name'], "Test")
        self.assertEqual(user_dict['last_name'], "User")

if __name__ == '__main__':
    unittest.main()
