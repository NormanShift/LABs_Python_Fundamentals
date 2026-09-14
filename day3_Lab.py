# Day 3 : Lab 3
# Part A - Conditions

# A:1
signed_or_not = -6

print(f"Is number positive: {signed_or_not <= 0}")
print(f"Is number positive: {signed_or_not >= 0}")

# A:2
age = int(input("Enter your age: "))

if age < 7:
    print("Kinder")
elif age < 13:
    print("Getting there")
elif age < 20:
    print("In your teens")
else:
    print("Getting older")

# A:3

username = input("Username: ")
password = input("enterDrag0n: ")

if username == "baldwin" and password == "enterDrag0n":
    print("You entered the Matrix!")
else:
    print("Wrong credentials!")

# A:4

# If the condition is true, the following conditions are skipped:
score = int(input("Enter your score (0–100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 65:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Grade E")


# A:5

member_input = (input("Member (yes or no)?")).strip().lower()
member = member_input == "yes"

print(type(member))

order_total = float(input("Enter Amount: "))

if (member and order_total >= 50) or order_total >= 50:
    print("Shipping is underway")
else:
    print("Please Register or increase the order total ($50 minimum).")


# A:6

print(5 > 3)  # True. Greater than.
print(5 < 3)  # False. Less than.
print(5 >= 3)  # True. Greater than or equal to.
print(5 <= 3)  # False. Less than or equal to.
print(5 == 3)  # False. Equals.
print(5 != 3)  # True. Not equal to.


# Part B - Truthy, falsy and membership

# B:1

empty_string = ""
non_empty_string = "Fuller!"
zero_int = 0
signed_int = 10
empty_list = []
non_empty_list = [1, 20, 40, 60, 80]

if empty_string:
    print("The empty string is True")
else:
    print("The empty string is False")

if non_empty_string:
    print("The non-empty string is True")
else:
    print("The non-empty string is False")

if zero_int:
    print("The zero integer is True")
else:
    print("The zero is integer False")

if signed_int:
    print("The non-zero integer is True")
else:
    print("The non-zero integer is False")

if empty_list:
    print("The empty list is True")
else:
    print("The empty list is False")

if non_empty_list:
    print("The non-empty list is True")
else:
    print("The non-empty list is False")

# Can also be tested like
print(bool(empty_string)) # False
print(bool(non_empty_string)) # True


# B:2

languages = ["Python", "Java", "C#"]

print("Python" in languages) # Returns true
print("Rust" in languages) # False
print("Rust" not in languages) # Here in reverses the first condition (not). Returning True (which is incorrect!).
# Also, strings are case sensitive (in this case).


# B:3

blocked_users = ["alfred", "cilla", "grinda", "patruck"]
#blocked_users = ["alfred1", "cilla1", "grinda1", "patruck1"]

ask_username = input("Enter username: ").strip().lower()

if ask_username in blocked_users:
    print("Blocked (u fogger)!")
else:
    print(">>> Access Granted >>>")

""" Or, but probably not the expected solution:
if ("alfred" in blocked_users
    or "cilla" in blocked_users
    or "grinda" in blocked_users
    or "patruck" in blocked_users):
    print("Blocked!")
else:
    print("Pass!") """


# B:4

logged_in = False
account_locked = False

if not logged_in: # not reverses the condition
    print("Please log in")

if not account_locked: # not flips False to True
    print("Your account is unlocked")


# Part C - For loops

# C:1

names_list = ["Grinda", "Cilla", "Gober", "Aakrid", "Leroy"]

for i, name in enumerate(names_list, start=1):
    print(f"{i} Greetings {name}!")

# C:2

numbers = range(1, 51)

print("Even numbers:")

for number in numbers:
    if number %2==0:
        print(number)


# C:3

summerize = [2, 5, 7, 8]

total = 0

for number in summerize:
    total = total + number

print(total)


# C:4

# Find the smallest number in a list
numbers = [2, 5, 7, 80, 10, 12, 15]

largest = 0

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is:", largest)


# C:5

list_of_words = ["apple", "pineapple", "banana", "cherry","cherrypie", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine"]

for word in list_of_words:
    if len(word) > 5:
        print(f" Word with more than 5 characters: {word}")
else:
    print("All words in the list of words have been checked.")


# C:6

list_of_scores = [95, 82, 67, 45, 88, 73, 59, 27]

passes = 0
fails = 0

for score in list_of_scores:
    if score > 70:
        passes += 1
    else:
        score < 70
        fails += 1

print(f"Number of passes: {passes}")
print(f"Number of fails: {fails}")


# C:7

dictionary = {
    "name": "Ada Gilmore",
    "age": 30,
    "city": "New York",
    "occupation": "Software Engineer"
}

# gender = dictionary.get("gender", "The entered key does not exist in the dictionary.")

for key, value in dictionary.items():
    print(f"{key}: {value}")

for key in dictionary:
    print(f"{key}: {dictionary[key]}")

for key in dictionary.keys():
    print(f"{key}: {dictionary[key]}")

print(key, dictionary[key])
print(dictionary.values())
print(dictionary.items())
# print (gender)


# Part D - range, enumerate and nested loops

# D:1
for number in range(10, 0, -1): # The last number is excluded
    print(number)

# D:2
input_int = int(input("Enter a number (1-10): "))

for number in range(1, 11):
    m_table = input_int * number
    print(f"{input_int} x {number} = {m_table}")

# D:3

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E", "Song F", "Song G", "Song H", "Song I", "Song J"]
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")

# D:4
# Nested loops coordinates example
for x in range(1, 4):
    for y in range(1, 5):
        print(f"({x}, {y})")

# D:5
# Simple 5x5 text grid using nested loops

for x in range(1, 2):
    for y in range(1, 6):
        continue
for z in range(1, 2):
    for y in range(1, 6):
        for z in range(1, 2):
            print(f"{x}, {y}, {z}, {y}, {z}")