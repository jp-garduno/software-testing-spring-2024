# -*- coding: utf-8 -*-

"""
Login unit testing examples.
"""
import unittest

from src.login import generate_salt


class TestLogin(unittest.TestCase):
    """
    Login unittest class.
    """

    def test_generate_salt(self):
        """
        Checks salt length.
        """
        self.assertEqual(len(generate_salt()), 32)
