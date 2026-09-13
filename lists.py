# Lists in Python are ordered, mutable collections that can hold a variety of data types. They are defined using square brackets [] and can contain elements of different types, including integers, strings, floats, booleans, other lists, and dictionaries. Lists are versatile and widely used in Python programming.

numbers = [10, 20, 30, 40, 50]

print(numbers)  # Accessing the first element

print("First element:", numbers[0])  # Accessing the first element
print("Second element:", numbers[1])  # Accessing the second element
print("Third element:", numbers[2])  # Accessing the third element
print("Fourth element:", numbers[3])  # Accessing the fourth element
print("Fifth element:", numbers[4])  # Accessing the fifth element
print("Last element:", numbers[-1])  # Accessing the last element
print(numbers[1:4])  # Accessing a slice of the list (elements at index 1, 2, and 3)
print(numbers[:3])  # Accessing the first three elements
print(numbers[:2])  # Accessing the first two elements
print(numbers[::2])  # Accessing every second element
print(numbers[::-1])  # Accessing the list in reverse order
print(numbers[::-2])  # Accessing every second element in the slice (elements at index 1 and 3)

mixed_list = [1, "two", 3.0, True, [5, 6], {"key": "value"}] # Shows that lists can contain different data types, including integers, strings, floats, booleans, other lists, and dictionaries. Lists are mutable.
print(mixed_list)  # Accessing the mixed list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]  # A list of lists (2D list)
print(matrix)  # Accessing the matrix

print("Element at row 1, column 2:", matrix[0][1])  # Accessing an element in the 2D list
print("Element at row 2, column 3:", matrix[1][2])  # Accessing an element in the 2D list


languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
print(languages)  # Accessing the list of languages

languages[2] = "C#"  # Modifying an element in the list
print(languages)  # Accessing the modified list

languages.append("Go")  # Adding an element to the end of the list
print(languages)  # Accessing the list after appending an element

languages.insert(1, "Swift")  # Inserting an element at a specific index
print(languages)  # Accessing the list after inserting an element

languages.remove("Java")  # Removing an element from the list by value.
print(languages)  # Accessing the list after removing an element

removed_element = languages.pop(3)  # Removing the last element by index and storing it in a variable
print(languages)  # Accessing the list after popping an element
print("Removed element:", removed_element)  # Accessing the removed element

print("Length of the list:", len(languages))  # Getting the length of the list

print("Python" in languages)  # Checking if an element exists in the list. Returns True if the element is found, otherwise returns False.
print("Rust" in languages)  # Checking if an element exists in the list. Returns True if the element is found, otherwise returns False.

numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()  # Sorting the list in ascending order. Changes the original list.
print("Sorted list:", numbers)  # Accessing the sorted list

numbers.reverse()  # Reversing the order of the list. Changes the original list.
print("Reversed list:", numbers)  # Accessing the reversed list

# sorted and sort are not the same. sorted() returns a new sorted list, while sort() modifies the original list in place.

sorted_numbers = sorted(numbers)  # Creating a new sorted list without modifying the original list.
print("Sorted numbers (new list):", sorted_numbers)  # Accessing the new sorted list
print("Original numbers (unchanged):", numbers)  # Accessing the original list


list_a = [1, 2, 3]

list_b = list_a

list_b.append(4)  # Modifying list_b also modifies list_a because they reference the same list in memory.
print("List A:", list_a)  # Accessing list_a after modifying list_b
print("List B:", list_b)  # Accessing list_b after modifying it

list_c = list_a.copy()  # Creating a copy of list_a. Modifying list_c does not affect list_a.
list_c.append(5)  # Modifying list_c does not affect list_a.
print("List A:", list_a)  # Accessing list_a after modifying list_c
print("List C:", list_c)  # Accessing list_c after modifying it


