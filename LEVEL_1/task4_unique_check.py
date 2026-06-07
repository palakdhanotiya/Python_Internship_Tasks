#Task 4: Verify whether all numbers in the grid are unique

grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

numbers = []

for row in grid:
    for number in row:
        numbers.append(number)

if len(numbers) == len(set(numbers)):
    print("All numbers are unique")
else:
    print("Duplicate numbers found")

