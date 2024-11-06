# -*- coding: utf-8 -*-

"""
System Test example using Behavior-Driven Development (BDD) with Behave (Gherkin) and Selenium.
"""
from behave import given, then, when  # pylint: disable=no-name-in-module
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver


@given("I am on the Google homepage")
def open_browser(context):
    """Opens Google in Chrome."""
    svc = webdriver.ChromeService(executable_path=binary_path)
    context.driver = webdriver.Chrome(service=svc)
    context.driver.get("https://www.google.com")


@when('I search for "{query}"')
def search(context, query):
    """Searches something in Google."""
    search_box = context.driver.find_element("id", "APjFqb")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    delay = 5  # seconds
    wait = WebDriverWait(context.driver, delay)
    wait.until(EC.presence_of_element_located((By.ID, "rcnt")))


@then('the title should start with "{query}"')
def verify_results(context, query):
    """Prints the title of the Google search results page."""
    title = context.driver.title

    try:
        assert title.startswith(query) is True
    finally:
        context.driver.quit()
