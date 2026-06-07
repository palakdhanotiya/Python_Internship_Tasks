#Task 1: Create a simple record management system using lists or dictionaries

records = []

number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):

    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    records.append(student)

print("\nStudent Records:")

for student in records:
    print("-------------------")
    print("Name :", student["name"])
    print("Age  :", student["age"])
    print("Marks:", student["marks"])

