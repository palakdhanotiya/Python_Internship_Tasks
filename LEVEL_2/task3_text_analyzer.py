#Task 3: Analyze text to count total characters and words

text = input("Enter a text:")

character = len(text)
word = len(text.split())

print("Total Characters :", character)
print("Total Words :", word)    