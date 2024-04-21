# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch

from src.data_fetcher import fetch_data_from_api


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("src.data_fetcher.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)
