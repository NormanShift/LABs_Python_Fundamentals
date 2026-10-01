# Responsibility: Collections of library items, users and bookings

import json
from pathlib import Path

from library_items import Book, AudioBook


class Library:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.users = []
        self.bookings = []

    def add_item(self, item):
        self.items.append(item) # Adding a library item to the list of items[] .

    def add_user(self, user):
        self.users.append(user) # Member or Librarian

    def find_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item

    def add_sample_books(library):
        library.add_item(
            Book(
                "Small Beginnings",
                "Charles S Noman",
                1921
            )
        )

        library.add_item(
            Book(
                "Python Fundamentals",
                "A. Developer",
                2026
            )
        )

        return None

    def view_items(self):
        if not self.items:
            print("The library has no registered items.")
            return

        print(f"\nItems in {self.name}:")

        for item in self.items:
            print(item)


