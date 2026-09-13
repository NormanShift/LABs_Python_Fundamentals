# Lesson 3

print(5 > 3)  # True
print(5 < 3)  # False
print(5 >= 3)  # True. Greater than or equal to.
print(5 <= 3)  # False. Less than or equal to.
print(5 == 3)  # False
print(5 != 3)  # True


number = 10 # Assignement of a variable
print(number == 10)  # True. Double equal sign is used for comparison, not assignment.

print(1 == 1)  # True
print(1 == '1')  # False
print('1' == '1')  # True


# and, or, not      ( && || ! )

# AND (all conditions true will give us true)
age = 25
has_ticket = True

print(age > 18 and has_ticket)  # True. Both conditions are true.
print(age >= 18 or has_ticket)  # True. At least one condition is true

# OR

is_admin = False
is_teacher = True

print(is_admin or is_teacher)  # True. At least one condition is true.

# NOT (reverses the boolean value)

is_logged_in = False

print(is_logged_in)  # False. The value of is_logged_in is False.
print(not is_logged_in)  # True. Negates the value of is_logged_in.

# IN (can be used as a condition)

languages = ["Python", "Java", "C#"]

print("Python" in languages) # Returns true
print("Rust" in languages) # False
print("Rust" not in languages) # Here in reverses the first condition (not). Returning True (which is incorrect!).
# Also, strings are case sensitive (in this case).


# Indentation (Tab or four white spaces.)
# if/elif/else

""" age = 20

if age >= 18:
    print("Adult")
else:
    print("Under 18") """


# If the condition is true, the following conditions are skipped:
score = 90

if score >= 90:
    print("Grade A")
elif score >= 80:
    print(("Grade B"))
elif score >= 70:
    print("Grade C")
else:
    print("Below C")


# Nesting (can be hard do read though).
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    if has_ticket:
        print("You may enter!")
    else:
        print("You need a ticket!")
else:
    print("Entry denied, you are too young!")


# Falsy -> empty-string,/list/zero/null

name = "" # empty values are treated as False

if name:
    print("We have a name")
else:
    print("The name is empty")


items = []

if items:
    print("The list contains data")
else:
    print("The list is empty")


# For loop

languages = ["Python", "Java", "C#", "JavaScript"]

""" Avoid repetition:
print(languages[0])
print(languages[1])
print(languages[2])
print(languages[3]) """

for language in languages:
    print(language)


word = "Python" # Strings are iterable

for character in word:
    print(character)


numbers = [3, 8, 12, 5, 20, 7]

for number in numbers:
    if number >= 10:
        print(number)


numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)

# Dictionary
student = {
    "name" : "Ada",
    "age" : 25,
    "course" : "Ai Developer"
}

for key in student:
    print(key)
    print(key, student[key])

# Unpacking
for key, value in student.items():
    print(key,value)


students = [
    {"name": "Anna", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91}
    ]


for student in students:
    print(student["name"])

for number in range(2, 10, 2): # The last number is excluded
    print(number)


languages = ["Python", "Java", "C#", "JavaScript"]

# for i in range(len(languages)):
#     print(languages[i])
# # or
# for language in languages:
#     print(language)

for index, language in enumerate(languages):
    print(index, language)


# While loops

count = 1

while count <= 5:
    print(count)
    count += 1


# Infinite loop

# while count <= 5:
#     print(count)


# break and continue
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number%2 != 0:
        print("Found an odd number:")
        break

for number in numbers:
    if number == 3:
        continue
    print(number)