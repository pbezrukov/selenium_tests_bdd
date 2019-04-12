from selenium_ui_tests_bdd.locators.search_page_locators import SearchPageLocators
from selenium_ui_tests_bdd.pages.base_page import BasePage
from selenium_ui_tests_bdd.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def navigate_to_login_page(self):
        self.click_on(*SearchPageLocators.log_in_button)

    def write_login_password(self, login, password):
        self.send_keys(*LoginPageLocators.login_textbox_locator, login)
        self.send_keys(*LoginPageLocators.password_textbox_locator, password)

    def sign_in_button(self):
        self.click_on(*LoginPageLocators.sign_in_button)

    def is_title(self):
        return self.get_title()

    def is_message(self):
        return self.find_elem(*LoginPageLocators.error_message)
