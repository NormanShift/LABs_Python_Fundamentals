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

        self.data_file = Path("library_items.json")

    def save_items(self):
        item_data = [
            item.to_dict()
            for item in self.items
        ]

        with self.data_file.open(
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                item_data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_items(self):
        if not self.data_file.exists():
            return

        try:
            with self.data_file.open(
                "r",
                encoding="utf-8"
            ) as file:
                item_data = json.load(file)

        except json.JSONDecodeError:
            print("The library data file could not be read.")
            return

        self.items = []

        for data in item_data:
            if data["type"] == "book":
                item = Book(
                    data["title"],
                    data["author"],
                    data["year"]
                )

            elif data["type"] == "audiobook":
                item = AudioBook(
                    data["title"],
                    data["author"],
                    data["year"],
                    data["length"]
                )

            else:
                continue

            item.available = data["available"]
            self.items.append(item)



    def add_item(self, item):
        self.items.append(item) # Adding a library item to the list of items[] .
        self.save_items() # Save the updated list of items to the JSON file.

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


