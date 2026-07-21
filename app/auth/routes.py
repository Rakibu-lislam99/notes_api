from flask import Blueprint , request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.extensions import db


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login' , methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password , password):
            return {'message': 'Login Successfull'} , 200
        return None
    else:
        return {'message': 'No user found'} , 401

@auth_bp.route('/logout')
def logout():
    pass

@auth_bp.route('/register'  , methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        return {
            'message': 'User already exists'
        } , 401
    else:
        user = User(
            email = email,
            username = username,
            password = generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return {
            'message': 'User created successfully'
        }


@auth_bp.route('/profile')
def profile():
    pass