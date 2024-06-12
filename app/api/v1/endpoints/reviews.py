from flask_restx import Namespace, Resource, fields

reviews_api = Namespace('reviews', description='Reviews operations')

review_model = reviews_api.model('Review', {
    'id': fields.String(required=True, description='The review identifier'),
    'text': fields.String(required=True, description='The review text'),
    'rating': fields.Integer(required=True, description='The review rating'),
})

@reviews_api.route('/')
class ReviewList(Resource):
    @reviews_api.doc('list_reviews')
    @reviews_api.marshal_list_with(review_model)
    def get(self):
        '''List all reviews'''
        return []  # Replace with actual implementation

    @reviews_api.doc('create_review')
    @reviews_api.expect(review_model)
    @reviews_api.marshal_with(review_model, code=201)
    def post(self):
        '''Create a new review'''
        return {}  # Replace with actual implementation

@reviews_api.route('/<string:review_id>')
class ReviewResource(Resource):
    @reviews_api.doc('get_review')
    @reviews_api.marshal_with(review_model)
    def get(self, review_id):
        '''Fetch a review given its identifier'''
        return {}  # Replace with actual implementation

    @reviews_api.doc('update_review')
    @reviews_api.expect(review_model)
    @reviews_api.marshal_with(review_model)
    def put(self, review_id):
        '''Update a review given its identifier'''
        return {}  # Replace with actual implementation

    @reviews_api.doc('delete_review')
    def delete(self, review_id):
        '''Delete a review given its identifier'''
        return '', 204  # Replace with actual implementation
