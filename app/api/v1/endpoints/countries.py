from flask_restx import Namespace, Resource, fields

countries_api = Namespace('countries', description='Countries operations')

country_model = countries_api.model('Country', {
    'id': fields.String(required=True, description='The country identifier'),
    'name': fields.String(required=True, description='The country name'),
})

@countries_api.route('/')
class CountryList(Resource):
    @countries_api.doc('list_countries')
    @countries_api.marshal_list_with(country_model)
    def get(self):
        '''List all countries'''
        return []  # Replace with actual implementation

    @countries_api.doc('create_country')
    @countries_api.expect(country_model)
    @countries_api.marshal_with(country_model, code=201)
    def post(self):
        '''Create a new country'''
        return {}  # Replace with actual implementation

@countries_api.route('/<string:country_id>')
class CountryResource(Resource):
    @countries_api.doc('get_country')
    @countries_api.marshal_with(country_model)
    def get(self, country_id):
        '''Fetch a country given its identifier'''
        return {}  # Replace with actual implementation

    @countries_api.doc('update_country')
    @countries_api.expect(country_model)
    @countries_api.marshal_with(country_model)
    def put(self, country_id):
        '''Update a country given its identifier'''
        return {}  # Replace with actual implementation

    @countries_api.doc('delete_country')
    def delete(self, country_id):
        '''Delete a country given its identifier'''
        return '', 204  # Replace with actual implementation
