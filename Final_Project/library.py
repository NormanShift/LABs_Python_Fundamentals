# Responsibility: Collections of library items, users and bookings

from library_item import Book


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

