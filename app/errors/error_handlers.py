from marshmallow import ValidationError
from flask import jsonify


def register_error_handlers(app):


    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            'errors' : error.messages
        }) , 400