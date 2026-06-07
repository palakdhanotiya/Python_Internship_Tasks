try:

    file = open("numbers.txt", "r")

    numbers = []

    for line in file:
        numbers.append(int(line.strip()))

    file.close()

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)

    print("Total   :", total)
    print("Average :", average)
    print("Maximum :", maximum)

except FileNotFoundError:
    print("File not found")