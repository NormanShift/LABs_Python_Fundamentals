from library import Library
from library_item import Book
from user import Librarian, Member


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
            print("Closing the system.")
            break

        else:
            print("Please choose a valid option.")



if __name__ == "__main__":
    main()