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

def pause():
    input("\nPress Enter to continue...")

clear_screen()

def librarian_menu(library):


    while True:
        clear_screen()
        print()
        print("Librarian Menu")
        print("1. View items")
        print("2. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear_screen()
            library.view_items()
            input("\n Press Enter to continue...")

        elif choice == "2":
            # clear_screen()
            return

        else:
            clear_screen()
            print("Please choose a valid option.")
            pause()


def member_menu(library):


    while True:
        clear_screen()
        print()
        print("Member Menu")
        print("1. View items")
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
            clear_screen()
            print("Please choose a valid option.")
            pause


def main():
    library = Library("Lexicon Library")

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
            # clear_screen()
            print("\n... Closing LMS\n")
            break

        else:
            print("Please choose a valid option.")
            pause()



if __name__ == "__main__":
    main()