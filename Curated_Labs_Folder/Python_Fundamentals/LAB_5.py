# ============================================================
# LAB 5 (made available on 2026-09-15)
# ============================================================

# Part A - Scope

# A:1
# Create a global variable course_name and a function that
# creates a local variable with the same name.
# Print both and explain the result.

course_name = "Python Fundamentals"

def show_course_name():
    course_name = "Python Advanced"
    print("Inside the function:", course_name)


show_course_name()
print("Outside the function:", course_name)

# Explanation:
# The course_name created inside the function is a local variable.
# It is separate from the global variable with the same name.
# Python uses the local variable inside the function.
# The global course_name variable remains unchanged.

# ------------------------------------------------------------
# A:2
# Create a function with a local counter and show that it does
# not remain available outside the function.

def use_local_counter():
    counter = 0
    counter += 1
    print("Counter inside the function:", counter)


use_local_counter()

# The following line would cause a NameError because counter
# exists only inside use_local_counter().
#
# print("Counter outside the function:", counter)

# Explanation:
# counter is created inside the function, so it belongs to the
# function's local scope. It is unavailable outside the function.

# ------------------------------------------------------------
# A:3
# Attempt to modify a global numeric variable without global.
# Describe the problem, then return the new value instead.

total = 100


# This version deliberately demonstrates the problem.
# Leave it commented out so that the rest of the file can run.

# def add_tax():
#     total = total * 1.25
#     return total
#
#
# total = add_tax()

# Explanation:
# Because total is assigned a value inside add_tax(), Python
# treats total as a local variable throughout the function.
# The right side tries to read that local total before it has
# received a value, causing an UnboundLocalError.

# Cleaner version using a parameter and return:

def add_tax(amount):
    return amount * 1.25

total = add_tax(total)
print("Total after tax:", total)

# The global total is passed into the function as an argument.
# Inside the function, its value is stored in the local parameter
# amount. The new value is returned and assigned back to total.

# ------------------------------------------------------------
# A:4
# Create a nested function and demonstrate a simple
# enclosing-scope lookup.

def outer_function():
    message = "Hello from the enclosing scope (/function)"

    def inner_function():
        print(message)

    inner_function()

outer_function()

# Explanation:
# inner_function() does not have its own variable called message.
# Python therefore looks one level outward and finds message in
# the local scope of outer_function().
# For inner_function(), outer_function() is the enclosing scope.

# ------------------------------------------------------------
# A:5
# Create examples that avoid shadowing built-in names such as
# list, str, sum, and max.

number_list = [10, 20, 30]
message_text = "Python"
total_sum = sum(number_list)
maximum_value = max(number_list)

print("Number list:", number_list)
print("Message text:", message_text)
print("Total sum:", total_sum)
print("Maximum value:", maximum_value)

# These names would shadow Python's built-in functions in the current scope.

# ------------------------------------------------------------
# Part B - *args

# B:1
def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_all(10, 20))
print(add_all(10, 20, 30))
print(add_all(1, 2, 3, 4, 5))

# ------------------------------------------------------------
# B:2
# Returns None when no numbers are supplied.

def average(*numbers):
    if not numbers:
        return None

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

print(average(10, 20, 30))
print(average(5, 10, 15, 20))
print(average())

# ------------------------------------------------------------
# B:3
# Return the longest supplied word.

def longest_word(*words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word("cat", "elephant", "giraffe", "dog"))
print(longest_word("Python", "Java", "JavaScript"))

# ------------------------------------------------------------
# B:4
# Join all supplied words using the supplied separator.

def build_sentence(separator, *words):
    return separator.join(words)


print(build_sentence(" ", "Python", "is", "fun"))
print(build_sentence("-", "one", "two", "three"))
print(build_sentence(", ", "Ada", "Grace", "Guillermo"))

# ------------------------------------------------------------
# B:5

def describe_scores(student_name, *scores):
    number_of_scores = len(scores)

    if not scores:
       return f"{student_name}: no scores supplied"

    total = 0

    for score in scores:
        total += score

    average_score = total / number_of_scores

    return (
        f"Student: {student_name}, "
        f"number of scores: {number_of_scores}, "
        f"average: {average_score:.2f}"
    )

print(describe_scores("Ada", 85, 90, 78))
print(describe_scores("Grace", 100, 95, 98, 91))
print(describe_scores("Guillermo"))


# ------------------------------------------------------------
# Part C - Positional unpacking

# C:1
# Create a list and unpack it into a function expecting three positional parameters.

def add_three_numbers(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

result = add_three_numbers(*numbers)

print("Sum:", result)

# ------------------------------------------------------------
# C:2
# Create a tuple containing first_name, last_name city. Call the funtion using *tuple.

def introduce_person(first_name, last_name, city):
    return f"{first_name} {last_name} lives in {city}."

# tuple = ("Ada", "Lovelace", "London") # Built-in type name or function, do not use!
person = ("Ada", "Lovelace", "London")

# print(type(person)) # Just checking to be sure.

# introduction = introduce_person(*tuple) # Well, this does not work!
introduction = introduce_person(*person)

print(introduction)

# ------------------------------------------------------------
# C:3
# Use starred assignment: first, *middle, last = values. Test with several list lengths.

values1 = [10, 20, 30, 40, 50]

first, *middle, last = values1

print("First:", first)
print("Middle:", middle)
print("Last:", last)


values2 = ["Ada", "Grace", "Kallur", "Baldur", "Guillermo"]

first, *middle, last = values2

print("First:", first)
print("Middle:", middle)
print("Last:", last)


values3 = [100, 200]

first, *middle, last = values3

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# --------------------------------------
# C:4
# Explain the difference between * in a function definition
# and * in a function call.

# In a function definition, * collects or packs multiple positional arguments into a tuple.

def show_numbers(*numbers):
    print("Packed tuple:", numbers)

show_numbers(10, 20, 30)

# In a function call, * unpacks a list or tuple into separate positional arguments.

def multiply_three_numbers(a, b, c):
    return a * b * c

# values = [1, 2] # Here the number of elements (becomes input arguments during the function call) does not match up with the input parameters of the function being called. Which produces a "TypeError".
values = [2, 3, 4]

product = multiply_three_numbers(*values)

print("Product:", product)

# --------------------------------------
# Part D - **kwargs

# D:1
# Display all supplied profile information.

def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_profile(
    name="Ada",
    age=36,
    city="London",
    language="Python"
)


# D:2
# Return one dictionary containing the username and all other details.

def create_user(username, **details):
    user = {"username": username}

    for key, value in details.items():
        user[key] = value

    return user


user1 = create_user(
    "ada123",
    age=36,
    city="London",
    language="Python"
)

print(user1)


# D:3
# Return a product dictionary containing its name, price and metadata.

def build_product(name, price, **metadata):
    product = {
        "name": name,
        "price": price
    }

    for key, value in metadata.items():
        product[key] = value

    return product


product1 = build_product(
    "Keyboard",
    799,
    brand="Logitech",
    colour="Black",
    available=True
)

print(product1)


# D:4
# Return only settings whose values are not None.

def filter_settings(**settings):
    filtered_settings = {}

    for key, value in settings.items():
        if value is not None:
            filtered_settings[key] = value

    return filtered_settings


active_settings = filter_settings(
    theme="Dark",
    language="English",
    notifications=None,
    volume=80,
    location=None
)

print(active_settings)


# D:5
# Unpack a dictionary into a function with named parameters.

def introduce(name, age, city):
    return f"{name} is {age} years old and lives in {city}."


person = {
    "name": "Ada",
    "age": 36,
    "city": "London"
}

print(introduce(**person))