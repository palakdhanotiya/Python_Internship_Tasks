import csv

file = open("students.csv", "r")

reader = csv.reader(file)

print("\n===== STUDENT DATA =====\n")

for row in reader:
    print(" | ".join(row))

file.close()