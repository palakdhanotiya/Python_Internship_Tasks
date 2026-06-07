#Task 2: Generate student reports from stored marks and names

students = []

number = int(input("Enter number of students: "))

for i in range(number):

    print("\nStudent", i + 1)

    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    else:
        grade = "D"

    student = {
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)

print("\n===== STUDENT REPORT =====")

for student in students:
    print("---------------------")
    print("Name :", student["name"])
    print("Marks:", student["marks"])
    print("Grade:", student["grade"])