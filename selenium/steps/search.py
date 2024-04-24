# -*- coding: utf-8 -*-

"""
System Test example using Behavior-Driven Development (BDD) with Gherkin, and Selenium.
"""
import time

from behave import given, then, when  # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


@given("I am on the Google homepage")
def open_browser(context):
    """Opens Google in Chrome."""
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")


@when('I search for "{query}"')
def search(context, query):
    """Searches something in Google."""
    search_box = context.driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the search results to load


@then("I should see the search results")
def verify_results(context):
    """Prints the title of the Google search results page."""
    title = context.driver.title
    print("Title of the search results page:", title)
    context.driver.quit()
