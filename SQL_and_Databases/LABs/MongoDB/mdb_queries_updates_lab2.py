# Exercises: MongoDB - Queries and Updates - Day 2 - LEXICON HT2026

#from datetime import datetime
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['webshop']

#-----------------------------------------------------

# print(client.list_database_names())  # List all databases on the server

# print(db.list_collection_names())  # List all collections in the 'webshop' database

#-----------------------------------------------------

# e1:

name_price = database.products.find({"price": {"$gt": 1000}}, {"name": 1, "price": 1 }) # I didn't use "_id": 0 here since the print statement below only gives name and price anyway, but it could be used to exclude the _id field from the output if desired. 

for product in name_price:
    print(product["name"], product["price"])  # Print the name and price of each document in the 'products' collection where the price is greater than 1000

#-----------------------------------------------------

# e2:

undelivered_orders = database.orders.find({"status": {"$ne": "delivered"}}, {"_id": 1, "status": 1}) # $ne means not equal to.

# for order in undelivered_orders:
#     print(order["_id"], order["status"])

for order in undelivered_orders:
    print(order) # The ouput is not as pretty here (in my opinion).

#-----------------------------------------------------

# e3:

city_project = database.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}, {"_id": 0, "first_name": 1, "last_name": 1, "city": 1})

for customer in city_project:
    print(customer)

#-----------------------------------------------------

# e4:

color_wq = database.products.find({"details.color": "white"}, {"_id": 0, "name": 1, "details": "white"})

for product in color_wq:
    print(product)

#-----------------------------------------------------

# e5:

products_sport = database.products.find({"tags":"sport"}, {"_id": 0, "name": 1, "tags": 1}) # Here we are searching in arrays under the tags field.

for product in products_sport:
    print(product)

#-----------------------------------------------------

# e#:

