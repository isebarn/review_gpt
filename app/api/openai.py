from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User
from flask_restx import Namespace, Resource, fields
from app.logic.clients.openai import summarize_reviews

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
