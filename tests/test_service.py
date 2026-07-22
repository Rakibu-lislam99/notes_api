from app.auth.service import AuthService

def test_register_service_creates_user(app , client):

    with app.app_context():

        response = AuthService.register(
            {
                'username' : 'Rakib',
                'email' : 'rakib@gmail.com',
                'password' : 'Password@123'
            }
        )

        assert response[1] == 201