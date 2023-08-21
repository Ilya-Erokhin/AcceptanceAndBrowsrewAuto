from behave import *
from selenium.webdriver.common.by import By

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.new_post_page import NewPostPage
from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')


# (.*) == link_text
@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation
# find one link, that we wanna click
    matching_links = [l for l in links if l.text == link_text]
# Gat access from the first element
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)

@when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()


@when('I click on the "(.*)" post')
def step_impl(context, content):
    page = BlogPage(context.driver)

    posts = page.posts

    for post in posts:
        if post.text == content:
            post.click()
            break
