from flask import Blueprint, request, jsonify
from app.models.review import Review

bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(
        user_id=data['user_id'],
        place_id=data['place_id'],
        rating=data['rating'],
        comment=data['comment']
    )
    review.save()
    return jsonify(review.to_dict()), 201

@bp.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.to_dict())

@bp.route('/', methods=['GET'])
def get_reviews():
    reviews = Review.get_all()
    return jsonify([review.to_dict() for review in reviews])

@bp.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    data = request.get_json()
    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    review.save()
    return jsonify(review.to_dict())

@bp.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    review.delete()
    return '', 204
