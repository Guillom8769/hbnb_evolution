# tests/test/test_country.py

import unittest
from app.models.country import Country
from app.persistence.data_manager import DataManager

class CountryModelTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.data_manager.clear('Country')
        self.country = Country(name="France", code="FR")

    def tearDown(self):
        self.data_manager.clear('Country')

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
