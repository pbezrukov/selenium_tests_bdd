# coding=utf-8
"""Tests with search pages feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium_ui_tests_bdd.pages.search_page import SearchPage
import allure


@scenario('../features/search_item.feature', 'Test with search of items')
def test_test_with_search_of_items():
    """Test with search of items."""


@given('I am on ebay main page')
def i_am_on_ebay_main_page(connect):
    """I am on ebay main page."""
    global browser
    browser = SearchPage(connect)


@when('Click on search button')
@allure.step("Click on search button")
def click_on_search_button():
    """Click on search button."""
    browser.search_button_click()


@when('I write <text> in textbox field')
@allure.step
def i_write_text_in_textbox_field(text):
    """I write <text> in textbox field."""
    browser.write_text_in_search_field(text)


@then('I should see <text>')
@allure.step
def i_should_see_text(text):
    """I should see <text>."""
    assert text in browser.is_title()


@then('Sum of prices of the first 10 found items should be more 1000$')
@allure.step("Sum of prices of the first 10 found items should be more 1000$")
def sum_of_prices_of_the_first_10_found_items_should_be_more_1000():
    """Sum of prices of the first 10 found items should be more 1000$."""
    assert browser.test_price() > 1000
