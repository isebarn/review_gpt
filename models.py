# sqlalchemy models for user and prompt tables
from app import db, app
from dataclasses import dataclass

@dataclass
class User(db.Model):
    id: int
    password: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# model for google app reviews. We have App, Review and Prompt tables
@dataclass
class App(db.Model):
    id: int
    package_name: str

    id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(80), nullable=False)

@dataclass
class Review(db.Model):
    id: int
    app_id: int
    review: str

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('app.id'), nullable=False)
    review = db.Column(db.String(500), nullable=False)

@dataclass
class ReviewSummary(db.Model):
    id: int
    app_id: int
    summary: str

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('app.id'), nullable=False)
    summary = db.Column(db.String(5000), nullable=False)


# create the database tables
with app.app_context():
    db.create_all()

    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    admin = Admin(app, name='Data', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(App, db.session))
    admin.add_view(ModelView(Review, db.session))
    admin.add_view(ModelView(ReviewSummary, db.session))
