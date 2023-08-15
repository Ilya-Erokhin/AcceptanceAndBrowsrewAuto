from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
# We already have the entire URL inside page_model/base_page.py (BasePage class)
        return super(HomePage, self).url + '/'

# Gives us the link of the blog page
    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)