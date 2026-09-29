import os
import subprocess

from library import Library


def clear_screen():
    if os.name == "nt":
        subprocess.run(
            ["cmd", "/c", "cls"],
            check=False
        )
    # else:
    #     subprocess.run(
    #         ["clear"],
    #         check=False
    #     )

clear_screen()

def librarian_menu(library):

    clear_screen()

    while True:
        print()
        print("Librarian Menu")
        print("1. View items")
        print("2. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear_screen()
            library.view_items()

        elif choice == "2":
            clear_screen()
            return

        else:
            print("Please choose a valid option.")


def member_menu(library):

    clear_screen()

    while True:
        print()
        print("Member Menu")
        print("1. View items")
        print("2. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear_screen()
            library.view_items()

        elif choice == "2":
            clear_screen()
            return

        else:
            print("Please choose a valid option.")


def main():
    library = Library("Lexicon Library")

    library.add_sample_books()

    clear_screen()

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
            clear_screen()
            print("\n... Closing LMS\n")
            break

        else:
            print("Please choose a valid option.")



if __name__ == "__main__":
    main()