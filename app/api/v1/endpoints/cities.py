from flask_restx import Namespace, Resource, fields

cities_api = Namespace('cities', description='Cities operations')

city_model = cities_api.model('City', {
    'id': fields.String(required=True, description='The city identifier'),
    'name': fields.String(required=True, description='The city name'),
    'description': fields.String(required=True, description='The city description'),
})

@cities_api.route('/')
class CityList(Resource):
    @cities_api.doc('list_cities')
    @cities_api.marshal_list_with(city_model)
    def get(self):
        '''List all cities'''
        return []  # Replace with actual implementation

    @cities_api.doc('create_city')
    @cities_api.expect(city_model)
    @cities_api.marshal_with(city_model, code=201)
    def post(self):
        '''Create a new city'''
        return {}  # Replace with actual implementation

@cities_api.route('/<string:city_id>')
class CityResource(Resource):
    @cities_api.doc('get_city')
    @cities_api.marshal_with(city_model)
    def get(self, city_id):
        '''Fetch a city given its identifier'''
        return {}  # Replace with actual implementation

    @cities_api.doc('update_city')
    @cities_api.expect(city_model)
    @cities_api.marshal_with(city_model)
    def put(self, city_id):
        '''Update a city given its identifier'''
        return {}  # Replace with actual implementation

    @cities_api.doc('delete_city')
    def delete(self, city_id):
        '''Delete a city given its identifier'''
        return '', 204  # Replace with actual implementation
