from flask import Flask, jsonify
from flask_restx import Api
from .api.v1.endpoints import users, places, reviews, amenities, cities, countries

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API',
              description='A simple API for HBnB Evolution project')

    api.add_namespace(users.bp, path='/api/v1/users')
    api.add_namespace(places.bp, path='/api/v1/places')
    api.add_namespace(reviews.bp, path='/api/v1/reviews')
    api.add_namespace(amenities.bp, path='/api/v1/amenities')
    api.add_namespace(cities.bp, path='/api/v1/cities')
    api.add_namespace(countries.bp, path='/api/v1/countries')

    @app.route('/')
    def home():
        return jsonify(message="Welcome to the HBnB API")

    return app

app = create_app()
