from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import User
from app.models.models import db
from flask_jwt_extended import create_access_token



class AuthService:


    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                token = create_access_token(identity=user.id)
                return {
                    'message': 'Login Successfully',
                    'access_token' : token
                    }, 200
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
            return {
                'message': 'User already exists'
            }, 401
        else:
            user = User(
                email=email,
                username=username,
                password=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()
            return {
                'message': 'User created successfully'
            } , 201

    @staticmethod
    def profile(data):
        user_id = data.get('user_id')
        user = User.query.filter_by(id=user_id).first()
        if user:
            return {
                'message' : 'User found' ,
                'user_id' : user.id ,
                'email' : user.email,
                'username' : user.username
            }
        return {
            'message' : 'User not found'
        }










