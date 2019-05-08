import re

from selenium_ui_tests_bdd.locators.search_page_locators import SearchPageLocators
from selenium_ui_tests_bdd.pages.base_page import BasePage


class SearchPage(BasePage):

    def write_text_in_search_field(self, text):
        self.send_keys(*SearchPageLocators.search_textbox_locator, text)

    def search_button_click(self):
        self.click_on(*SearchPageLocators.search_button_locator)

    def is_title(self):
        return self.get_title()

    def test_price(self):
        price_list = []
        prices = self.find_elements(*SearchPageLocators.price_locator)
        for price in prices:
            price = re.findall(r'\d+.\d+$', price.text)
            for i in price:
                price_list.append(float(i))
        return sum(price_list)
