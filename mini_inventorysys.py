# CLI Mini Inventory System

inventory = []

def show_menu():
    print("\n--- Mini Inventory System ---")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Item")
    print("6. Exit")

def add_item():
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    inventory.append({"name": name, "quantity": qty, "price": price})
    print(f"{name} added successfully!")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        print("No | Item Name | Quantity | Price | Total Value")
        for idx, item in enumerate(inventory, start=1):
            total_value = item['quantity'] * item['price']
            print(f"{idx}. {item['name']} | {item['quantity']} | {item['price']} | {total_value}")

def update_item():
    view_inventory()
    try:
        num = int(input("Enter item number to update: "))
        item = inventory[num-1]
        print(f"Updating {item['name']}")
        item['quantity'] = int(input("Enter new quantity: "))
        item['price'] = float(input("Enter new price: "))
        print("Item updated successfully!")
    except:
        print("Invalid input.")

def delete_item():
    view_inventory()
    try:
        num = int(input("Enter item number to delete: "))
        removed = inventory.pop(num-1)
        print(f"{removed['name']} removed from inventory.")
    except:
        print("Invalid input.")

def search_item():
    keyword = input("Enter item name to search: ").lower()
    results = [i for i in inventory if keyword in i['name'].lower()]
    if results:
        print("Search Results:")
        for item in results:
            total_value = item['quantity'] * item['price']
            print(f"{item['name']} | {item['quantity']} | {item['price']} | {total_value}")
    else:
        print("No matching items found.")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        add_item()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        search_item()
    elif choice == "6":
        print("Exiting Inventory System. Goodbye! 🛒")
        break
    else:
        print("Invalid choice. Try again.")