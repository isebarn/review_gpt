# sqlalchemy models for user and prompt tables
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from flask_restx import fields
db = SQLAlchemy()
Base = declarative_base()

from dataclasses import dataclass

@dataclass
class User(db.Model):
    id: int
    password: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# model for google app, it has 
# a title, link, product_id, serpapi_link, rating, author, video, thumbnail and a user_id
@dataclass
class Product(db.Model):
    id: int
    title: str
    link: str
    product_id: str
    serpapi_link: str
    rating: str
    author: str
    video: str
    thumbnail: str
    user_id: int

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    product_id = db.Column(db.String(500), nullable=False)
    serpapi_link = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(500), nullable=False)
    video = db.Column(db.String(500), nullable=False)
    thumbnail = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # product_id and user_id are unique together
    __table_args__ = (db.UniqueConstraint('product_id', 'user_id', name='_product_user_uc'),)
    

# review has avatar, date, likes, rating, snippet, title, and an product_id
@dataclass
class Review(db.Model):
    id: int
    product_id: int
    review_id: str
    avatar: str
    date: str
    likes: str
    rating: str
    snippet: str
    title: str
    answer: str

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    review_id = db.Column(db.String(500), nullable=False)
    avatar = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(500), nullable=False)
    likes = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.String(500), nullable=False)
    snippet = db.Column(db.String(5000), nullable=False)
    title = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(5000), nullable=True)

    # review_id and product_id are unique together
    __table_args__ = (db.UniqueConstraint('review_id', 'product_id', name='_review_product_uc'),)

@dataclass
class ReviewSummary(db.Model):
    id: int
    product_id: int
    summary: str

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    summary = db.Column(db.String(5000), nullable=False)

@dataclass
class ProductMessage(db.Model):
    id: int
    product_id: int
    message: str
    date: datetime
    from_user: bool

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    message = db.Column(db.String(5000), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    from_user = db.Column(db.Boolean, nullable=False, default=False)

@dataclass
class QuickPrompt(db.Model):
    id: int
    name: str
    prompt: str
    description: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    prompt = db.Column(db.String(5000), nullable=False)
    description = db.Column(db.String(5000), nullable=False)


# method that converts models to flask_restx field models
# int becomes fields.Integer
# str becomes fields.String
# datetime becomes fields.DateTime
# bool becomes fields.Boolean
def model_to_field(model):
    field_model = {}
    for key, value in model.__dataclass_fields__.items():
        if key != '_':
            if value.type == int:
                field_model[key] = fields.Integer
            elif value.type == str:
                field_model[key] = fields.String
            elif value.type == datetime:
                field_model[key] = fields.DateTime
            elif value.type == bool:
                field_model[key] = fields.Boolean
    
    return field_model



""" # create the database tables
with app.app_context():
    db.create_all()

    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    admin = Admin(app, name='Data', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(App, db.session))
    admin.add_view(ModelView(Review, db.session))
    admin.add_view(ModelView(ReviewSummary, db.session))
 """