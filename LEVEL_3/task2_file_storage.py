#Task 2: Save and retrieve records using file-based storage

file = open("records.txt", "a")

number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):

    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    record = name + "," + age + "," + marks + "\n"

    file.write(record)

file.close()

print("\nRecords saved successfully!")

print("\nSaved Records:\n")

file = open("records.txt", "r")

for line in file:
    print(line.strip())

file.close()