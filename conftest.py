import pytest
from selenium import webdriver
import os
from datetime import datetime
from utils.execution_context import get_execution_timestamp

RUN_FOLDER = (
    f"test_runs/{get_execution_timestamp()}"
)

SCREENSHOT_FOLDER = (
    f"{RUN_FOLDER}/screenshots"
)

LOG_FOLDER = (
    f"{RUN_FOLDER}/logs"
)

REPORT_FOLDER = (
    f"{RUN_FOLDER}/reports"
)

os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed: 
        driver = item.funcargs.get("driver")

        if driver:

            # create screenshots folder
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            # unique name
            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"{SCREENSHOT_FOLDER}/{test_name}_{timestamp}.png"

            driver.save_screenshot(file_name)

# def pytest_configure(config):

#     report_path = (
#         f"{REPORT_FOLDER}/report.html"
#     )

#     config.option.htmlpath = report_path