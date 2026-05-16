from pages.login_page import LoginPage
from utils.config import BASE_URL, EMAIL, PASSWORD
import pytest
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(driver):

    logger.info("Starting valid login test")

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login(EMAIL, PASSWORD)

    assert "Logged in as" in (
        login.get_logged_in_text()
    )

@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(driver):

    logger.info("Starting invalid login test")

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login(
        "wrong@gmail.com",
        "wrong123"
    )

    assert "incorrect" in (
        login.get_error_message()
    )

