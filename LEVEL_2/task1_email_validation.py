#Task 1: Validate an email address using basic rules

email = input("Enter an email address: ")

if "@" in email and "." in email and " " not in email :
    print(email, "is a valid email address.")
else:
    print(email,"is not a valid email address.")