from flask_restx import Namespace, Resource, fields

amenities_api = Namespace('amenities', description='Amenities operations')

amenity_model = amenities_api.model('Amenity', {
    'id': fields.String(required=True, description='The amenity identifier'),
    'name': fields.String(required=True, description='The amenity name'),
})

@amenities_api.route('/')
class AmenityList(Resource):
    @amenities_api.doc('list_amenities')
    @amenities_api.marshal_list_with(amenity_model)
    def get(self):
        '''List all amenities'''
        return []  # Replace with actual implementation

    @amenities_api.doc('create_amenity')
    @amenities_api.expect(amenity_model)
    @amenities_api.marshal_with(amenity_model, code=201)
    def post(self):
        '''Create a new amenity'''
        return {}  # Replace with actual implementation

@amenities_api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @amenities_api.doc('get_amenity')
    @amenities_api.marshal_with(amenity_model)
    def get(self, amenity_id):
        '''Fetch an amenity given its identifier'''
        return {}  # Replace with actual implementation

    @amenities_api.doc('update_amenity')
    @amenities_api.expect(amenity_model)
    @amenities_api.marshal_with(amenity_model)
    def put(self, amenity_id):
        '''Update an amenity given its identifier'''
        return {}  # Replace with actual implementation

    @amenities_api.doc('delete_amenity')
    def delete(self, amenity_id):
        '''Delete an amenity given its identifier'''
        return '', 204  # Replace with actual implementation
