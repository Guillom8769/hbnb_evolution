from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    from .api.v1.endpoints import users, places, reviews, amenities, cities, countries
    app.register_blueprint(users.bp)
    app.register_blueprint(places.bp)
    app.register_blueprint(reviews.bp)
    app.register_blueprint(amenities.bp)
    app.register_blueprint(cities.bp)
    app.register_blueprint(countries.bp)

    # Root route
    @app.route('/')
    def home():
        return jsonify(message="Welcome to the HBnB API")

    return app

app = create_app()

if __name__ == "__main__":
    print("Starting the HBnB API server...")
    app.run(host="0.0.0.0", port=5000)
