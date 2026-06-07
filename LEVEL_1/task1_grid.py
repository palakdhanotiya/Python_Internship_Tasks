#Task 1: Display a simple 3×3 number grid using Python


grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for number in row:
        print(number, end=" ")
    print()