Feature: Test that pages have the correct content

  Scenario: Blog page has a correct title
    Given I am on the blog page
    Then There is a title shown on the page
    And The title tag has the content "This is the blog page"

  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has the content "This is the homepage"

  Scenario: Create post has a correct title
    Given I am on the new post page
    Then There is a title shown on the page
    And The title tag has the content "Create post"

  Scenario: Blog page loads the posts
    Given I am on the blog page
    And I wait for the posts to load
    Then I can see there is a posts section on the page

  Scenario: User can create new posts
    Given I am on the new post page
    When I enter "Test Post" in the "title" field
    And I enter "Test Content" in the "content" field
    And I press the submit button
    Then I am on the blog page
    Given I wait for the posts to load
    Then I can see there is a post with title "Test Post" in the posts section

  Scenario: Post page has a correct title and content
    Given I am on the new post page
    When I enter "Test Post2" in the "title" field
    And I enter "Test Content2" in the "content" field
    And I press the submit button
    Then I am on the blog page
    Given I wait for the posts to load
    Then I can see there is a post with title "Test Post2" in the posts section
    When I click on the "Test Post2" post
    Then I am on the post page
    And The title tag has the content "Test Post2"
    And The post content has a "Test Content2" content
