from tests.acceptance.locators.post_page import PostPageLocators
from tests.acceptance.page_model.base_page import BasePage


class PostPage(BasePage):

    @property
    def url(self):
        title_text = self.title.text
        encoded_title = title_text.replace(' ', '%20')
        return super(PostPage, self).url + '/post/' + encoded_title

    @property
    def title_text(self):
        return self.driver.find_element(*PostPageLocators.TITLE).text

    @property
    def content_text(self):
        return self.driver.find_element(*PostPageLocators.CONTENT).text