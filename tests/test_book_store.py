# -*- coding: utf-8 -*-

"""
Book store unit testing examples.
"""
import unittest

from src.book_store import Book, BookStore


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    def test_book_init(self):
        """
        Checks the book properties
        """
        title = "title"
        author = "author"
        price = 9.99
        quantity = 5
        book = Book(title, author, price, quantity)
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)
        self.assertEqual(book.price, price)
        self.assertEqual(book.quantity, quantity)


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
