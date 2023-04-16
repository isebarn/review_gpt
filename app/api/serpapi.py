from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User
from flask_restx import Namespace, Resource, fields
from flask_restx import reqparse
from app.logic.clients.serpapi import search_product
from app.logic.queries.product import get_product
from app.logic.clients.serpapi import get_reviews



api = Namespace('serpapi', description='serpapi search')

# product has title, link, product_id, serpapi_link, rating, author, video and thumbnail
product = api.model('Product', {
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
    'title': fields.String(required=True, description='title'),
    'avatar': fields.String(required=True, description='avatar'),
    'rating': fields.String(required=True, description='rating'),
    'snippet': fields.String(required=True, description='snippet'),
    'likes': fields.String(required=True, description='likes'),
    'date': fields.String(required=True, description='date'),
    'sentiment': fields.Float(required=False, description='sentiment')
})


parser = reqparse.RequestParser()
parser.add_argument('search', type=str, required=True, help='product is required')

# endpoint that accepts a product in the query string and returns a list of items
@api.route('/products')
class Search(Resource):
    @api.expect(parser)
    @api.marshal_list_with(product)
    @jwt_required()
    def get(self):
        """Search for a product on google play"""
        # get the product from the query string
        args = parser.parse_args()
        search = args.get('search')
        
        # search for the product on google play
        results = search_product(search)
        return results['organic_results'][0]['items']
    

# endpoint that accepts a product_id in the query string and returns a list of reviews
@api.route('/reviews/<string:product_id>')
class Reviews(Resource):
    @api.expect(product)
    @api.marshal_list_with(review)
    @jwt_required()
    def get(self, product_id):
        """Get data from google search reviews"""
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if product := get_product(user, product_id):
            asd = get_reviews(product.product_id).get('reviews', [])
            return asd

        return {'message': 'product is required'}, 400
        


