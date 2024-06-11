from flask import Blueprint, request, jsonify
from app.models.amenity import Amenity

bp = Blueprint('amenities', __name__, url_prefix='/amenities')

@bp.route('/', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = Amenity(name=data['name'])
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@bp.route('/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.to_dict())

@bp.route('/', methods=['GET'])
def get_amenities():
    amenities = Amenity.get_all()
    return jsonify([amenity.to_dict() for amenity in amenities])

@bp.route('/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = Amenity.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    data = request.get_json()
    amenity.name = data.get('name', amenity.name)
    amenity.save()
    return jsonify(amenity.to_dict())

@bp.route('/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = Amenity.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    amenity.delete()
    return '', 204
