from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.logic.commands.product_message import get_product_messages, post_product_message
from models import User, ProductMessage, Product
from flask_restx import Namespace, Resource, fields

api = Namespace('product_message', description='product search')

# a message has id, product_id, message, date, from_user
message = api.model('Message', {
    'id': fields.Integer(required=True, description='id'),
    'product_id': fields.String(required=True, description='product_id'),
    'message': fields.String(required=True, description='message'),
    'date': fields.String(required=True, description='date'),
    'from_user': fields.Boolean(required=True, description='from_user')
})

@api.route('/<string:product_id>')
class ProductMessage(Resource):
    @api.marshal_list_with(message)
    @jwt_required()
    def get(self, product_id):
        """Get all product messages"""
        user = User.query.filter_by(email=get_jwt_identity()).first()
        return get_product_messages(user, product_id)

    @api.expect(message)
    @api.marshal_list_with(message)
    @jwt_required()
    def post(self, product_id):
        """Create a new product message"""
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if product := Product.query.filter_by(id=product_id, user_id=user.id).first():
            return post_product_message(product, request.json)

