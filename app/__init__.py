from flask import Flask
from . import config
from .extensions import db



def create_app(testing=False):
    app = Flask(__name__)                     # create flask app
    app.config.from_object(config.Config)     # app configuration

    db.init_app(app)                         # database initialization

    if testing:
        app.config['TESTING'] = True

    @app.route('/' , methods=['GET'])      # basic route
    def index():
        return {
            'message' : 'Hello World!'
        } , 200

    with app.app_context():
        db.create_all()

    return app

