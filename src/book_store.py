# -*- coding: utf-8 -*-

"""
Book store example.
"""


class Book:  # pylint: disable=too-few-public-methods
    """
    Book class.
    """

    def __init__(self, title, author, price, quantity):
        """Book init."""
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def display(self):
        """Displays the book information."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")


class BookStore:
    """
    Book store class.
    """

    def __init__(self):
        """Book class init."""
        self.books = []

    def add_book(self, book):
        """Adds a book to the store."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the store.")

    def display_books(self):
        """Displays all books available in the store."""
        if not self.books:
            print("No books in the store.")
        else:
            print("Books available in the store:")
            for book in self.books:
                book.display()

    def search_book(self, title):
        """Searches a books in the store."""
        found_books = [
            book for book in self.books if book.title.lower() == title.lower()
        ]
        if not found_books:
            print(f"No book found with title '{title}'.")
        else:
            print(f"Found {len(found_books)} book(s) with title '{title}':")
            for book in found_books:
                book.display()


def main():
    """Application entrypoint."""
    bookstore = BookStore()

    while True:
        print(
            "\n1. Display all books\n2. Search for a book\n3. Add a new book\n4. Exit"
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            bookstore.display_books()
        elif choice == "2":
            title = input("Enter the title of the book you want to search: ")
            bookstore.search_book(title)
        elif choice == "3":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            price = float(input("Enter the price of the book: "))
            quantity = int(input("Enter the quantity of the book: "))
            new_book = Book(title, author, price, quantity)
            bookstore.add_book(new_book)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
