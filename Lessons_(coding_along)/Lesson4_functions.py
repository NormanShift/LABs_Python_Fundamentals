#Second week of Python Fundamentals, 2026
#Functions and control flow

#Functions (reusable blocks of code that perform a specific task)

#Defining a function
def greet(name):
    print("Hello")

#Actually calling the function
greet("F")  # Output: Hello

# Parameters and arguments
def greet(name): # Parameter is "name". This is a placeholder for the value that will be passed to the function when it is called.
    print("Hello", name)

greet("Adam")  # argument is "Adam"


def introduce(name, age):
    print(name, "is", age, "years old.")

introduce("Adamant", 25)

# Keyword arguments example:
def introduce(name, age):
    print("Name", name)
    print("Age", age)

introduce(age=36, name="Mildred") # keyword arguments, order does not matter. Or, overriding the order of the parameters in the function definition.

def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    print("Tax amount:", tax)

calculate_tax(50000, 0.2)

def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax

# calculate_tax(50000, 0.2)
result = calculate_tax(50000, 0.2) # Store the returned value in a variable
print("Tax amount:", result)


# def add_with_print(a, b):
#     print(a + b)

# result = add_with_print(3, 5) # This will print 8, but the result variable will be None because the function does not return anything
# print("Result:", result) # Output: Result: None

# Proper way to define the function with a return statement
def add_with_print(a, b):
    return a + b

result = add_with_print(3, 5)
print("Result:", result)


def calculate_tax(income, tax_rate):
    return income * tax_rate

tax_amount = calculate_tax(50000, 0.2)

income_after_tax = 50000 - tax_amount # Income after tax is calculated by subtracting the tax amount from the income
print("Tax amount:", tax_amount)
print("Income after tax:", income_after_tax)

print(calculate_tax(50000, 0.2)) # Directly printing the returned value from the function without storing it in a variable


def example():
    print("Before return")
    return 10 # return statement ends the function execution and sends a value back to the caller
    print ("After return") # This line will not be executed because the function has already returned a value
result = example()
print("Result:", result) # Output: Result: 10


# def check_grade(score):
#     if score >= 70:
#         return "Pass"
#     else:
#         return "Fail"

# print(check_grade(85)) # Output: Pass
# print(check_grade(65)) # Output: Fail

""" def check_grade(score):
    if score >= 70:
        return "Pass" # Here the if statement ends with a return statement, so the function will exit and return "Pass" if the score is greater than or equal to 70

    return "Fail" # This line will be executed if the score is less than 70

print(check_grade(85)) # Output: Pass
print(check_grade(65)) # Output: Fail """


def get_first_item(items):
    return items[0]

languages = ["Python", "Java", "C++", "JavaScript"]

print(get_first_item(languages)) # Output: Python


def print_languages(languages):
    for language in languages:
        print(language)

my_languages = ["Python", "Java", "C++", "JavaScript"]
print_languages(my_languages) # Output: Python, Java, C++, JavaScript (each on a new line)

""" #Calculate something and return the result:
def count_passing_scores(scores):
    passed = 0
    for score in scores:
        if score >= 70:
            passed += 1

    return passed

scores = [85, 90, 65, 70, 55, 80]

result = count_passing_scores(scores)
print("Number of passing scores:", result) # Output: Number of passing scores: 4 """


""" def get_student_status(student):
    if student["score"] >= 70: # Dictionary key access to get the score of the student
        return "Pass"

    return "Fail"

# Dictionary representing a student with a name and score
student = {
    "name": "Alice",
    "score": 85
}

status= get_student_status(student)
print("Student status:", status) # Output: Student status: Pass """


# Separating the function definition and the function call for clarity. Separating responsibilities of the function and the data being passed to it. The function is defined to take a student dictionary as input and return their status based on their score. The student data is defined separately and passed to the function when called.
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 65},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 55}]

def get_student_status(student):
    if student["score"] >= 70:
        return "Pass"
    return "Fail"

for student in students: # The loop is responsible for iterating through each student in the list of students and calling the get_student_status function to determine their status based on their score.
    status = get_student_status(student) # The function is responsible for determining the status of each student based on their score. It returns "Pass" if the score is 70 or above, and "Fail" otherwise.
    print(f"{student['name']} has a score of {student['score']} and has {status}.")


def greet(name, greeting="Hello"):
    print(greeting, name) # Here the order is reversed to print the greeting and the name in the expected order.

greet("Alice", "Good morning") # But we still pass in the arguments "incorrect order" upon calling the function. The input (arguments) are reversed inside the function, giving the semantically correct output of: Good morning Alice


def greet(greeting = "Hello", name):
    print(greeting, name)

greet("Alice") # Output: Hello Alice


def create_user(name, role="student", active=True):
    print("Name:", name)
    print("Role:", role)
    print("Active:", active)

create_user("Alice") # Output: Name: Alice, Role: student, Active
create_user("Bob", role="admin") # Output: Name: Bob, Role: admin, Active: True
create_user("Charlie", active=False) # Output: Name: Charlie, Role: student, Active: False


def min_and_max(numbers):
    return min(numbers), max(numbers)

result = min_and_max([3, 5, 1, 8, 2])
smallest, largest = min_and_max([3, 5, 1, 8, 2])
print(result)
print(type(result)) # Output: (1, 8) <class 'tuple'>

print("Smallest:", smallest)
print("Largest:", largest)


# def min_and_max(numbers):
#     if not numbers: # Check if the list is empty
#         return None, None

#     min_value = numbers[0]
#     max_value = numbers[0]

#     for number in numbers:
#         if number < min_value:
#             min_value = number
#         elif number > max_value:
#             max_value = number

#     return min_value, max_value


# Functions calling functions:

def calculate_tax(income, tax_rate):
    return income * tax_rate

def calculate_total_with_tax(income, tax_rate):
    tax = calculate_tax(income, tax_rate) # Calling the previous function to calculate the tax amount
    return income - tax

result = calculate_total_with_tax(50000, 0.2)

print("Total with tax:", result)

#---------------------------------
numbers = [3, 5, 1, 8, 2] # Unsorted list of numbers

print(len(numbers)) # Built-in function len() returns the number of items in a list. Output: 5

numbers.sort() # A method belonging to the list object that sorts the list in place. Output: [1, 2, 3, 5, 8]

print(numbers) # Output: [1, 2, 3, 5, 8]

def get_first_item(items): # Function to get the first item from a list. It checks if the list is empty and returns None if it is, otherwise it returns the first item.
    if not items: # Check if the list is empty
        return None
    return items[0]

print(get_first_item(numbers)) # Output: 1


# type hints (not enforced at runtime, but useful for documentation and static analysis):

def add(a: int, b: int) -> int: # Function that takes two integers and returns an integer. The type hints indicate the expected types of the parameters and the return type.
    return a + b

print(add(3, 5))

print(add("Hello ", "world!")) # Output: Hello, world! (This works because Python is dynamically typed, but it goes against the type hints provided in the function definition.)


# docstrings (documentation strings) are used to describe what a function does. They are enclosed in triple quotes and can be accessed using the __doc__ attribute of the function.

def calculate_area(width, height):
    """Calculate the area of a rectangle given its width and height."""
    return width * height

# print(calculate_area(5, 10)) # Output: 50
print(calculate_area.__doc__) # Docstrings Dunder-funcion. Output: Calculate the area of a rectangle given its width and height.