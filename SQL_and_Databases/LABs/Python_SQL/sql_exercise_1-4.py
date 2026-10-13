# Exercises: Python and personal data

import sqlite3

conn = sqlite3.connect('webshop.db') # Connect to the database
cursor = conn.cursor() # Create a cursor object to execute SQL queries

#----------------------------------
# e1:

""" 
cursor.execute('''SELECT first_name, last_name, city from customers''') # Queries goes within the execute method, and the result is stored in the cursor object
for first_name, last_name, city in cursor.fetchall():
    name = f"{first_name} {last_name}"
    city = city if city is not None else "Unknown"
    print(f"Cust: {name:<18} City: {city:<10}") # Format the output nicely with left-aligned name and right-aligned price

conn.close()
 """

#----------------------------------
# e2:

""" user_input = input("Enter your budget max: ")
budget_max = float(user_input)

cursor.execute('''SELECT name, price from products where price <= ?''', (budget_max,)) # Use parameterized query to prevent SQL injection
for name, price in cursor.fetchall():
    print(f"Prod: {name:<20} Price: {price:>8.2f} kr") # Format the output nicely with left-aligned name and right-aligned price

conn.close() """

#----------------------------------
# e3:

category = input("Available categories: Clothing, Accessories, Shoes\nEnter a product category: ")

cursor.execute(
    '''SELECT COUNT(*) FROM products WHERE category = ?''',
    (category,)
)

product_count = cursor.fetchone()[0]

print(f"Category: {category}, Number of products: {product_count}")

conn.close()

#----------------------------------
# e4:

"""
Building an SQL query with an f-string is ill adviced because user input
becomes part of the SQL code.
A malicious hacker or unexpected input could therefore change the intended output of the query, which is refered to as "SQL injection".

A ? placeholder is safer because the SQL command and the supplied value are
handled separately. The input is treated as data rather than executable SQL.
"""

#----------------------------------
# e5:

