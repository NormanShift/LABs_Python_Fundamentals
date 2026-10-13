from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)  # Connect to the MongoDB server
print(client.list_database_names())  # List all databases on the server