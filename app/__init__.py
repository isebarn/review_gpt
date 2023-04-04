# flask app
import json
from flask import Flask
from flask_cors import CORS
from models import db
from app.logic.commands.authentication import bcrypt
from app.logic.commands.authentication import jwt
from config import Config
from app.api import api


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    api.init_app(app)
    CORS(app)

    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    from models import User, Product, Review, ReviewSummary, ProductMessage, QuickPrompt
    admin = Admin(app, name='Data', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Review, db.session))
    admin.add_view(ModelView(ReviewSummary, db.session))
    admin.add_view(ModelView(ProductMessage, db.session))   
    admin.add_view(ModelView(QuickPrompt, db.session))

    with app.app_context():
        db.create_all()

        with open("seed.json", "r") as f:
            data = json.load(f)
            for name, quick_prompt in data['quick_prompt'].items():
                # check if a prompt with the same name already exists, if not, create it
                if not QuickPrompt.query.filter_by(name=name).first():
                    db.session.add(QuickPrompt(
                        name=name,
                        prompt=quick_prompt["prompt"], 
                        description=quick_prompt["description"])
                    )
                    

        db.session.commit()
    
    return app