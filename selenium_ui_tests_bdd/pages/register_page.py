from selenium_ui_tests_bdd.locators.search_page_locators import SearchPageLocators
from selenium_ui_tests_bdd.pages.base_page import BasePage
from selenium_ui_tests_bdd.locators.login_page_locators import LoginPageLocators


class RegisterPage(BasePage):

    def navigate_to_register_page(self):
        self.click_on(*SearchPageLocators.register_button)

    def is_text_on_page(self):
        return self.page_source()
