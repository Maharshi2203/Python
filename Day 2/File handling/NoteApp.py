while True:
    print("\n=====Note App=====")
    print("1.Add Note")
    print("2.View Note")
    print("3.Exit Note")

    choice = input("Enter your choice: ")

    if choice == "1":
        note=input("Enter the note: ")

        with open("note.txt","a") as file:
            file.write(note+"\n")

            print("note saved successfully")
        
    elif choice == "2":
        try:
            with open("note.txt", "r") as file:
                content = file.read()

                if content:
                    print("\n--- Your Notes ---")
                    print(content)
                else:
                    print("No notes found.")
        except FileNotFoundError:
            print("No notes file found.")

    elif choice == "3":
        print("Exiting Notes App...")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")