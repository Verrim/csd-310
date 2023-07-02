#This program was written by me, however, I have coppied the format:

# Import Statement
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.12tpk99.mongodb.net/?retryWrites=true&w=majority"

# connect MongoDB cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech

# displays
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# exit
input("\n\n  End of program, press any key to exit... ")



