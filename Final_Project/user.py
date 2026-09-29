# Types: User, Member, Librarian

class User:
    def __init__(self):
        pass


class Librarian(User):
    def __init__(self):
        super().__init__()


class Member(User):
    def __init__(self):
        pass

