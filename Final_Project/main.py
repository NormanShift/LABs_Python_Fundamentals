from library import Library
from library_item import Book
from user import Librarian, Member


from library import Library


def librarian_menu(library):
    while True:
        print()
        print("Librarian Menu")
        print("1. View items")
        print("2. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.view_items()

        elif choice == "2":
            return

        else:
            print("Please choose a valid option.")


def member_menu(library):
    while True:
        print()
        print("Member Menu")
        print("1. View items")
        print("2. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.view_items()

        elif choice == "2":
            return

        else:
            print("Please choose a valid option.")


def main():
    library = Library("Lexicon Library")

    library.add_sample_books()

    while True:
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
            print("Closing LMS.")
            break

        else:
            print("Please choose a valid option.")



if __name__ == "__main__":
    main()