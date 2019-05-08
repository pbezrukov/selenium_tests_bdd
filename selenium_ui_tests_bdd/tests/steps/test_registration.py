# coding=utf-8
"""Tests with registration page feature tests."""

import allure
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pytest_bdd import parsers

from selenium_ui_tests_bdd.pages.register_page import RegisterPage


@scenario('../features/registration.feature', 'Check registration page')
def test_check_registration_page():
    """Check registration page."""


@given('I am on ebay main page')
def i_am_on_ebay_main_page(connect):
    """I am on ebay main page."""
    global browser
    browser = RegisterPage(connect)


@when('I click on register Button')
@allure.step('I click on register button')
def i_click_on_register_button():
    """I click on register Button."""
    browser.navigate_to_register_page()


@then(parsers.parse('The page should have {text}'))
@allure.step('The new page should have {text}')
def the_page_should_have_create_an_account(text):
    """The page should have Create an account."""
    source = browser.page_source()
    assert text in source
