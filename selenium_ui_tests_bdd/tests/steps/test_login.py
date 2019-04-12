# coding=utf-8
"""Login feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)
from selenium_ui_tests_bdd.pages.login_page import LoginPage
import allure

scenarios('../features/login.feature')


@given('I am on ebay login page')
def i_am_on_ebay_login_page(connect):
    """I am on ebay login page."""
    global browser
    browser = LoginPage(connect)
    browser.navigate_to_login_page()


@given('I am on ebay main page')
def i_am_on_ebay_main_page(connect):
    """I am on ebay main page"""
    global browser
    browser = LoginPage(connect)


@when('I write email and password and click Sign in button')
@allure.step('I write email, password and click Sign in button')
def i_write_email_and_password_and_click_button():
    """I write email and password and click button."""
    browser.write_login_password("admin@ad.com", "125976")
    browser.sign_in_button()


@when('I click sign in button')
@allure.step('I click sign in')
def click_sign_in():
    """I click sign in button"""
    browser.navigate_to_login_page()


@then(parsers.parse("I should see {text} in error message"))
@allure.step('I should see {text} in error message')
def i_should_see_error_message(text):
    """I should see error message."""
    message = browser.is_message().text
    assert text in message


@then(parsers.parse('I should see {text} title'))
@allure.step('I should see {text} title')
def check_title(text):
    """I should see title"""
    title = browser.is_title()
    assert text == title
