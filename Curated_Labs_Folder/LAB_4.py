# Part A - Function fundamentals

# A:1
def greet(name):
    print("Hello", name)

def show_course_name(course_name):
    print("Course Name:", course_name)

def print_separator():
    print("-" * 30)

print_separator() # Output: ------------------------------
greet("Alice")
show_course_name("Python Programming")
print_separator()
greet("Bob")
show_course_name("Data Science")
print_separator()

# A:2 to 4
def greet_person(name): # Here, 'name' is a parameter of the function 'greet_person'.
    print("Hello", name)

def introduce(name, age):
    print(name, "is", age, "years old.")

introduce("Adamant", 25) # Arguments are passed into the function parameters. In this example, the order of the arguments matters.
greet_person("Charlie") # Calling the function with an argument just for sports. :))


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

Addition = add(10, 5)
Subtraction = subtract(10, 5)
Multiplication = multiply(10, 5)
Division = divide(10, 0)  # This will return an error message for division by zero

print("Addition:", Addition)
print("Subtraction:", Subtraction)
print("Multiplication:", Multiplication)
print("Division:", Division)

# A:5
def calculate_area(length, width):
    return length * width

area = calculate_area(10, 5) # The actual calculation is done inside the function, and the result is returned to the variable 'area'.
print("Area:", area)


# Part B - Return values

# B:1
def is_even(number):
    return number % 2 == 0 # "==" the comparison returns a bool. Because the comparison operator is being used, it returns a bool.

number = is_even(6)

# print(type(number))
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False


# B:2
def get_larger(a, b):
    if a > b:
        return a
    else:
        return b

print(get_larger(7, 4)) # Returns 7


# B:3
def classify_score(score):
    if score >= 70:
        print("Pass")
    else:
        print("Fail")

classify_score(70)
classify_score(68)


# B:4
def full_name(first_name, last_name):
    f_name = (f"Hi there {first_name} {last_name}.")

    return f_name

full_name("Andy", "Billgerer")


# B:5
def calculate_discount(price, percent):
    discount = price * percent
    final_price = price - discount
    return final_price

discounted_price = calculate_discount(50000, 0.3)

print(f"Special price, for yoo: {discounted_price}")


# B:6
# Using return vs not using return - when using return we can then store the ouput of a function verses only printing the output to the console.
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

# Part C - Defaults and keyword arguments

# C:1
def greet(name, greeting='Hello'):
        print(greeting, name) # Here the order is reversed to print the greeting and the name in the expected order.

greet("Alice", "Good morning") # But we still pass in the arguments "incorrect order" upon calling the function. The input (arguments) are reversed inside the function, giving the semantically correct output of: Good morning Alice

# C:2
def calculate_price(price, quantity = 1, discount=0):
    discount = price * discount
    discounted_price = price - discount
    total = discounted_price * quantity
    return total

total_price = calculate_price(3000, 5, 0.3)
print(total_price)

# C:3
def create_profile(name, city='Unknown', active=True):
    # profile = {
    #     "name": name,
    #     "city": city,
    #     "active": active
    # }
    # return profile
    return {
        "name": name,
        "city": city,
        "active": active
        }

profile1 = create_profile("Alice", "Detroit") 
profile2 = create_profile("City", city="Chicago", active=True) 
profile3 = create_profile("Charlie", active=False)

print("The following profiles were created:\n")
print(profile1)
print(profile2)
print(profile3)

# C:4
def orderly(param_1=2, param_2=20, param_3=40):
    out_put = param_1 * param_2 + param_3

    return out_put

unorderly = orderly(param_3=70, param_1=3, param_2=9)

print(unorderly)