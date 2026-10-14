# Exercises: MongoDB - Queries and Updates - Day 2 - LEXICON HT2026

from datetime import datetime
# from pprint import pprint
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['webshop']

#-----------------------------------------------------

# print(client.list_database_names())  # List all databases on the server

# print(db.list_collection_names())  # List all collections in the 'webshop' database

#-----------------------------------------------------

# e1:

# name_price = database.products.find({"price": {"$gt": 1000}}, {"name": 1, "price": 1 }) # I didn't use "_id": 0 here since the print statement below only gives name and price anyway, but it could be used to exclude the _id field from the output if desired. 

# for product in name_price:
#     print(product["name"], product["price"])  # Print the name and price of each document in the 'products' collection where the price is greater than 1000

#-----------------------------------------------------

# e2:

# undelivered_orders = database.orders.find({"status": {"$ne": "delivered"}}, {"_id": 1, "status": 1}) # $ne means not equal to.

# # for order in undelivered_orders:
# #     print(order["_id"], order["status"])

# for order in undelivered_orders:
#     print(order) # The ouput is not as pretty here (in my opinion).

#-----------------------------------------------------

# e3:

# city_project = database.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}, {"_id": 0, "first_name": 1, "last_name": 1, "city": 1})

# for customer in city_project:
#     print(customer)

#-----------------------------------------------------

# e4:

# color_wq = database.products.find({"details.color": "white"}, {"_id": 0, "name": 1, "details": "white"})

# for product in color_wq:
#     print(product)

#-----------------------------------------------------

# e5:

# products_sport = database.products.find({"tags":"sport"}, {"_id": 0, "name": 1, "tags": 1}) # Here we are searching in arrays under the tags field.

# for product in products_sport:
#     print(product)

#-----------------------------------------------------

# e6:

# cheap_charlie = database.products.find({}, {"_id": 0, "name": 1, "price": 1}).sort("price", 1).limit(5)

# for cheapest in cheap_charlie:
#     print(cheapest)

# e7:

# orders_tw = database.orders.find({"items.product_id": 2}, {"_id": 1, "items.name.$": 1})

# for item in orders_tw:
#     # print(item)
#     print("Order Id:", item["_id"], " Item:", item["items"][0]["name"])

#-----------------------------------------------------

# e8:

# increase_price = database.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}}) # Run at your own risk. To reset the database to it's default state, perferably run seed_webshop.py .

# accessories = database.products.find({"category": "Accessories"}, {"_id": 1, "category": 1, "price": 1})

# for prod in accessories:
#     print(prod)

#-----------------------------------------------------

# e9:
# # Solution 1 (two steps):
# tag_new = database.products.update_one({"_id": 11}, {"$push": {"tags": "new"}}, upsert=True)

# field_new1 = database.products.update_one({"_id": 11}, {"$set": {"restock_date": datetime.now()}})

# # Solution 2 (one step):
# tag_field = database.products.update_one(
#     {"_id": 11},
#     {
#         "$addToSet": {"tags": "new"},
#         "$set": {"restock_date": datetime.now()}
#     }
# )

# result = database.products.find({"_id": 11})

# for prod in result:
#     print(prod)


#-----------------------------------------------------
# e10:

order_filter = {
    "status": "new",
    "order_date": {"$lt": datetime(2026, 3, 20)}
}

# The idea is to use the same filter. First for the retrieval, then the delete.

order_count = database.orders.count_documents(order_filter)

print("Orders found:", order_count)

delete_result = database.orders.delete_many(order_filter)

print("Orders deleted:", delete_result.deleted_count)