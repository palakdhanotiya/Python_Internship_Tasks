#Task 4: Create a log file system with date and time entries

from datetime import datetime

message = input("Enter log message: ")

current_time = datetime.now()

log_entry = str(current_time) + " - " + message + "\n"

file = open("log.txt", "a")

file.write(log_entry)

file.close()

print("Log saved successfully!")