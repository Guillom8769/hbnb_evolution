import unittest
import os
import json
from app.models.country import Country
from app.persistence.data_manager import DataManager

class CountryModelTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.country = Country(code="FR", name="France")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_country(self):
        self.country.save()
        retrieved_country = Country.get(self.country.code)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, self.country.name)

    def test_update_country(self):
        self.country.save()
        self.country.name = "Updated Country"
        self.country.save()
        retrieved_country = Country.get(self.country.code)
        self.assertEqual(retrieved_country.name, "Updated Country")

    def test_delete_country(self):
        self.country.save()
        self.country.delete()
        retrieved_country = Country.get(self.country.code)
        self.assertIsNone(retrieved_country)

    def test_get_all_countries(self):
        self.country.save()
        another_country = Country(code="US", name="United States")
        another_country.save()
        countries = Country.get_all()
        self.assertEqual(len(countries), 2)

if __name__ == '__main__':
    unittest.main()
