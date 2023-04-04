from flask_restx import Api
from app.api.authentication import api as authentication
from app.api.product import api as product_api
from app.api.reviews import api as reviews_api
from app.api.serpapi import api as serpapi_api
from app.api.product_message import api as product_message_api
from app.api.openai import api as openai_api
from app.api.quick_prompt import api as quick_prompt_api

api = Api()

api.add_namespace(authentication)
api.add_namespace(product_api)
api.add_namespace(reviews_api)
api.add_namespace(serpapi_api)
api.add_namespace(product_message_api)
api.add_namespace(openai_api)
api.add_namespace(quick_prompt_api)