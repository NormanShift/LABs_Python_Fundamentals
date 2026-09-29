# This is the project for the final part of Python Fundamentals at Lexicon 2026. The course is part of an education in Python and Ai, extending to spring 2027.

# Defining an empty list (later to be populated by book of the type dictionary):
books =[]

 # A method for adding books to books[]
def add_book(title, author, year):
    # Each book or item in the list is by it's own, a dictionary in books[]
    book = {"title": title,
            "author": author,
            "year": year,
            "available": True} # Adding a book always sets availability to True
    books.append(book)
    print(f"Book '{title}' added to the library.")

# Actually adding a book to books[] (calling add_books() )
add_book("Small Beginnings", "Charles S Noman", 1921)


# Of course we also want a function for viewing the library books[] (the list of dictionaries (books) is the library).
def view_books():
    # Here book is a dictionary being iterated over by the for loop. Each value is being accessed within ["key"] (square brackets).
    for book in books:
        print(f"{book["title"]} by {book["author"]}\nPublished: {book["year"]}\nAvailable: {book["available"]}")

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


# Next phase
# Adding functionality - Borrow a Book
def reserve_book(title):
    for book in books:
        if book["title"].lower() == title.lower():

            if not book["available"]:
                print(f"'{book['title']}' is already reserved!")
                return

            book["available"] = False
            print(f"'{book['title']}' has been reserved.")
            return

    print(f"No book matching '{title}' was found.")

reserve_book("Small Beginningrfd")
reserve_book("Small Beginnings")
reserve_book("Small Beginnings")

# Returning a book to the library (in a real world scenario a barcode could be used)
def return_book(title):
    for book in books:
        if book["title"].lower() == title.lower():

            if book["available"]:
                print(f"{book["title"]} was already returned!")
                return
            
            book["available"] = True
            print(f"'{book["title"]}' has been returned.")
            return

    print(f"No book matching '{title}' was found.")

return_book("Roaming Cattle")
return_book("Small Beginnings")