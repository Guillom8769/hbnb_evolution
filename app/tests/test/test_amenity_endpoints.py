import unittest
import json
from app import create_app

class AmenityEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_amenity(self):
        response = self.client.post('/amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        amenity_id = response.get_json()['id']
        response = self.client.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'WiFi')

    def test_update_amenity(self):
        response = self.client.post('/amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        amenity_id = response.get_json()['id']
        response = self.client.put(f'/amenities/{amenity_id}', data=json.dumps({
            'name': 'Updated Amenity'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated Amenity')

    def test_delete_amenity(self):
        response = self.client.post('/amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        amenity_id = response.get_json()['id']
        response = self.client.delete(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
