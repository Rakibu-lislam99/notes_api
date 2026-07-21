from flask import Blueprint , request
from marshmallow import ValidationError

from .service import AuthService
from .schemas import RegistrationSchema , LoginSchema


auth_bp = Blueprint('auth', __name__)



@auth_bp.route('/login' , methods=['POST'])
def login():
    schema = LoginSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return err.messages,401
    return AuthService.login(data)


@auth_bp.route('/logout')
def logout():
    pass

@auth_bp.route('/register'  , methods=['POST'])
def register():
    schema = RegistrationSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return err.messages,401
    return AuthService.register(data)


@auth_bp.route('/profile')
def profile():
    pass