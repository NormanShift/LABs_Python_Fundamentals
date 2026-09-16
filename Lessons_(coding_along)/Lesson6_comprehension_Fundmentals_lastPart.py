# Last part of the first part of Python Fundamentals (List comprehension)


# numbers = [1, 2, 3, 4, 5]

# doubled_numbers =[]

# for number in numbers:
#     doubled_numbers.append(number * 2)

# print(doubled_numbers)


# List comprehension

# Number * 2 for every number in numbers:
# doubled_numbers = [number * 2 for number in numbers]

# print(doubled_numbers)

#------------

numbers = [1, 2, 3, 4, 5]

squares =[number **2 for number in numbers]

print(squares)

#------------

names = ["ada", "grace", "guido"]

upper_names = [name.upper() for name in names]

print(upper_names)

#------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = [] # An empty list to be populated with the following for loop.

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers)

#------------

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

#------------

numbers = [1, 2, 3, 4, 5, 6]

result = [number ** 2 for number in numbers if number % 2 == 0] # First the condition and then the expression.

print(result)

#------------

names = ["Ada", "Gerard", "Bob", "Mildred", "Axa"]

long_names = [name for name in names if len(name) >= 5]

print(long_names)

#------------

# Dictionary comprehension

# numbers =[1, 2, 3, 4, 5] # -> key

# # squares = {}

# # for number in numbers:
# #     squares[number] = number ** 2

# # print(squares)


# # Same thing using dictionary comprehension (curly braces creates the dictionary):

# squares = {number: number ** 2 for number in numbers}

# print(squares)

#------------

prices = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}


double_prices = {
    product: price * 2
    for product, price in prices.items()} # items() gives both the key and the value.

print(double_prices)

#------------

scores = {
    "Anna": 85,
    "Bob": 62,
    "Charlie": 92,
    "Diana": 70
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 70
}

print(passed)

#------------

# Set comprehension

words = ["python", "java", "python", "csharp", "java"]

lengths = {len(word) for word in words}

print(lengths) # The output is a set, which only accepts uniqe values.

#------------

# Tuple???

numbers = (number * 2 for number in range(5))

print(numbers)

#------------

# Enumerate

languages = ["Python", "Java", "C#"]

for index in range(len(languages)):
    print(index, languages[index])

# A "cleaner" way of getting the same output:
# for index, languages in enumerate(languages):
#     print(index, languages)

# Yet another way to use enumerate:
# for position, language in enumerate(languages, start=1):
#     print(position, language)


# for language in languages:
#     print(languages)

# Zip

for index, language in enumerate(languages):
    print(index, languages) # Revisit!

#-------------------

names = ["Anna", "Bob", "Charlie"]
scores = [85, 62, 91]

for index in range(len(names)):
     print(names[index], scores[index])


for name, score in zip(names, scores):
    print(name, score)

pairs = list(zip(names, scores))

print(pairs)

#--------------
names = ["Anna", "Bob", "Charlie"]
scores = [85, 62, 91]
cities = ["Stockholm", "Goteborg", "Malmo"]

for name, score, city in zip(names, scores, cities):
    print(name, score, city)

#--------------

names = ["Anna", "Bob", "Charlie", "Diana"]
scores = [85, 62, 91]

for name, score in zip(names, scores):
    print(name, score) # The last name in the list "Diana" is skipped in the output.

#--------------

names = ["Anna", "Bob", "Charlie"]
scores = [85, 62, 91]

student_scores = dict(zip(names, scores)) # Convertst the two lists into key:value pairs.

print(student_scores)


# Unpacking

coordinates = (10, 20)

x, y = coordinates

print(x)
print(y)

#-------------------

names = ["Anna", "Bob", "Charlie"]

first, second, third = names
print(first)
print(second)
print(third)

#------------------

# numbers = [10,20,30,40,50]


# # first, *rest = numbers

# # print(first)
# # print(rest)

# #----------------

# first, *middle, last =numbers

# print("First:", first)
# print("Middle:", middle)
# print("Last:", last)

#------------------

# person = ("Ada", 36, "London")

# name, _, city = person

# print(name)
# print(city)
# print(_) # Actually prints 36 from ths list.

#-----------------------------

# first = [1,2,3]
# second = [*first, *second]

# combined = [*first, *second]

# print(combined)


# defaults =  {
#     "theme" : "light",
#     "language": "English"
# }

# user_settings = {
#     "language" : "Swedish",
#     "notifications" : True
# }

# settings = {
#     **defaults,
#     **user_settings
# }

# print(settings)


# #-----------------

# # Lambda functions

# def double(number):
#     return number *2

# print(double(5))

# # Or

# double = lambda number: number * 2 # Syntax: variable = lambda parameters colon expression

# print(double(5))



names = ["Anna", "Bob", "Charlie", "Ada"]

# print(sorted(names)) # Alphabetical order



# def get_length(name):
#     return len(name)

# sorted_names =sorted(names, key=get_length)

# print(sorted_names)


sorted_names = sorted(names, key=lambda name: len(name)) # Syntax: variable = lambda parameters colon expression

print(sorted_names)



# Sort Dictionaries

# students = [
#     {"name": "Anna", "score": 85},
#     {"name": "Bob", "score": 63},
#     {"name": "Charles", "score": 91}
# ]

# sorted_students = sorted(
#     students,
#     key=lambda student:student["score"])

# print(sorted_students)


# MAP

# numbers = [1, 2, 3, 4, 5]

# doubled = map(lambda number: number *2, numbers)

# print(doubled)

# doubled = list(map(lambda number: number *2, numbers))

# print(doubled)



# doubled = [number * 2 for number in numbers]

# print(doubled)



numbers = [1, 2, 3, 4, 5, 6]


# even_numbers = list(
#     filter(lambda number: number % 2 == 0, numbers)
# )

# print(even_numbers)

# Same thing with comprehension:

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)