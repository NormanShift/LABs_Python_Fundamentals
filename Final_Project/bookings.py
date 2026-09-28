# This is the project for the final part of Python Fundamentals at Lexicon 2026. The course is part of an education in Python and Ai, extending to spring 2027.

# Defining an empty list (later to be populated by book of the type dictionary):
books =[]

 # A method for adding books to books[]
def add_book(title, author, year):
    # Each book or item in the list is by it's own, a dictionary in books[]
    book = {"title": title, "author": author, "year": year}
    books.append(book)
    print(f"Book '{title}' added to the library.")

# Actually adding a book to books[] (calling add_books() )
add_book("Small Beginnings", "Charles S Noman", 1921)


# Of course we also want a function for viewing the library books[] (the list of dictionaries (books) is the library).
def view_books():
    # Here book is the key being iterated over by the for loop. Each value is being accessed within [] (square brackets).
    for book in books:
        print(f"{book["title"]} by {book["author"]} {book["year"]}")

view_books()


def search_books(title):
    for book in books:
        # Here we can search for the title of a book
        if book["title"].lower() == title.lower():
            print(f"Search results: {book["title"]} by {book["author"]} {book["year"]}")
            return
    print(f"No book book matching '{title}' currently in the Library")

search_books("Andy Kaufman") # Returns 'No book matching: ...'
search_books("Small Beginnings")