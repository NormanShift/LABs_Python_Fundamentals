import os
import subprocess

from library_items import Book
from library import Library
from helpers import clear_screen, pause

def add_book_from_input(library):
    print("\nAdd a new book")

    title = input("Title: ").strip()
    author = input("Author: ").strip()

    try:
        year = int(input("Publication year: "))
    except ValueError:
        print("Publication year must be a whole number.")
        pause()
        return

    book = Book(title, author, year)

    try:
        library.add_item(book)
        print(f"\n'{book.title}' was added.")

    except ValueError as error:
        print(f"\nCould not add book: {error}")

    pause()


# --------------------------------
# Menus goes hereunder:

def librarian_menu(library):


    while True:
        clear_screen()
        print()
        print("Librarian Menu")
        print("1. Add item")
        print("2. View items")
        print("3. Return to main menu")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            clear_screen()
            add_book_from_input(library)

        elif choice == "2":
            clear_screen()
            library.view_items()
            pause()

        elif choice == "3":
            # clear_screen()
            return

        else:
            
            print("Please choose a valid option.")
            pause()


def member_menu(library):


    while True:
        clear_screen()
        print()
        print("Member Menu")
        print("1. View items")
        # print("2. Reserve item")
        print("2. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear_screen()
            library.view_items()
            pause()

        elif choice == "2":
            # clear_screen()
            return

        else:
            # clear_screen()
            print("Please choose a valid option.")
            pause()


def main():
    library = Library("Lexicon Library")
    library.load_items()  # Load items from the JSON file

    if not library.items:
        library.add_sample_books()


    while True:
        clear_screen()
        print()
        print("Library Booking System")
        print("1. Librarian")
        print("2. Member")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            librarian_menu(library)

        elif choice == "2":
            member_menu(library)

        elif choice == "3":
            clear_screen()
            print("\n... Closing LMS\n")
            break

        else:
            print("Please choose a valid option.")
            pause()



if __name__ == "__main__":
    main()