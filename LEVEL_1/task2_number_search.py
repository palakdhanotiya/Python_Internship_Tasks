#Task 2: Check whether a given number exists in the predefined grid

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

number = int(input("Enter a number to search: "))

#7found = False

for row in grid:
    if number in row:
        found = True
        break

if found:
   grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

number = int(input("Enter a number to search: "))

found = False

for row in grid:
    if number in row:
        found = True
        break

if found:
    print("Number found in grid")
else:
    print("Number not found in grid")
