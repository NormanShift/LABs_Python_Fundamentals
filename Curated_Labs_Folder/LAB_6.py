# LAB 6

# Part A - List comprehensions

# A:1

squared_list = [] # First, we initialize an empty list.

for n in range(1, 21):
    squared_list.append(n ** 2) # Then we populate the list

print(squared_list)

# Same but with list comprehension:

squared_list = [n ** 2 for n in range(1, 21)] # Basically we define the operation and the loop inside the list.

print(squared_list)

#--------------------------
# A:2

even_numbers = [n for n in range(1, 21) if n % 2 == 0]

print(even_numbers)

#--------------------------
# A:3

names_list = ["  jimmey  ","  ryu   ","  charlie    "," williams      "]

# for name in names_list:
#     names = name.strip().title()
#     print(names)

# Or:
# clean_names = []

# for name in names_list:
#     clean_names.append(name.strip().title())

# print(clean_names)

# Or:
clean_names = [name.strip().title() for name in names_list]

print(clean_names)

#--------------------------
# A:4

scores = [85, 62, 92, 70]

passed = [score for score in scores if score >= 70]

print("Passed:", passed)

#--------------------------
# A:5

scores = [85, 62, 92, 70, 52]

final_scores = ["Pass"
    if score >= 70
    else "Fail"
    for score in scores
    ] # Pass and Fail are added (assigned or "apended") to the list and is now populating the list

print(final_scores)

# A:6

# 1st loop from previous lesson (list reused)
numbers = [3, 8, 12, 5, 20, 7]

# for number in numbers:
#     if number >= 10:
#         print(number)

nine_up = [
    number
    for number in numbers
    if number >= 10] # Add number to the list if number above 9.

print(nine_up)

# 2nd loop from previous lesson (list reused)
numbers = [1, 2, 3, 4, 5, 6]

# for number in numbers:
#     if number % 2 == 0:
#         print(number)

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# 3rd loop from previous lesson (parts reused)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 65},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 55}]

def get_student_status(student):
    if student["score"] >= 70:
        return "Pass"
    return "Fail"

# for student in students:
#     status = get_student_status(student) 
#     print(f"{student['name']} has a score of {student['score']} and has {status}.")

statuses = [
    "Pass"
    if student["score"] >= 70
    else "Fail"
    for student in students
]

print(statuses)

student_results = [
    f"{student['name']} has a score of {student['score']} and has {get_student_status(student)}."
    for student in students
]

print(student_results)


#---------------------
# Part B - Dictionary and set comprehensions
# B:1

mapping_dict = {
    number: number ** 2
    for number in range(1, 11)}

print(mapping_dict)

#---------------------
# B:2

words = ["Krake", "Filur", "Kuf", "Genialitet", "Joker"]

words_length = {
    word: len(word)
    for word in words
    }

print(words_length)

#---------------------
# B:3

duplicates = ["Krake", "  Filur    ", "   Krake  ", "  Kuf   ", "   Genialitet  ", "  Joker   ", "  Filur  ", "  Kuf   "]

no_duplicates = {word.strip().lower() for word in duplicates}

print(no_duplicates) # The output is a set, which only accepts uniqe values (removes duplicates)
print(sorted(no_duplicates))

#---------------------
# B:4

# A dictionary of dictionaries.
products = {
    "P01": {
        "name": "Laptop",
        "price": 999.99,
        "stock": 15
        },
    "P02": {
        "name": "Mouse",
        "price": 24.99,
        "stock": 50,
        },
    "P03": {
        "name": "Keyboard",
        "price": 49.99,
        "stock": 30
        },
    "P04": {
        "name": "Monitor",
        "price": 69.95,
        "stock": 9
        },
    }

threshold = 100

cheap_products = {
product_id: product_info
for product_id, product_info in products.items()
if product_info["price"] < threshold
} # Filter: Below threshold

print(cheap_products)

# print(products.items())

#---------------------
# B:5

students_list = [
    {"name": "Alice", "age": 20, "major": "Computer Science", "score": 95, "grade": "A"},
    {"name": "Bob", "age": 22, "major": "Mathematics", "score": 86, "grade": "A"},
    {"name": "Charlie", "age": 21, "major": "Physics", "score": 80, "grade": "B"},
    {"name": "David", "age": 23, "major": "Biology", "score": 85, "grade": "A"}
]


student_results = {
    student["name"]: "PASS" if student["score"] >= 70 else "FAIL"
    for student in students_list
}

print(student_results)

#---------------------
# Part C - enumerate

# C:1

playlist = ["C't By Me Larv", "A Turn In se herz", "RammSchwein", "Curly Lingers", "Be toven", "AlcaTrash"]

# n_playlist = enumerate(playlist, start=1)

# print(list(n_playlist)) # Works but output can be prettier

for track, song in enumerate(playlist, start=1):
    print(track, song)

# C:2

tasks = ["shop", "drive", "collect", "buy", "fetch", "relax"]

for number, task in enumerate(tasks, start=1):
    print(f"Task {number}: {task.capitalize()}")


# C:3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

threshold = 5

for index, number in enumerate(numbers, start=0): # For lists, index starts at 0.
    if number >= threshold:
        print(f"Index {index} above threshold holds:", number) # Actually prinding indes numbers of any given list.


# C:4

languages = ["Python", "Java", "C#", "JavaScript"]

# Old version:
for i in range(len(languages)):
    print(languages[i])

# New version:
for index, language in enumerate(languages):
    print(index, language)


# Part D - zip and unpacking

# D:1

names = ["Jimmey","Ryu","Charlie","Williams"]

scores = [1, 2, 3, 4]

for name, score in zip(names, scores):
    print(name, score)


# D:2

