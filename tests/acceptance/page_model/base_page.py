from tests.acceptance.locators.base_page import BasePageLocators
'''
BasePage represents things, that are sharing between ALL pages
'''

class BasePage:
# All pages need the __init__ method, to get driver(browser)
    def __init__(self, driver):
        self.driver = driver

# Got a current base URL, without any endpoints
    @property
    def url(self):
        return 'http://127.0.0.1:5000'

# Got a title, because all pages should have a title
    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)