from flask_jwt_extended import jwt_required
from app import app
import repository
from flask import redirect, request, jsonify, render_template, session, url_for

# endpoint to sign up with email and password
@app.route('/sign_up', methods=['POST'])
def sign_up():
    data = request.get_json()
    email = data['email']
    password = data['password']
    if repository.sign_up(email, password):
        return jsonify({'message': 'success'})
    return jsonify({'message': 'failed'})

# endpoint to login with email and password
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    if token := repository.login(email, password):
        return jsonify({'token': token})
    
    return jsonify({'message': 'failed'})


# endpoint to get an openai summary of the top num reviews for a product
@app.route('/summary', methods=['GET'])
@jwt_required()
def summary():
    product_id = request.args.get('product_id')
    num = request.args.get('num', 10)
    return jsonify(repository.get_summary(product_id, num))
