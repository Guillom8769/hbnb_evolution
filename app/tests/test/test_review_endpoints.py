import unittest
import json
from app import create_app

class ReviewEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        response = self.client.post('/reviews/', data=json.dumps({
            'user_id': 'user123',
            'place_id': 'place123',
            'rating': 5,
            'comment': 'Great place!'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_review(self):
        response = self.client.post('/reviews/', data=json.dumps({
            'user_id': 'user123',
            'place_id': 'place123',
            'rating': 5,
            'comment': 'Great place!'
        }), content_type='application/json')
        review_id = response.get_json()['id']
        response = self.client.get(f'/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['comment'], 'Great place!')

    def test_update_review(self):
        response = self.client.post('/reviews/', data=json.dumps({
            'user_id': 'user123',
            'place_id': 'place123',
            'rating': 5,
            'comment': 'Great place!'
        }), content_type='application/json')
        review_id = response.get_json()['id']
        response = self.client.put(f'/reviews/{review_id}', data=json.dumps({
            'comment': 'Updated comment'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['comment'], 'Updated comment')

    def test_delete_review(self):
        response = self.client.post('/reviews/', data=json.dumps({
            'user_id': 'user123',
            'place_id': 'place123',
            'rating': 5,
            'comment': 'Great place!'
        }), content_type='application/json')
        review_id = response.get_json()['id']
        response = self.client.delete(f'/reviews/{review_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
