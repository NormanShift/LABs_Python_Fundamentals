# Types: User, Member, Librarian

class User:
    def __init__(self, user_id, name):
        if not name.strip():
            raise ValueError("user name cannot be empty!")
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"{self.user_id}: {self.name}"
        

class Librarian(User):
    def add_library_item(self, library, item):
        library.add_item(item)


class Member(User):
    pass

