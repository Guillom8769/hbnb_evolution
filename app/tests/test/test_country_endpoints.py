import unittest
import json
from app import create_app
from app.models.country import Country

class CountryEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        Country.preload_data()

    def test_get_countries(self):
        response = self.client.get('/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_country(self):
        response = self.client.get('/countries/FR')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['code'], 'FR')

if __name__ == '__main__':
    unittest.main()
