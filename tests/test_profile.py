



def test_profile_requires_login(client):
    response = client.get('/auth/profile')

    assert response.status_code == 401

def test_profile_success(client , login_headers):
    response = client.get(
        '/auth/profile' ,
        headers=login_headers
    )

    assert response.status_code == 200







