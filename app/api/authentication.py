from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User
from flask_restx import Namespace, Resource, fields
from app.logic.commands.authentication import sign_up
from app.logic.commands.authentication import login

api = Namespace('authentication', description='Authentication related operations')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password'),
})

signup = api.model('Signup', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password'),
})

user = api.model('User', {
    'email': fields.String(required=True, description='The user email'),
    'id': fields.Integer(required=True, description='The user id'),
})

user_response = api.model('UserResponse', {
    'user': fields.Nested(user, description='The user'),
})

@api.route('/login')
class Login(Resource):
    @api.doc('login')
    @api.expect(login_model)
    def post(self):
        data = api.payload
        email = data['email']
        password = data['password']
        if token := login(email, password):
            return {'token': token}
        
        return {'message': 'failed'}
    
@api.route('/signup')
class Signup(Resource):
    @api.doc('signup')
    @api.expect(signup)
    def post(self):
        data = api.payload
        email = data['email']
        password = data['password']
        if sign_up(email, password):
            return {'message': 'success'}
        return {'message': 'failed'}
        
@api.route('/user')
class UserController(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_response)
    @jwt_required()
    def get(self):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        return {'user': user}