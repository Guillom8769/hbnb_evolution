from flask import Blueprint, request, jsonify
from app.models.place import Place

bp = Blueprint('places', __name__, url_prefix='/places')

@bp.route('/', methods=['POST'])
def create_place():
    data = request.get_json()
    place = Place(
        name=data['name'],
        description=data['description'],
        address=data['address'],
        city_id=data['city_id'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        host_id=data['host_id'],
        num_rooms=data['num_rooms'],
        num_bathrooms=data['num_bathrooms'],
        price_per_night=data['price_per_night'],
        max_guests=data['max_guests']
    )
    place.save()
    return jsonify(place.to_dict()), 201

@bp.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.to_dict())

@bp.route('/', methods=['GET'])
def get_places():
    places = Place.get_all()
    return jsonify([place.to_dict() for place in places])

@bp.route('/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = Place.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    data = request.get_json()
    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)
    place.address = data.get('address', place.address)
    place.city_id = data.get('city_id', place.city_id)
    place.latitude = data.get('latitude', place.latitude)
    place.longitude = data.get('longitude', place.longitude)
    place.host_id = data.get('host_id', place.host_id)
    place.num_rooms = data.get('num_rooms', place.num_rooms)
    place.num_bathrooms = data.get('num_bathrooms', place.num_bathrooms)
    place.price_per_night = data.get('price_per_night', place.price_per_night)
    place.max_guests = data.get('max_guests', place.max_guests)
    place.save()
    return jsonify(place.to_dict())

@bp.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    place.delete()
    return '', 204
