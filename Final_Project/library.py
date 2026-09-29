# Responsibility: Collections of library items, users and bookings


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
            if title.lower() == title.lower():
                return item

        return None
