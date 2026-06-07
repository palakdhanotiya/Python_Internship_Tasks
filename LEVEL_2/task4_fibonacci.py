#Task 4: Generate the Fibonacci sequence up to a given number of terms

terms = int(input("Enter a number of terms:"))

first = 0
second = 1

print("Fibonacci sequence:")

for i in range(terms):
    print(first , end = " ")
    next = first + second
    first = second
    second = next


