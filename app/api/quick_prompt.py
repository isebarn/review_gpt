from flask import Flask
from flask_jwt_extended import JWTManager
from models import QuickPrompt
from flask_restx import Namespace, Resource, fields
from models import model_to_field

api = Namespace('quick_prompt', description='quick prompt')

# a quick prompt has id, prompt, name, description
quick_prompt = api.model('QuickPrompt', model_to_field(QuickPrompt))

@api.route('/')
class QuickPromptController(Resource):
    # get method to get all quick prompts
    @api.marshal_list_with(quick_prompt)
    def get(self):
        """Get all quick prompts"""
        asd = QuickPrompt.query.all()
        return QuickPrompt.query.all()