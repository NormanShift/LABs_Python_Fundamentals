# Types: LibraryItem, Book, Audiobook (later)

class LibraryItem:
    def __init__(self):
        pass


class Book(LibraryItem):
    def __init__(self):
        super().__init__()


class Audiobook(LibraryItem):
    pass

