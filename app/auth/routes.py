from flask import Blueprint , request
from .service import AuthService
from .schemas import RegisterSchema , LoginSchema
from flask_jwt_extended import jwt_required , get_jwt_identity


auth_bp = Blueprint('auth', __name__)



@auth_bp.route('/login' , methods=['POST'])
def login():
    schema = LoginSchema()
    data = schema.load(request.get_json())
    return AuthService.login(data)


@auth_bp.route('/logout')
def logout():
    pass

@auth_bp.route('/register'  , methods=['POST'])
def register():
    schema = RegisterSchema()
    data = schema.load(request.get_json())
    return AuthService.register(data)


@auth_bp.route('/profile')
@jwt_required()
def profile():
    user_id  = get_jwt_identity()
    return AuthService.profile(user_id)