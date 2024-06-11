import unittest
import os
import json
from app.models.review import Review
from app.persistence.data_manager import DataManager

class ReviewModelTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.test_file = self.data_manager.file_path
        self.review = Review(
            user_id="user123",
            place_id="place123",
            rating=5,
            comment="Great place!"
        )

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_review(self):
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.comment, self.review.comment)

    def test_update_review(self):
        self.review.save()
        self.review.comment = "Updated comment"
        self.review.save()
        retrieved_review = Review.get(self.review.id)
        self.assertEqual(retrieved_review.comment, "Updated comment")

    def test_delete_review(self):
        self.review.save()
        self.review.delete()
        retrieved_review = Review.get(self.review.id)
        self.assertIsNone(retrieved_review)

    def test_get_all_reviews(self):
        self.review.save()
        another_review = Review(
            user_id="user456",
            place_id="place456",
            rating=4,
            comment="Nice place"
        )
        another_review.save()
        reviews = Review.get_all()
        self.assertEqual(len(reviews), 2)

if __name__ == '__main__':
    unittest.main()
