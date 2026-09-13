# Tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined by enclosing the elements in parentheses `()`.

coordinates = (10, 20)

print(coordinates)  # Accessing the tuple
print("X coordinate:", coordinates[0])  # Accessing the first element
print("Y coordinate:", coordinates[1])  # Accessing the second element

x, y = coordinates  # Unpacking the tuple into variables
print("Unpacked X coordinate:", x)  # Accessing the unpacked variable
print("Unpacked Y coordinate:", y)  # Accessing the unpacked variable

person = ("Alice", 30, "Engineer")
print(person)  # Accessing the tuple


a = 10
b = 20

b, a = a, b  # Unpacking the tuple into variables

print("Swapped values: a =", a, ", b =", b)  # Accessing the swapped values


# Sets are unordered collections of unique elements. They are defined by enclosing the elements in curly braces `{}`.

numbers_set = {1, 2, 3, 4, 5}

print(numbers_set)  # Accessing the set

numbers_duplicate = {1, 2, 2, 3, 4, 4, 5}
print(numbers_duplicate)  # Accessing the set with duplicates (duplicates are removed)

users_list = ["Alice", "Bob", "Charlie", "Alice"]
users_set = set(users_list)  # Converting a list to a set to remove duplicates
print(users_set)  # Accessing the set with duplicates removed

languages_set = {"Python", "Java", "C++", "JavaScript", "Ruby"}
print(languages_set)  # Accessing the set of languages

added = languages_set.add("Go")  # Adding an element to the set
print(languages_set)  # Accessing the set after adding an element

languages_set.remove("Java")  # Removing an element from the set. Random order of elements in a set means that the order of elements may not be preserved.
print(languages_set)  # Accessing the set after removing an element
print(list(languages_set)[0])  # Accessing the set after removing an element

backend_languages = {"Python", "Java", "C#", "Ruby"}
frontend_languages = {"JavaScript", "HTML", "CSS", "Python"}

print(backend_languages & frontend_languages)  # Accessing the intersection of two sets (common elements)
print(backend_languages | frontend_languages)  # Accessing the union of two sets (all unique elements)
print(backend_languages - frontend_languages)  # Accessing the difference of two sets (elements in backend_languages but not in frontend_languages)

empty_collection = {}  # This is an empty dictionary, not a set. To create an empty set, use `set()`.
print(type(empty_collection))  # Accessing the type of the empty collection (will print <   class 'dict'>)

empty_collection_set = set()  # This is an empty set.
print(type(empty_collection_set))  # Accessing the type of the empty set (will print <class 'set'>)


# Dictionaries are unordered collections of key-value pairs. They are defined by enclosing the key-value pairs in curly braces `{}`.

person_dict = {"name": "Alice", "age": 30, "occupation": "Engineer"} # A dictionary with string keys and mixed value types (string and integer). Dictionaries are mutable and can hold various data types as values.

print(person_dict)  # Accessing the dictionary
print("Name:", person_dict["name"])  # Accessing a specific value by key
print("Age:", person_dict["age"])  # Accessing a specific value by key
print("Occupation:", person_dict["occupation"])  # Accessing a specific value by key

person_dict["age"] = 31  # Modifying a value by key
print(person_dict)  # Accessing the modified dictionary

person_dict["city"] = "New York"  # Adding a new key-value pair
print(person_dict)  # Accessing the dictionary after adding a new key-value pair

person = {
    "name": "Bob",
    "name": "Robert",  # Duplicate key, the last value will overwrite the previous one

    }

print(person)  # Accessing the dictionary with duplicate keys (will print {'name': 'Robert'})

print(person_dict["country"])  # Accessing a value not in the dictionary (will raise a KeyError)

print(person_dict.get("country", "Country not found"))  # Accessing a value not in the dictionary using get() (will print "Country not found")

print(person_dict.keys())  # Accessing the keys of the dictionary
print(person_dict.values())  # Accessing the values of the dictionary

print(person_dict.items())  # Accessing the key-value pairs of the dictionary


# Challenge: nested data structures

students_list = [
    {"name": "Alice", "age": 20, "major": "Computer Science", "score": 95, "grade": "A"},
    {"name": "Bob", "age": 22, "major": "Mathematics", "score": [90, 86], "grade": "A"},
    {"name": "Charlie", "age": 21, "major": "Physics", "score": 80, "grade": "B"},
    {"name": "David", "age": 23, "major": "Biology", "score": 85, "grade": "A"}
] # A list of dictionaries, where each dictionary represents a student with their name, age, and major. Lists are mutable, while dictionaries are also mutable but have unique keys.

print(students_list)  # Accessing the list of dictionaries
print("First student:", students_list[0])  # Accessing the first dictionary in the list
print("First student's name:", students_list[0]["name"])  # Accessing a specific value in the first dictionary

print("Fourth student's score:", students_list[3]["score"])  # Accessing a specific value in the fourth dictionary
print("Fourth student's grade:", students_list[3]["grade"])  # Accessing a specific value in the fourth dictionary
print("Second student's score:", students_list[1]["score"][1])  # Accessing a specific value in the second dictionary


test = {
    1: "one",
    "two": 2,
}

print(test, type(test[1]))  # Accessing the dictionary with mixed key types

