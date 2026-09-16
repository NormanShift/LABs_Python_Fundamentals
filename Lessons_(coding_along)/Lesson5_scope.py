# message = "Hello from global scope" # global scope

# def greet():
#     print(message)

# greet()


# message = "Global message"

# def greet():
#     message = "Local message"
#     print(message)


# greet() # Prints the data of the functions message variable

# print(message) # Prints a diffrent variable (Global)


# Parameters actually works as variables locally within the function.
# def greet(name):
#     message = "Hello" + name
#     print(message)


# greet("Ada")

# print(name) # Gives an error


# Lookup rule -> LEGB

# L - Local
# E - Enclosing
# G - Global
# B - Built-in


# name = "Global Ada"

# def greet():
#     name = "Local Grace"
#     print(name)

# greet() # Here Python looks for the local scope.


# numbers = [1, 2, 3]

# print(len(numbers)) # Built-in:s


# Built-in:s:
# list = [1, 2, 3]

# print(list)

# new_list = list("Python")

# Avoid:
# list
# str
# int
# print
# sum
# max


# Local scope with nested function(s) ("extreme example"):
# def outer():
#     message = "Hello from outer"

#     def inner():
#         print(message)

#     inner()

# outer()



# counter = 0

# def increase_counter():
#     counter = 1
#     print("Insidde:", counter)

# increase_counter()

# print("Outside:", counter)


""" This example is incomplete, screenshot available
counter = 0

def increase_counter():
    global counter # Global keyword
    counter = 1

increase_counter()

print(counter)


counter = 0

def increase_counter():
    increase_counter + 1 """



# x = 10

# def example():
#     x = 20
#     print("Inside:", x)

# example()

# print("Outside:", x)



# total = 100

# def add_tax():
#     total = total * 1.25
#     return total

# add_tax()

# Rewrite the function without using the global keyword (and don't change variable names):

# total = 100

# def add_tax(total):
#     total = total * 1.25
#     return total

# add_tax(1000)


# *args explained (actually the standard convention):
# def add_number(a, b, c, d):
#     return a + b + c + d

# print(add_number(10, 20, 30, 40))

# Actual example using *args
# def show_numbers(*args):
#     print(args)

# show_numbers(10, 20, 40) # Returns a touple
# show_numbers(1, 3)
# show_numbers(3)
# show_numbers(1, 2, 3, 4, 5)



# def show_names(*args):
#     for name in args:
#         print(name)


# show_names("Ada", "Grace", "Guillermo")



# def add_numbers(*args):
#     total = 0

#     for number in args:
#         total += number

#     return total

# print(add_numbers(10, 20))
# print(add_numbers(10, 20, 30))
# print(add_numbers(10, 20, 40, 50))



def calculate_total(discount, *prices):
    total = 0

    for price in prices:
        total += price

    return total * (1 - discount)

print(calculate_total(0.10, 100, 200, 300)) # The first arg goes into the first parameter (input) of the function and the following values goes into the *args (*prices in this example).

# Useful
# -the function should accept several positional values
# -the exact number of values is not known in advance


# Better:

def calculate_area(width, height):
    return width *height

# less clearer or less flexible

def calculate_area(*area):
    return args[0] * args[1]


# Unpacking with *

def add_three(a, b, c):
    return a + b + c

numbers = [10, 30, 50]

print(add_three(numbers)) # This won't work

print(add_three(*numbers)) # Unpacks the list, of parameters (inputs), kind of in reverse.


values = (5, 10, 16) # Defining a tuple

print(add_three(*values)) # Unpacking that tuple


# **kwargs (expanding on the *args)

def show_user(**kwargs):
    print(kwargs)

show_user(name="Ada", age=36, city="London") # **kwargs outputs a dictionary.


def show_user(**kwargs):
    print("Name:", kwargs["name"])
    print("Name:", kwargs["age"])

show_user(name="Ada", age = 36)
show_user(name="Ada") # Will give a key error.



def show_user(**kwargs):
    print("Name:", kwargs.get["name", "unknown"])
    print("Name:", kwargs.get["age", "unknown"])
    print("Name:", kwargs.get["city", "unknown"])


show_user(name="Ada", age=36)



def show_information(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_information(name="Ada",
                 age=37,
                 city="London",
                 language="Python")







