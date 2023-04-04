from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User
from flask_restx import Namespace, Resource, fields
from app.logic.queries.product import get_products
from app.logic.commands.product import post_product

api = Namespace('product', description='product search')

# product has title, link, product_id, serpapi_link, rating, author, video and thumbnail
product = api.model('Product', {
    'id': fields.Integer(required=True, description='id'),
    'title': fields.String(required=True, description='title'),
    'link': fields.String(required=True, description='link'),
    'product_id': fields.String(required=True, description='product_id'),
    'serpapi_link': fields.String(required=True, description='serpapi_link'),
    'rating': fields.String(required=True, description='rating'),
    'author': fields.String(required=True, description='author'),
    'video': fields.String(required=True, description='video'),
    'thumbnail': fields.String(required=True, description='thumbnail')
})

@api.route('')
class Product(Resource):
    @api.marshal_list_with(product)
    @jwt_required()
    def get(self):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        products = get_products(user)

        return products

    @api.expect(product)
    @api.marshal_with(product)
    @jwt_required()
    def post(self):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        product = post_product(user, request.json)

        return product
    
