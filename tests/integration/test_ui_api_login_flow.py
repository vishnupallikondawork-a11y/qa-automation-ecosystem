import pytest
from utils.config import BASE_URL
from pages.login_page import LoginPage
from test_data.login_data import VALID_USER
from api_clients.auth_api import AuthAPI
from utils.api_utils import APIUtils


@pytest.mark.integration
@pytest.mark.regression

def test_ui_api_login_flow(driver):

    #UI Login

    driver.get(BASE_URL)
    login_page = LoginPage(driver)

    login_page.login(
        VALID_USER["email"],
        VALID_USER["password"]
    )

    assert "Logged in as" in (
        login_page.get_logged_in_text()
    )

    # API Validation

    auth_api = AuthAPI()
    response = auth_api.login(
        VALID_USER["email"],
        VALID_USER["password"]
    )
    response_body = response.json()
    APIUtils.validate_status_code(
        response,
        200
    )
    APIUtils.validate_response_code(
        response_body,
        200
    )