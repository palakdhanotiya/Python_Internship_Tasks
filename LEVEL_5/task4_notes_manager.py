while True:

    print("\n===== PERSONAL NOTES MANAGER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        note = input("Enter your note: ")

        file = open("notes.txt", "a")

        file.write(note + "\n")

        file.close()

        print("Note Saved Successfully!")

    elif choice == "2":

        try:

            file = open("notes.txt", "r")

            print("\n===== SAVED NOTES =====")

            for line in file:
                print("-", line.strip())

            file.close()

        except FileNotFoundError:

            print("No notes found.")

    elif choice == "3":

        print("Exiting Program...")
        break

    else:

        print("Invalid Choice!")