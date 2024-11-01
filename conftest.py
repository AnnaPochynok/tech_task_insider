import pytest
from src.ui.utils.browser_setup import setup_browser
from src.api.client.api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on: chrome or firefox"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def driver(request, browser):
    driver = setup_browser(browser)
    yield driver
    if request.node.session.Failed:
        test_name = request.node.name
        driver.save_screenshot(f"screenshots/{test_name}_failure_screenshot.png")
        print(f"Screenshot saved for failed test: {test_name}")
    driver.quit()


@pytest.fixture()
def api():
    api_client = ApiClient()
    yield api_client
    api_client.clean_session_cookies()
