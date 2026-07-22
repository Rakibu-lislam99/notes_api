from flask import Flask
from . import config
from .extensions import db , jwt
from .auth.routes import auth_bp
from app.errors.error_handlers import register_error_handlers

def create_app(testing=False):
    app = Flask(__name__)                     # create flask app
    app.config.from_object(config.Config)     # app configuration

    db.init_app(app)                         # database initialization
    jwt.init_app(app)

    if testing:
        app.config['TESTING'] = True

    app.register_blueprint(auth_bp , url_prefix='/auth')

    register_error_handlers(app)


    with app.app_context():
        db.create_all()

    return app

