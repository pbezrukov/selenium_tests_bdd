import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')
def connect(request):
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(browser, test_name)
    browser.quit()


def take_screenshot(browser, test_name):
    now = datetime.datetime.now()
    screenshots_dir = os.path.dirname(__file__) + "/results/screenshots/"
    screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name + str(now))
    browser.save_screenshot(screenshot_file_path)
