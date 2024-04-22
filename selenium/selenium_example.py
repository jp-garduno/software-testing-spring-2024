# -*- coding: utf-8 -*-

"""
Selenium test examples.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open Google homepage
driver.get("https://www.google.com")

# Find the search box element by its name attribute
search_box = driver.find_element("name", "q")

# Type "Hello, world!" into the search box
search_box.send_keys("Hello, world!")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to let the search results load
time.sleep(5)

# Print the title of the search results page
print("Title of the search results page:", driver.title)

# Close the browser
driver.quit()
