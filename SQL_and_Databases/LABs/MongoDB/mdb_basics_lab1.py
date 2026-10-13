# Exercises: MongoDB basics - Day 1 - LEXICON HT2026
# Running this script will connect to the MongoDB server, access the 'webshop' database, and perform various queries on the 'products' and 'customers' collections.

from datetime import datetime
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # Connect to the MongoDB server
db = client['webshop']  # Access the 'webshop' database

print(client.list_database_names())  # List all databases on the server

# e1:

for product in db.products.find({"category": "Accessories"}):  # Retrieve documents from the 'products' collection where the category is 'accessories'
    print(product["name"])


# e2:
for customer in db.customers.find({"city": "Göteborg"}):  # Retrieve documents from the 'customers' collection where the city is 'Göteborg'
    print(customer["first_name"], customer["last_name"])  # Print the first and last names of each document in the 'customers' collection


# e3:
for product in db.products.find():
    print(product["name"], product["price"])  # Print the name and price of each document in the 'products' collection


# e4:
count = db.customers.count_documents({"city": "Uppsala"})

print("Number of customers in Uppsala:", count)


# e5:
find_one_result = db.products.find_one({"name":"Sandals"})
print("Sandals in stock:",find_one_result.get("stock"))


# e6:
for customer in db.customers.find():
    if customer.get("newsletter") == True:
        print(customer["first_name"], "gets the newsletter")  # Print the first name of each document in the 'customers' collection where the newsletter field is True

# e7:
insert_self = db.customers.insert_one({"first_name": "Christian", "last_name": "Norman", "email": "christian.norman@slottington.se", "city": "Fööruurten", "joined": datetime(2026,10,13), "newsletter": True, "phone": "070-1234567"})  # Insert a new document ("myself") into the 'customers' collection
print("Inserted myself without _id:", insert_self.inserted_id)  # Print the _id of the inserted document
find_oneself = db.customers.find_one({"first_name": "Christian", "last_name": "Norman"})

pprint(find_oneself)  # Pretty print the document that was just inserted into the 'customers' collection


# e8:
