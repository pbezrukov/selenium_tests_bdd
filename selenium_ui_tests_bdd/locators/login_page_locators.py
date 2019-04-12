from selenium.webdriver.common.by import By


class LoginPageLocators:

    login_textbox_locator = (By.XPATH, "//*[@id='userid']")
    password_textbox_locator = (By.XPATH, "//*[@id='pass']")
    sign_in_button = (By.XPATH, "//*[@id='sgnBt']")
    error_message = (By.XPATH, "//*[@id='errf']")
