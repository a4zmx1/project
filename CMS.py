# Cafe Management System

menu = {}
order = {}

while True:
    print("\n----- CAFE MANAGEMENT SYSTEM ----------")
    print("1. Add Menu Item")
    print("2. Update Menu Item")
    print("3. Delete Menu Item")
    print("4. Show Menu")
    print("5. Take Order")
    print("6. Generate Bill")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Menu Item
    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        if name in menu:
            print("Item already exists.")
        else:
            menu[name] = price
            print("Item added successfully.")

    # Update Menu Item
    elif choice == "2":
        name = input("Enter item name to update: ")
        if name in menu:
            price = float(input("Enter new price: "))
            menu[name] = price
            print("Item updated.")
        else:
            print("Item not found.")

    # Delete Menu Item
    elif choice == "3":
        name = input("Enter item name to delete: ")
        if name in menu:
            del menu[name]
            print("Item deleted.")
        else:
            print("Item not found.")

    # Show Menu
    elif choice == "4":
        if len(menu) == 0:
            print("Menu is empty.")
        else:
            print(menu)

    # Take Order
    elif choice == "5":
        item = input("Enter item name: ")
        if item in menu:
            qty = int(input("Enter quantity: "))
            order[item] = qty
            print("Item added to order.")
        else:
            print("Item not available in menu.")

    # Generate Bill
    elif choice == "6":
        total = 0
        print("BILL")
        for item, qty in order.items():
            price = menu[item]
            cost = price * qty
            total += cost
            print(item, "x", qty, "=", cost)

        print("Total Bill:", total)

    # Exit
    elif choice == "7":
        print("Thank you for visiting the cafe!")
        break

    else:
        print("Invalid choice.")