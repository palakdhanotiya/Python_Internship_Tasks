#Task 3: Build a daily task list manager with file saving

task_file = "tasks.txt"

number = int(input("How many tasks do you want to add? "))

file = open(task_file, "a")

for i in range(number):

    task = input(f"Enter Task {i+1}: ")

    file.write(task + "\n")

file.close()

print("\n===== TASK LIST =====")

file = open(task_file, "r")

count = 1

for line in file:
    print(f"{count}. {line.strip()}")
    count += 1

file.close()



