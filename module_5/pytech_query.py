# import
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.12tpk99.mongodb.net/?retryWrites=true&w=majority"

# connect MongoDB cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get student collection
students = db.students

# find students in collection
student_list = students.find({})

# output of find
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop collection output
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find shane document
shane = students.find_one({"student_id": "1007"})

# output of find
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + shane["student_id"] + "\n  First Name: " + shane["first_name"] + "\n  Last Name: " + shane["last_name"] + "\n")

# end
input("\n\n  End of program, press any key to continue...")
