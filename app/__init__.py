from flask import Flask ,request
from app import config
from app.extensions import db , jwt , migrate
from app.auth.routes import auth_bp
from app.errors.error_handlers import register_error_handlers
from app.logger import setup_logger


def create_app(testing=False):
    app = Flask(__name__)                     # create flask app
    app.config.from_object(config.Config)     # app configuration

    if testing:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    db.init_app(app)                         # database initialization
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp , url_prefix='/auth')

    @app.before_request
    def log_request():
        app.logger.info(
            f"{request.method} {request.path} | {request.remote_addr}"
        )
    @app.after_request
    def log_response(response):
        app.logger.info(
            f"{request.method} {request.path} -> {response.status_code}"
        )
    register_error_handlers(app)
    setup_logger(app)

    return app

