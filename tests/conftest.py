import pytest
from app import create_app
from app.extensions import db
from app.models.models import User
from werkzeug.security import generate_password_hash



@pytest.fixture(scope='session')
def app():
    app = create_app(testing = True)

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def clean_database(app):
    with app.app_context():
        db.session.query(User).delete()
        db.session.commit()

        yield

        db.session.query(User).delete()
        db.session.commit()

@pytest.fixture
def user(app , clean_database):
    with app.app_context():
        user = User(
            username = 'rakib',
            email = 'rakib@gmail.com',
            password = generate_password_hash('Password@123')
        )
        db.session.add(user)
        db.session.commit()

        return user

@pytest.fixture
def login_headers(client , user):
    response = client.post(
        '/auth/login' ,
        json = {
            'email' : 'rakib@gmail.com' ,
            'password' : "Password@123"
        }
    )
    token = response.json['access_token']

    return {
        'Authorization' : f'Bearer {token}'
    }









