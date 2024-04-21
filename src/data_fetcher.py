# -*- coding: utf-8 -*-

"""
Source code for mock up testing examples.
"""
import requests


def fetch_data_from_api(url):
    """Fetches data from an external API using the requests library."""
    response = requests.get(url, timeout=10)
    return response.json()
