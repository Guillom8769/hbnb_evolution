import unittest
import json
from app import create_app

class PlaceEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        response = self.client.post('/places/', data=json.dumps({
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Test St',
            'city_id': 'city123',
            'latitude': 12.34,
            'longitude': 56.78,
            'host_id': 'host123',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_place(self):
        response = self.client.post('/places/', data=json.dumps({
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Test St',
            'city_id': 'city123',
            'latitude': 12.34,
            'longitude': 56.78,
            'host_id': 'host123',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4
        }), content_type='application/json')
        place_id = response.get_json()['id']
        response = self.client.get(f'/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Test Place')

    def test_update_place(self):
        response = self.client.post('/places/', data=json.dumps({
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Test St',
            'city_id': 'city123',
            'latitude': 12.34,
            'longitude': 56.78,
            'host_id': 'host123',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4
        }), content_type='application/json')
        place_id = response.get_json()['id']
        response = self.client.put(f'/places/{place_id}', data=json.dumps({
            'name': 'Updated Place'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated Place')

    def test_delete_place(self):
        response = self.client.post('/places/', data=json.dumps({
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Test St',
            'city_id': 'city123',
            'latitude': 12.34,
            'longitude': 56.78,
            'host_id': 'host123',
            'num_rooms': 3,
            'num_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4
        }), content_type='application/json')
        place_id = response.get_json()['id']
        response = self.client.delete(f'/places/{place_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
