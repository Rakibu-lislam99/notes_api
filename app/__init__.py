from flask import Flask


def create_app(testing=False):
    app = Flask(__name__)


    if testing:
        app.config['TESTING'] = True

    @app.route('/' , methods=['GET'])
    def index():
        return {
            'message' : 'Hello World!'
        } , 200

    return app

