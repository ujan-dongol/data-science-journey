

student1 = {
    "First Name" : "Texas",
    "Middle Name" : "Aus",
    "Last Name" : "Acdc",
     "course": "BSc IT",
    "age": 21
}



student2 = {
    "First Name" : "Americano",
    "Middle Name" : "Aucerr",
    "Last Name" : "Amongus",
     "course": "BBA",
    "age": 22
}


student3 = {
    "First Name" : "Tullu",
    "Middle Name" : "Ramma",
    "Last Name" : "Bask",
    "course": "MBBS",
    "age": 45
}

manage =[student1, student2, student3]

for student in manage:
    print(student)
# upto here all 3 students detail will print   
courses = set()

for student in manage:
    courses.add(student["course"])

print("\nUnique Courses:")
print(courses)