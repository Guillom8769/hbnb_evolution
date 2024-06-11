import unittest
from app import create_app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # Par défaut, il n'y a pas de route à la racine.

if __name__ == '__main__':
    unittest.main()
