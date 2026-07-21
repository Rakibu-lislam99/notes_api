from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.models import db

class AuthService:


    @staticmethod
    def login(data):
        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                return {'message': 'Login Successfully'}, 200
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
            }












