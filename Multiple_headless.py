"""A headless browser is a browser without a graphical user interface.
In other words, it runs in the background without displaying anything on the screen.
Selenium is a popular automation tool for testing web applications, and it can be used with headless browsers
to perform automated testing without requiring a visible browser window
"""
import selenium.webdriver.common.devtools.v85.runtime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Initialize the Chrome driver
driver = webdriver.Chrome('', options=chrome_options)

# Navigate to a URL
driver.get('https://www.example.com')

# Print the page title
print(driver.title)

# Quit the browser
driver.quit()

import pytest
import json


@pytest.fixture
def config(scope='session'):  # execute only once
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)  # dictionary
    # assert Values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the webdriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser"{config["browser"]}" is not supported')
    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])
    # return the webdriver instance for the setup
    yield b
    # quit the webdriver instance for the setup
    b.quit()
