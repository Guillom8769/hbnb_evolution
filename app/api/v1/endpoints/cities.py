from flask import Blueprint, request, jsonify
from app.models.city import City

bp = Blueprint('cities', __name__, url_prefix='/cities')

@bp.route('/', methods=['POST'])
def create_city():
    data = request.get_json()
    city = City(name=data['name'], country_code=data['country_code'])
    city.save()
    return jsonify(city.to_dict()), 201

@bp.route('/<city_id>', methods=['GET'])
def get_city(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict())

@bp.route('/', methods=['GET'])
def get_cities():
    cities = City.get_all()
    return jsonify([city.to_dict() for city in cities])

@bp.route('/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    data = request.get_json()
    city.name = data.get('name', city.name)
    city.country_code = data.get('country_code', city.country_code)
    city.save()
    return jsonify(city.to_dict())

@bp.route('/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    city.delete()
    return '', 204
