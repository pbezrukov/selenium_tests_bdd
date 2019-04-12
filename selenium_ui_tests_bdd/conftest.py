import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')
def connect():
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()
