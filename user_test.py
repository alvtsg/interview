import pytest
import requests
from users import Users


def test_create_user():
    user = Users()
    user_data = {"name":"John Smith", "gender":"male", "email":"john.smith@example.com", "status":"active"}
    status_code, api_output = user.create_user(user_data)
    assert status_code in [200, 201]


def test_get_users():
    user = Users()
    status_code, api_output = user.get_users()
    assert status_code == 200
    # Test get user with ID
    user_id = api_output[0].get('id')
    status_code, api_output = user.get_users(user_id)
    assert status_code == 200


def test_update_user():
    user = Users()
    status_code, api_output = user.get_users()
    assert status_code == 200
    # Test get user with ID
    user_id = api_output[0].get('id')
    user_data = {"name":"Jane Doe", "gender":"female", "email":"jane.doe@example.com", "status":"active"}
    status_code = user.update_user(user_id, user_data)
    assert status_code == 200


def test_delete_user():
    user = Users()
    status_code, api_output = user.get_users()
    assert status_code == 200
    # Test get user with ID
    user_id = api_output[0].get('id')    
    try: 
        status_code = user.delete_user(user_id)
    except Exception:
        pass
    finally:
        print(f'final status code is {status_code}')
    assert status_code in [200, 204]


def test_http_code_401():
    user = Users(headers={'Authorization': 'Bearer 11111111'})
    user_data = {"name":"John Smith", "gender":"male", "email":"john.smith@example.com", "status":"active"}
    status_code, api_output = user.create_user(user_data)
    assert status_code == 401


def test_http_code_404():
    user = Users()
    # Provide a non-existent user id as input
    status_code, api_output = user.get_users(122111231423423)
    assert status_code == 404


def test_http_code_422():
    user = Users()
    user_data = {"_name":"John Smith", "_gender":"male", "_email":"john.smith@example.com", "_status":"active"}
    status_code, api_output = user.create_user(user_data)
    assert status_code == 422


def test_http_code_405():  
    test_url = 'https://gorest.co.in/public/v2/users'
    # Need to use TRACE method to trigger http code 405 - method not allowed
    req = requests.Request('TRACE', test_url)
    r = req.prepare()
    s = requests.Session()
    output = s.send(r)
    assert output.status_code == 405
