import unittest
import json
from app import create_app

class UserEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/users/', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'Test',
            'last_name': 'User'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_user(self):
        response = self.client.post('/users/', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'Test',
            'last_name': 'User'
        }), content_type='application/json')
        user_id = response.get_json()['id']
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['email'], 'test@example.com')

    def test_update_user(self):
        response = self.client.post('/users/', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'Test',
            'last_name': 'User'
        }), content_type='application/json')
        user_id = response.get_json()['id']
        response = self.client.put(f'/users/{user_id}', data=json.dumps({
            'first_name': 'Updated'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['first_name'], 'Updated')

    def test_delete_user(self):
        response = self.client.post('/users/', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'Test',
            'last_name': 'User'
        }), content_type='application/json')
        user_id = response.get_json()['id']
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
