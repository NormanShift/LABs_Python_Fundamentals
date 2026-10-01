# Types: LibraryItem, Book, Audiobook (later)

class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Reserved"

        return(
            f"{self.title} by {self.author}"
            f"({self.year}) - {status}"
        )

    def to_dict(self):
        return {
            "type": "library_item",
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available
        }


class Book(LibraryItem):
    # def __init__(self, title, author, year):
    #     super().__init__(title, author, year)
    def to_dict(self):
        return {
        "type": "book",
        "title": self.title,
        "author": self.author,
        "year": self.year,
        "available": self.available
        }


class AudioBook(LibraryItem):
    # def __init__(self, title, author, year, lenght):
    #     super().__init__(title, author, year)
    #     self.length = lenght

    # def __str__(self):
        # status = "Available" if self.available else "Reserved"

        # return (
        #     f"{self.title} by {self.author} "
        #     f"({self.year}), {self.length} minutes "
        #     f"- {status}"
        # )
        def __init__(self, title, author, year, length):
            super().__init__(title, author, year)
            self.length = length
        
        def __str__(self):
            return (
                f"{super().__str__()}, "
                f"length: {self.length} minutes"
        )

        def to_dict(self):
            return {
            "type": "audiobook",
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available,
            "length": self.length
            }




book = Book(
    "Small Beginnings",
    "Charles S Noman",
    1921
)

audio_book = AudioBook(
    "Python Advanced",
    "A. Developer",
    2026,
    420
)

print(book)
print(audio_book)