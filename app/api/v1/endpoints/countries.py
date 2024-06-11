from flask import Blueprint, jsonify
from app.models.country import Country

bp = Blueprint('countries', __name__, url_prefix='/countries')

@bp.route('/', methods=['GET'])
def get_countries():
    countries = Country.get_all()
    return jsonify([country.to_dict() for country in countries])

@bp.route('/<country_code>', methods=['GET'])
def get_country(country_code):
    country = Country.get(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.to_dict())
