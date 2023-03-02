import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    return driver


def pytest_addoption(parser):  # this get the value from the cLI hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the value to the setup method
    return request.config.getoption("--browser")


###HTML REPORT###

# Adding environment  hook to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Ecommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Avinash'
