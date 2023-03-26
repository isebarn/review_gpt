# flask app
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

app.config['SERP_API_KEY'] = os.getenv("SERP_API_KEY")

# use sqlite for development
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# openapi config
app.config['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# bcrypt for password hashing
bcrypt = Bcrypt(app)

# enable CORS
CORS(app)

# jwt
app.config["JWT_SECRET_KEY"] = "samba" 
jwt = JWTManager(app)

import models, endpoints

if __name__ == '__main__':
    app.run(debug=True)