# Lab 7

# Part A - Classes and objects

# A:1

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages =pages


book1 = Book("Dramatichus", "Emmerald Smithsonian", 384)
book2 = Book("Gebraldar Man", "Kubriq Wilderson", 455)
book3 = Book("The Fornicus Debacle", "Stalind Colaugustine", 280)
book4 = Book("Hollywood & NASA", "Stanley Cathron", 89)

print(f"Title: {book1.title}\nAuthor: {book1.author}\nPages: {book1.pages}\n")
print(f"Title: {book2.title}\nAuthor: {book2.author}\nPages: {book2.pages}\n")
print(f"Title: {book3.title}\nAuthor: {book3.author}\nPages: {book3.pages}\n")
print(f"Title: {book4.title}\nAuthor: {book4.author}\nPages: {book4.pages}\n")

#------------------------------

#  A:2

