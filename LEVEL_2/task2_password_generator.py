#Task 2: Generate a random password with letters and numbers

import random
import string

characters = string.ascii_letters + string.digits

length = int(input("Enter the length of password: "))

password = " "

for i in range(length):
    password += random.choice(characters)

print("Generated password:", password)