#Task 3: Calculate and display the sum of each row in the grid

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in grid :
    row_sum = sum(row)
    print("Sum of row",row, "is:", row_sum)
    row_sum += row_sum
    