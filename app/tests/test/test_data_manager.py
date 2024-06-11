import unittest
import os
import json
from app.models.user import User
from app.persistence.data_manager import DataManager

class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.user = User(email="test@example.com", password="password", first_name="Test", last_name="User")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_user(self):
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.user.email)
        self.assertEqual(retrieved_user.password, self.user.password)

    def test_update_user(self):
        self.user.save()
        self.user.first_name = "Updated"
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertEqual(retrieved_user.first_name, "Updated")

    def test_delete_user(self):
        self.user.save()
        self.user.delete()
        retrieved_user = User.get(self.user.id)
        self.assertIsNone(retrieved_user)

    def test_get_all_users(self):
        self.user.save()
        another_user = User(email="another@example.com", password="password", first_name="Another", last_name="User")
        another_user.save()
        users = User.get_all()
        self.assertEqual(len(users), 2)

if __name__ == '__main__':
    unittest.main()
