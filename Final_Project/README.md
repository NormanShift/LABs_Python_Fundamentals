# Library Management System

This repository contains my final project for the Python Fundamentals course held by Lexicon in September 2026.

The project is a small command-line Library Management System written in Python. I chose a library system because it is a practical example of how collections, classes, functions, file handling, validation, and a simple user interface can work together in one program.

There were certainly more adventurous project options available, but I decided to build something practical. Jokes aside, books are amazing, aren't they?

## Current project status

This project is an incomplete but functional prototype.

The current version provides two menu sections:

- Librarian
- Member

The two sections are currently menu choices rather than a complete login or authorization system. Selecting a role opens the corresponding submenu.

### Librarian functionality

The Librarian can currently:

- Add a printed book to the library catalogue
- Enter the title, author, and publication year
- View all registered library items
- Receive an error message if the publication year is not a whole number
- Receive an error message when attempting to add a duplicate book

### Member functionality

The Member can currently:

- View all registered library items

The Member cannot yet reserve, borrow, or return items.

## Data persistence

Library items are stored in a JSON file.

When the program starts, it loads previously saved items from the file. When a book is added through the Librarian menu, the updated catalogue is saved so that the book remains available after the program is closed and restarted.

If the saved catalogue is empty, the program adds sample books for demonstration purposes.

## Command-line interface

The program contains:

- A main menu
- A Librarian submenu
- A Member submenu
- Screen-clearing between menus
- Pauses after operations so that output can be read
- Validation of menu choices
- An option for returning to the previous menu
- An option for closing the program

## Project structure

The project is divided into multiple Python modules with different responsibilities.

- `main.py` contains the command-line menus, user input, and program entry point.
- `library.py` manages the library catalogue, saved data, and library operations.
- `library_items.py` contains the classes representing library items.
- `library_items.json` stores the catalogue between program sessions.

Additional modules or classes may exist in the repository as part of the planned design, but not all of them are currently connected to the running application.

## Python concepts currently demonstrated

The working version demonstrates:

- Variables and data types
- Functions and parameters
- Conditions and loops
- Lists
- Classes and objects
- Inheritance between library item types
- Object attributes and state
- Methods
- User input
- Input validation
- Exception handling
- Importing from multiple modules
- Reading and writing JSON
- Persistent file storage
- A command-line menu system

## Running the program

Open a terminal in the project directory and run:

 python main.py
