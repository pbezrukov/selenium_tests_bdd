from selenium.webdriver.common.by import By


class SearchPageLocators:

    search_textbox_locator = (By.CSS_SELECTOR, "#gh-ac")
    search_button_locator = (By.XPATH, "//*[@id='gh-btn']")
    log_in_button = (By.XPATH, "//a[contains(@_sp,'m570.l1524')]")
    register_button = (By.XPATH, "//a[contains(.,'register')]")
    price_locator = (By.XPATH, "(//span[@class='s-item__price'])[position() <= 10]")
