# First lab exercise for Python fundamentals

# Part A - Warm-up: Python basics

# A1.
print("Christian Norman\nPython Fundamentals\nLesson 1 - Revisiting the basics\n")

# A2.
name = "Kalle Karlsson"
age = 25
height = 1.75
student = True

print(type(name), " Name:", name)
print(type(age), "Age:", age)
print(type(height), "Height:", height)
print(type(student), "Is a student:", student)

# A3.
print(type(age), "Age:", age)
float_age = float(age)  # Convert age to float
print(type(float_age), "Age as float:", float_age)

# A4.
a = 10
b = 3

print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Product: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor div: a // b =", a // b)
print("Modulo: a % b =", a % b)
print("Power: a ** b =", a ** b)

# A5.
#Example 1:3:
name = "Kalle Karlsson"
user_input = "25"
number = 10

user_input_c = int(user_input)
number_f = float(number)
number_s = str(number)

print(type(user_input), "User input as string:", user_input)
print(type(user_input_c), "User input as integer:", user_input_c)

print(type(number), "Number as integer:", number)
print(type(number_f), "Number as float:", number_f)

print(type(number), "Number as integer:", number)
print(type(number_s), "Number as string:", number_s)


# Part B - User input and calculations

# B:1.
user_name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2026
age = current_year - year_of_birth

print(f"Greetings {user_name}, you are {age} years old.")

# B:2.
item_price = float(input("Enter the price of the item: "))

discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = item_price * (discount_percentage / 100)
final_price = item_price - discount_amount

print(f"The final price of the item is: ${final_price:.2f}")

# B:3.
temperature_celsius = float(input("Enter the temperature in Celsius: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {temperature_fahrenheit:.2f}")

# B:4.
length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the room is: {area:.2f} square units")
print(f"The perimeter of the room is: {perimeter:.2f} units")

# B:5. Extend one of the previous exercises to include error handling for user input. For example, if the user enters a non-numeric value for the year of birth, the program should catch the error and prompt the user to enter a valid number.

# Part C - Strings

# C:1.
sentence = "  Python is a powerful programming language.  "

print(len(sentence))  # Length of the string
print(sentence.upper())  # Convert to uppercase
print(sentence.lower())  # Convert to lowercase
print(sentence.strip())  # Remove leading and trailing whitespace

# C:2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Your full name is: {full_name}")

# C:3

string_slicing = "python programming"
print(string_slicing[0])  # Extract the first character
print(string_slicing[-1])  #Extract the last character
print(string_slicing[0:6])  # Extract a substring (first 6 characters). The last index is exclusive, so it extracts characters from index 0 to 5.
print(string_slicing[-11:])  # Extract a substring (last 11 characters). The last index is exclusive, so it extracts characters from index -11 to the end of the string.
print(string_slicing[::-1])  # Extract the string in reverse order with slicing. The step value of -1 reverses the string.

# C:4
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_name_stripped = first_name.strip()  # Remove leading and trailing whitespace
last_name_stripped = last_name.strip()  # Remove leading and trailing whitespace

gen_username = first_name_stripped[:3].lower() + last_name_stripped[:5].lower()  # Concatenate the stripped first and last names to create a username in lowercase

print(f"Your full name is: {first_name_stripped} {last_name_stripped}")
print(f"Your username is: {gen_username}")

# C:5
email_address = input("Enter your email address: ").strip()

username, domain = email_address.split("@")  # Split the email address into username and domain using the "@" symbol as the delimiter
print(f"Username: {username}")
print(f"Domain: {domain}")

# C:6
heated_string = "Java is a powerful programming language."

replaced_string = heated_string.replace("Java", "Python")  # Replace the word "Java" with "Python" in the string
print(heated_string)
print(f"Replaced string:\n{replaced_string}")


# Part D - String investigation

# D:1
text = "Python"
# expression 1
text[0] # Prediction: "P". Extracts the character at index 0, which is the first character of the string.
# expression 2
text[2] # Prediction: "t". Extracts the character at index 2.
# expression 3
text[-1] # Prediction: "n". Extracts the last character of the string.
# expression 4
text[-2] # Prediction: "o". Extracts the character at index -2.
# expression 5
text[1:4] # Prediction: "yth". Extracts characters from index 1 to index 4 (exclusive), which includes characters at indices 1, 2, and 3.
# expression 6
text[:3] # Prediction: "Pyt". Extracts characters from the beginning of the string up to index 3 (exclusive).
# expression 7
text[3:] # Prediction: "hon". Extracts characters from index 3 to the end of the string.
# expression 8
text[::2] # Prediction: "Pto". A stepping of 2 means it takes every second character from the string, starting from the first character.
# expression 9
text[::-1] # Prediction: "nohtyP". Reverses the string by using a step of -1, which means it starts from the end and goes to the beginning.

# D:2

