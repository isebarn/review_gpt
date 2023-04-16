from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.logic.commands.reviews import get_reviews, post_reviews
from models import User
from flask_restx import Namespace, Resource, fields



api = Namespace('reviews', description='reviews')

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

# a review has title, avatar, rating, snippet, likes, date
review = api.model('Review', {
    'id': fields.Integer(required=True, description='id'),
    'title': fields.String(required=True, description='title'),
    'avatar': fields.String(required=True, description='avatar'),
    'rating': fields.String(required=True, description='rating'),
    'snippet': fields.String(required=True, description='snippet'),
    'likes': fields.String(required=True, description='likes'),
    'date': fields.DateTime(required=True, description='date'),
    "answer": fields.String(required=True, description='answer'),
    "sentiment": fields.Float(required=False, description='sentiment')
})


# endpoint that accepts a product_id in the query string and returns a list of reviews
@api.route('/<string:product_id>')
class Reviews(Resource):
    @api.expect(product)
    @api.marshal_list_with(review)
    @jwt_required()
    def get(self, product_id):
        """Get data from google search reviews"""
        user = User.query.filter_by(email=get_jwt_identity()).first()        
        return get_reviews(user, product_id)

    # save a list of review objects to the database
    @api.marshal_list_with(review)
    @jwt_required()
    def post(self, product_id):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        reviews = post_reviews(user, product_id, request.json)
        return reviews