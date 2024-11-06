# -*- coding: utf-8 -*-

"""
Book store unit testing examples.
"""
import unittest
from unittest.mock import patch

from src.book_store import Book, BookStore


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    def setUp(self):
        """
        Creates the book properties
        """
        self.title = "title"
        self.author = "author"
        self.price = 9.99
        self.quantity = 5

    def test_book_init(self):
        """
        Checks the book properties.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        self.assertEqual(book.title, self.title)
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.price, self.price)
        self.assertEqual(book.quantity, self.quantity)

    @patch("builtins.print")
    def test_book_display(self, mock_print):
        """
        Checks the book display function.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        book.display()
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call(f"Title: {self.title}")
        mock_print.assert_called_with(f"Quantity: {self.quantity}")


class TestBookStore(unittest.TestCase):
    """
    Book store unittest class.
    """

    def test_book_store_init(self):
        """
        Checks the book store properties.
        """
        book_store = BookStore()
        self.assertEqual(book_store.books, [])
