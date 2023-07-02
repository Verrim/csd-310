# Import
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

# loop collection output results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# test input to delete
test_doc = {
    "student_id": "1010",
    "first_name": "Patricia",
    "last_name": "James"
}

# insert test to delete
test_doc_id = students.insert_one(test_doc).inserted_id

# output of test insert
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# find student w/ id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# output
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# remove student 1010 from collection
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find students in collection
new_student_list = students.find({})

# output
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop collection output results
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit
input("\n\n  End of program, press any key to continue...")
