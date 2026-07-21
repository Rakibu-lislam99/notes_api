from flask import Blueprint , request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.extensions import db
from service import AuthService

auth_bp = Blueprint('auth', __name__)



@auth_bp.route('/login' , methods=['POST'])
def login():
    data = request.get_json()
    return AuthService.login(data)


@auth_bp.route('/logout')
def logout():
    pass

@auth_bp.route('/register'  , methods=['POST'])
def register():
    data = request.get_json()
    return AuthService.register(data)


@auth_bp.route('/profile')
def profile():
    pass