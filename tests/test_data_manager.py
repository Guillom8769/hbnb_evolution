import unittest
from app.persistence.data_manager import DataManager
from app.models.user import User
from app.models.city import City
from app.models.review import Review

class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.user = User(email='test@example.com', password='password123', first_name='John', last_name='Doe')
        self.city = City(name='New York', country_code='US')
        self.review = Review(user_id=self.user.id, place_id='123', rating=5, comment='Great place!')

    def test_save_user(self):
        self.user.save()
        retrieved_user = self.data_manager.get(self.user.id, 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], self.user.email)

    def test_get_user(self):
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.user.email)

    def test_update_user(self):
        self.user.save()
        self.user.email = 'newemail@example.com'
        self.user.save()
        retrieved_user = User.get(self.user.id)
        self.assertEqual(retrieved_user.email, 'newemail@example.com')

    def test_delete_user(self):
        self.user.save()
        self.user.delete()
        retrieved_user = User.get(self.user.id)
        self.assertIsNone(retrieved_user)

    def test_save_city(self):
        self.city.save()
        retrieved_city = self.data_manager.get(self.city.id, 'City')
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city['name'], self.city.name)

    def test_get_city(self):
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city.name, self.city.name)

    def test_update_city(self):
        self.city.save()
        self.city.name = 'Los Angeles'
        self.city.save()
        retrieved_city = City.get(self.city.id)
        self.assertEqual(retrieved_city.name, 'Los Angeles')

    def test_delete_city(self):
        self.city.save()
        self.city.delete()
        retrieved_city = City.get(self.city.id)
        self.assertIsNone(retrieved_city)

    def test_save_review(self):
        self.review.save()
        retrieved_review = self.data_manager.get(self.review.id, 'Review')
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review['comment'], self.review.comment)

    def test_get_review(self):
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.comment, self.review.comment)

    def test_update_review(self):
        self.review.save()
        self.review.comment = 'Updated review'
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertEqual(retrieved_review.comment, 'Updated review')

    def test_delete_review(self):
        self.review.save()
        self.review.delete()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNone(retrieved_review)

if __name__ == '__main__':
    unittest.main()
