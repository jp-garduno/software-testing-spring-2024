Feature: Google Search
  As a user
  I want to search for "Hello, world!" on Google
  So that I can see the search results page

  Scenario: Searching for "Hello, world!" on Google
    Given I am on the Google homepage
    When I search for "Hello, world!"
    Then I should see the search results
