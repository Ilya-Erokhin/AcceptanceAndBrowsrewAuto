from selenium.webdriver.common.by import By

from tests.acceptance.page_model import post_page


class PostPageLocators:
    TITLE = (By.CSS_SELECTOR, 'h1')
    CONTENT = (By.CSS_SELECTOR, 'p')