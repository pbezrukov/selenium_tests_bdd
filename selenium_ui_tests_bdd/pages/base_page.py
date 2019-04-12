from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.browser = driver
        self.base_url()

    def base_url(self):
        return self.browser.get("https://www.ebay.com")

    def find_elem(self, by, locator):
        element = (by, locator)
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(element))

    def click_on(self, by, locator):
        element = self.find_elem(by, locator)
        element.click()

    def send_keys(self, by, locator, data):
        element = self.find_elem(by, locator)
        element.clear()
        element.send_keys(data)

    def get_title(self):
        return self.browser.title

    def find_elements(self, by, locator):
        return self.browser.find_elements(by, locator)

    def page_source(self):
        return self.browser.page_source
