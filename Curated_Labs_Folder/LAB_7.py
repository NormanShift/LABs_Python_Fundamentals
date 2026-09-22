# Lab 7

# Part A - Classes and objects

# A:1

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages =pages


# book1 = Book("Dramatichus", "Emmeralda Smithsonian", 384)
# book2 = Book("Gebraldar Man", "Kubriq Wilderson", 455)
# book3 = Book("The Fornicus Debacle", "Stalind Colaugustine", 280)
# book4 = Book("Hollywood & NASA", "Stanley Cathron", 89)

# print(f"Title: {book1.title}\nAuthor: {book1.author}\nPages: {book1.pages}\n")
# print(f"Title: {book2.title}\nAuthor: {book2.author}\nPages: {book2.pages}\n")
# print(f"Title: {book3.title}\nAuthor: {book3.author}\nPages: {book3.pages}\n")
# print(f"Title: {book4.title}\nAuthor: {book4.author}\nPages: {book4.pages}\n")

#------------------------------

#  A:2

# class Laptop():
#     def __init__(
#             self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# laptop1 = Laptop("Compaq", "T-800", 32, 1595.95)
# laptop2 = Laptop("MSI", "Stealth G8", 32, 1595.95)
# laptop3 = Laptop("ASUS", "Republic OC-ed", 32, 1595.95)

# print(vars(laptop1))
# print(vars(laptop2))
# print("Recommended price:", laptop3.price)

# laptop3.price = 1495.95

# print("Discounted:" , laptop3.price)

#------------------------------

# A:3

# class Laptop():
#     def __init__(
#             self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# laptop1 = Laptop("Compaq", "T-800", 32, 1595.95)
# laptop2 = Laptop("MSI", "Stealth G8", 32, 1595.95)

# print("Same instance (?):", laptop1 is laptop2)

#------------------------------

# A:4

# class Book():
#     def __init__(self, title, author, pages = 346):
#         self.title = title
#         self.author = author
#         self.pages =pages


# book1 = Book("Dramatichus", "Emmeralda Smithsonian")
# print("Title:", book1.title)
# print("Author:", book1.author)
# print("Default:", book1.pages)

#------------------------------

# A:5

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages =pages


book1 = Book(
    title = "Dramatichus",
    author = "Emmeralda Smithsonian",
    pages = 348
)

print("Title:", book1.title)
print("Author:", book1.author)
print("Default:", book1.pages)


#------------------------------

# Part B - Methods and state

# B:1

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages >= 300
    



book1 = Book("Dramatichus", "Emmeralda Smithsonian", 384)
book2 = Book("Gebraldar Man", "Kubriq Wilderson", 455)
book3 = Book("The Fornicus Debacle", "Stalind Colaugustine", 280)
book4 = Book("Hollywood & NASA", "Stanley Cathron", 89)

print(book1.is_long())

print(f"Title: {book1.title}\nAuthor: {}\nPages: {book1.pages}\n")
print(f"Title: {book2.title}\nAuthor: {book2.author}\nPages: {book2.pages}\n")
print(f"Title: {book3.title}\nAuthor: {book3.author}\nPages: {book3.pages}\n")
print(f"Title: {book4.title}\nAuthor: {book4.author}\nPages: {book4.pages}\n")