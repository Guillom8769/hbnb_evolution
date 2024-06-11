import unittest
import json
from app import create_app

class CityEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_city(self):
        response = self.client.post('/cities/', data=json.dumps({
            'name': 'Paris',
            'country_code': 'FR'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_city(self):
        response = self.client.post('/cities/', data=json.dumps({
            'name': 'Paris',
            'country_code': 'FR'
        }), content_type='application/json')
        city_id = response.get_json()['id']
        response = self.client.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Paris')

    def test_update_city(self):
        response = self.client.post('/cities/', data=json.dumps({
            'name': 'Paris',
            'country_code': 'FR'
        }), content_type='application/json')
        city_id = response.get_json()['id']
        response = self.client.put(f'/cities/{city_id}', data=json.dumps({
            'name': 'Updated City'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated City')

    def test_delete_city(self):
        response = self.client.post('/cities/', data=json.dumps({
            'name': 'Paris',
            'country_code': 'FR'
        }), content_type='application/json')
        city_id = response.get_json()['id']
        response = self.client.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
