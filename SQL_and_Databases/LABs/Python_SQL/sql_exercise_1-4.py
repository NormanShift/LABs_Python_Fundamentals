# Exercises: Python and personal data

import sqlite3

conn = sqlite3.connect('webshop.db') # Connect to the database
cursor = conn.cursor() # Create a cursor object to execute SQL queries

# e1:

""" 
cursor.execute('''SELECT first_name, last_name, city from customers''') # Queries goes within the execute method, and the result is stored in the cursor object
for first_name, last_name, city in cursor.fetchall():
    name = f"{first_name} {last_name}"
    city = city if city is not None else "Unknown"
    print(f"Cust: {name:<18} City: {city:<10}") # Format the output nicely with left-aligned name and right-aligned price

conn.close()
 """

# e2:

user_input = input("Enter your budget max: ")
budget_max = float(user_input)

cursor.execute('''SELECT name, price from products where price <= ?''', (budget_max,)) # Use parameterized query to prevent SQL injection
for name, price in cursor.fetchall():
    print(f"Prod: {name:<20} Price: {price:>8.2f} kr") # Format the output nicely with left-aligned name and right-aligned price

conn.close()


# e3:

user_input = input("Enter a category: ")
category = user_input