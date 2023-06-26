from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.12tpk99.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech
 
shane = {
    "student_id": "1007",
    "first_name": "Shane",
    "last_name": "Diyanni",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "12345",
                    "description": "Data/Database Security",
                    "instructor": "Professor Chelsie Thompson",
                    "grade": "A+"
                },
                {
                    "course_id": "12346",
                    "description": "Cooking",
                    "instructor": "Professor Dylan",
                    "grade": "A+"
                }
            ]
        }
    ]

}

lacey = {
    "student_id": "1008",
    "first_name": "Lacey",
    "last_name": "Deihl",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "12345",
                    "description": "Data/Databse Security",
                    "instructor": "Professor Chelsie Thompson",
                    "grade": "B+"
                },
                {
                    "course_id": "12346",
                    "description": "Cooking",
                    "instructor": "Professor Dylan",
                    "grade": "A-"
                }
            ]
        }
    ]
}

jake = {
    "student_id": "1009",
    "first_name": "Jake",
    "last_name": "Mathews",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "12345",
                    "description": "Data/Database Security",
                    "instructor": "Professor Chelsie Thompson",
                    "grade": "C"
                },
                {
                    "course_id": "12346",
                    "description": "Cooking",
                    "instructor": "Professor Dylan",
                    "grade": "B"
                }
            ]
        }
    ]
}

students = db.students

print("\n  -- INSERT STATEMENTS --")
shane_student_id = students.insert_one(shane).inserted_id
print("  Inserted student record Shane Diyanni into the students collection with document_id " + str(thorin_student_id))

lacey_student_id = students.insert_one(lacey).inserted_id
print("  Inserted student record Lacey Deihl into the students collection with document_id " + str(bilbo_student_id))

jake_student_id = students.insert_one(jake).inserted_id
print("  Inserted student record Jake Mathews into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")
