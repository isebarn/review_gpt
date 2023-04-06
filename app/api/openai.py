from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User
from flask_restx import Namespace, Resource, fields
from app.logic.clients.openai import summarize_reviews
from app.logic.clients.openai import answer_reviews

api = Namespace('openai')

prompt = api.model('Prompt', {
    'prompt': fields.String(required=True, description='prompt'),
})

@api.route('/<string:product_id>')
class SummaryController(Resource):
    @api.expect(prompt)
    @jwt_required()
    def post(self, product_id):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        return summarize_reviews(user, product_id, request.json['prompt'])

review_answer = api.model('ReviewAnswer', {
    'id': fields.Integer(required=True, description='id'),
    'title': fields.String(required=True, description='title'),
    'avatar': fields.String(required=True, description='avatar'),
    'rating': fields.String(required=True, description='rating'),
    'snippet': fields.String(required=True, description='snippet'),
    'likes': fields.String(required=True, description='likes'),
    'date': fields.String(required=True, description='date'),
    "answer": fields.String(required=True, description='answer')
})    

# Path answer_reviews accepts a list of reviews and returns an answer
@api.route('/answer_reviews')
class AnswerReviewsController(Resource):
    @api.marshal_list_with(review_answer)
    @jwt_required()
    def post(self):
        # get the review ids from the request
        reviews = request.json

        return answer_reviews(reviews)