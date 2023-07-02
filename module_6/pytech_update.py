# Import
from pymongo import MongoClient

# MongoDB connect string
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

# loop output of collection
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update shane last name
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Diyanni 2"}})

# find new student document w/ id 1007
shane = students.find_one({"student_id": "1007"})

# output
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output updated document
print("  Student ID: " + shane["student_id"] + "\n  First Name: " + shane["first_name"] + "\n  Last Name: " + shane["last_name"] + "\n")

# exit
input("\n\n  End of program, press any key to continue...")
