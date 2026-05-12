from api_clients.auth_api import AuthAPI
from utils.config import EMAIL, PASSWORD
from test_data.login_data import (VALID_USER, INVALID_USER)
import pytest
import json

@pytest.mark.api
@pytest.mark.smoke

def test_valid_login_api():
    auth = AuthAPI()

    response = auth.login(
        VALID_USER["email"],
        VALID_USER["password"]
    )
    

    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    assert response_body["responseCode"] == 200
    assert response_body["message"] == 'User exists!'


@pytest.mark.api
@pytest.mark.regression

def test_invalid_login_api():
    auth = AuthAPI()

    response = auth.login(
        INVALID_USER["email"],
        INVALID_USER["password"]
    )
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    assert response_body["responseCode"] == 404
    assert response_body["message"] == 'User not found!'

