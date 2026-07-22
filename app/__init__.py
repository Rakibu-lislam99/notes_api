from flask import Flask
from app import config
from app.extensions import db , jwt
from app.auth.routes import auth_bp
from app.errors.error_handlers import register_error_handlers

def create_app(testing=False):
    app = Flask(__name__)                     # create flask app
    app.config.from_object(config.Config)     # app configuration

    if testing:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    db.init_app(app)                         # database initialization
    jwt.init_app(app)


    app.register_blueprint(auth_bp , url_prefix='/auth')

    register_error_handlers(app)


    return app

