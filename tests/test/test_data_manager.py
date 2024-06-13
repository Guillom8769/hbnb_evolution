# tests/test/test_data_manager.py

import unittest
from app.models.user import User
from app.models.country import Country
from app.persistence.data_manager import DataManager

class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.data_manager.clear('User')
        self.data_manager.clear('Country')
        self.user = User(email="test@example.com", password="password", first_name="Test", last_name="User")
        self.country = Country(name="France", code="FR")

    def tearDown(self):
        self.data_manager.clear('User')
        self.data_manager.clear('Country')

    def test_save_and_get_user(self):
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.user.email)
        self.assertEqual(retrieved_user.password, self.user.password)

    def test_update_user(self):
        self.user.save()
        self.user.first_name = "Updated"
        self.user.email = "updated@example.com"  # Pour éviter le conflit d'email
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

    def test_save_duplicate_email(self):
        self.user.save()
        duplicate_user = User(email="test@example.com", password="password", first_name="Duplicate", last_name="User")
        with self.assertRaises(ValueError):
            duplicate_user.save()

    def test_save_and_get_country(self):
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, self.country.name)
        self.assertEqual(retrieved_country.code, self.country.code)

    def test_update_country(self):
        self.country.save()
        self.country.name = "Updated Country"
        self.country.save()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, "Updated Country")

    def test_delete_country(self):
        self.country.save()
        self.country.delete()
        retrieved_country = Country.get(self.country.id)
        self.assertIsNone(retrieved_country)

    def test_get_all_countries(self):
        self.country.save()
        another_country = Country(name="Spain", code="ES")
        another_country.save()
        countries = Country.get_all()
        self.assertEqual(len(countries), 2)

if __name__ == '__main__':
    unittest.main()
