from models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from app.logic.commands.product import db
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()

def sign_up(email, password):
    # check if the email is already in the database
    user = User.query.filter_by(email=email).first()
    if user:
        return False
    
    # check if the email is a valid email string
    if not email or '@' not in email:
        return False
    
    # check if the password is a valid password string
    if not password or len(password) < 6:
        return False
    
    # hash the password
    password = bcrypt.generate_password_hash(password).decode('utf-8')

    # if the email is not in the database, add the user to the database
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return True

# login with email and password and return a jwt token
def login(email, password):
    # check if the email is in the database
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    
    # check if the password is correct
    if bcrypt.check_password_hash(user.password, password):
        return create_access_token(identity=user.email)
    return False