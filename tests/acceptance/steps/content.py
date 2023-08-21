from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.new_post_page import NewPostPage
from tests.acceptance.page_model.post_page import PostPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
# We are loading the page, that we wanna interact with
    page = BasePage(context.driver)

# Checking the title of that page is correct
    assert page.title.is_displayed()

@step('The title tag has the content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)

    assert page.title.text == content

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

# Make sure that we have at least one post with the title, that we are passed in
    assert len(posts_with_title) > 0
# We can see all posts there
    assert all([post.is_displayed() for post in posts_with_title])


@then('The title tag has the content "(.*)"')
def step_impl(context, content):
    page = PostPage(context.driver)

    assert page.title.text == content


@then('The post content has a "(.*)" content')
def step_impl(context, content):
    page = PostPage(context.driver)

    assert page.content_text == content