
# initilize the Phonebook
phonebook = {}

print("Welcome to Python Phonebook.")

#Interface loop
while True:
    print("Menu:")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. List All Contact")
    print("4. Exit")

    choice = input("Choose an option (1-4):")

    # Add Contact 
    if choice == '1':
        name = input("Enter contact name:")

        if name in phonebook:
            print(f"Error:'{name}' already exists.")

        else:
            number = input("Enter phone number:")
            phonebook[name] = number
            print(f"Contact '{name}' added successfully!")
# Search Contact

    if choice == '2':
        name = input("Enter name to Search:")
        if name in phonebook:
            print(f"Found: {name} - {phonebook[name]}")
        else:
            print("Contact not found.")

# Delete Contact

if choice == '3':
    name = input("Enter name to delete:")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name} deleted.")
    else:
        print("Contact not found.")

# List all Contact
elif choice == '4':
    if len(phonebook) == 0:
        print("No contact found")
    else:
        for name,phone_number in phonebook.items():
            print(f"Name:{name}. phone number:{phone_number}")
        

        for name , number in phonebook:
            print(name, ":", phonebook[name])

# Exit
elif choice == "5":
  print("Goodbye!")




else:
 print("Invalid choice")





    


