# Exercises: Python and personal data

import sqlite3

conn = sqlite3.connect('webshop.db') # Connect to the database
cursor = conn.cursor() # Create a cursor object to execute SQL queries

# e1:

cursor.execute('''SELECT first_name, last_name, city from customers''') # Queries goes within the execute method, and the result is stored in the cursor object
for first_name, last_name, city in cursor.fetchall():
    name = f"{first_name} {last_name}"
    city = city if city is not None else "Unknown"
    print(f"Cust: {name:<18} City: {city:<10}") # Format the output nicely with left-aligned name and right-aligned price

conn.close()

# e2: