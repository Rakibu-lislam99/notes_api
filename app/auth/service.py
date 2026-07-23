from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token
from flask import  current_app


class AuthService:


    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                token = create_access_token(identity=user.user_id)
                return {
                    'message': 'Login Successfully',
                    'access_token' : token
                    }, 200
            else:
                current_app.logger.info(
                    f"Invalid login attempt: {user.email}"
                )
                return {"message": 'Invalid Credentials'}, 401
        else:
            return {'message': 'No user found'}, 401


    @staticmethod
    def register(data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            current_app.logger.info(
                f"Duplicate registration attempt: {user.email}"
            )
            return {
                'message': 'Invalid Credentials'
            }, 409
        else:
            user = User(
                email=email,
                username=username,
                password=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()
            current_app.logger.info(
                f"New user created: {user.email}"
            )
            return {
                'message': 'User created successfully'
            } , 201

    @staticmethod
    def profile(user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            return {
                'message' : 'User found' ,
                'user_id' : user.id ,
                'email' : user.email,
                'username' : user.username
            }
        return {
            'message' : 'Invalid Credentials'
        }, 401










