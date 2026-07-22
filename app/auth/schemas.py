from marshmallow import Schema, fields , validate , ValidationError
import re


def validate_uppercase(password):
    if not re.search(r'[A-Z]' , password):
        raise ValidationError('Password must contain at least one uppercase letter')

def validate_lowercase(password):
    if not re.search(r"[a-z]" , password):
        raise ValidationError('Password must contain at least one lowercase letter')

def validate_number(password):
    if not re.search(r"[0-9]" , password):
        raise ValidationError('Password must contain at least one number')


class LoginSchema(Schema):

    email = fields.Email(
        required=True,
        validate = validate.Length(min=3, max=100)
    )

    password = fields.String(
        required=True,
        validate=[
            validate.Length(min=8),
            validate_uppercase,
            validate_lowercase,
            validate_number
                  ]
    )


class RegisterSchema(Schema):

    email = fields.Email(
        required=True,
        validate = validate.Length(min=3, max=100)
    )


    password = fields.String(
        required=True,
    validate=[
        validate.Length(min=8),
        validate_uppercase,
        validate_lowercase,
        validate_number
    ]
    )

    username = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100)
    )