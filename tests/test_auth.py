


def test_register_successfully_creates_user(client , clean_database):

    response = client.post(
        '/auth/register' ,
        json = {
            'email' : 'rakib@gmail.com' ,
            'password' : 'Password@123' ,
            'username' : 'rakib'
        }
    )

    assert response.status_code == 201


def test_register_duplicate_email(client , user):
    response = client.post(
        '/auth/register' ,
        json = {
            'email' : 'rakib@gmail.com' ,
            'password' : 'Password@123'
        }
    )

    assert response.status_code == 409


def test_login_successfully(client , user):
    response = client.post(
        '/auth/login' ,
        json = {
            'email' : "rakib@gmail.com",
            'password' : 'Password@123'
        }
    )

    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_wrong_password(client , user):
    response = client.post(
        '/auth/login' ,
        json = {
            'email' : 'rakib123@gmail.com',
            'password' : 'WrongPassword'
        }
    )

    assert response.status_code == 401














