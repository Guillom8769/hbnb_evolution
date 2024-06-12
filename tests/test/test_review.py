import unittest
from app.models.review import Review

class ReviewModelTestCase(unittest.TestCase):
    def setUp(self):
        self.review = Review(
            user_id="user_1",
            place_id="place_1",
            rating=5,
            text="Great place!"
        )

    def test_save_and_get_review(self):
        self.review.save()
        saved_review = Review.get(self.review.id)
        self.assertIsNotNone(saved_review)
        self.assertEqual(saved_review.id, self.review.id)
        self.assertEqual(saved_review.text, "Great place!")

    def test_update_review(self):
        self.review.save()
        self.review.text = "Updated review"
        self.review.save()
        updated_review = Review.get(self.review.id)
        self.assertEqual(updated_review.text, "Updated review")

    def test_delete_review(self):
        self.review.save()
        self.review.delete()
        deleted_review = Review.get(self.review.id)
        self.assertIsNone(deleted_review)

    def test_get_all_reviews(self):
        self.review.save()
        reviews = Review.get_all()
        self.assertGreaterEqual(len(reviews), 1)

if __name__ == '__main__':
    unittest.main()
