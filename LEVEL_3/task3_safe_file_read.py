#Task 3: Read and display file content line by line safely

try:

    file = open("records.txt", "r")

    print("File Content:\n")

    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("File not found")