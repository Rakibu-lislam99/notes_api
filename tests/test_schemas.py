from app.auth.schemas import RegisterSchema
from marshmallow import ValidationError
import pytest

def test_register_schema_valid():
    schema = RegisterSchema()
    data = schema.load(
        {
            'username' : 'Rakib' ,
            'email' : 'rakib@gmail.com',
            'password' : 'Password@123'
        }
    )

    assert data['username'] == 'Rakib'


def test_register_schema_invalid_email():
    schema = RegisterSchema()

    with pytest.raises(ValidationError):
        schema.load(
            {
                'username' : 'Rakib' ,
                'email' : 'abc' ,
                'password' : 'Password@123'
            }
        )
