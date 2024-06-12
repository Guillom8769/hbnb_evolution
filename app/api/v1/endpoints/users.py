from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.user import User

user_ns = Namespace('users', description='User operations')

user_model = user_ns.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'email': fields.String(required=True, description='The user email'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        '''List all users'''
        users = User.get_all()
        return users

    @user_ns.doc('create_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        '''Create a new user'''
        data = request.get_json()
        user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
        user.save()
        return user, 201

@user_ns.route('/<string:user_id>')
class UserResource(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        '''Fetch a user given its identifier'''
        user = User.get(user_id)
        if not user:
            user_ns.abort(404, "User not found")
        return user

    @user_ns.doc('update_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        '''Update a user given its identifier'''
        user = User.get(user_id)
        if not user:
            user_ns.abort(404, "User not found")
        data = request.get_json()
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.save()
        return user

    @user_ns.doc('delete_user')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        user = User.get(user_id)
        if not user:
            user_ns.abort(404, "User not found")
        user.delete()
        return '', 204
