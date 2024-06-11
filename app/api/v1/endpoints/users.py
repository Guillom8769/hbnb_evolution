from flask import Blueprint, request, jsonify
from app.models.user import User

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    user.save()
    return jsonify(user.to_dict()), 201

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())

@bp.route('/', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.save()
    return jsonify(user.to_dict())

@bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user.delete()
    return '', 204
