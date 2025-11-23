# operations.py
from inventory_data import inventory

def add_item_logic():
    """Handles the full logic for adding a new item."""
    print("\n--- Adding New Item ---")
    try:
        item_id = int(input("Enter new Item ID: "))
        
        if item_id in inventory:
            print(f"Error: Item ID {item_id} already exists.")
        else:
            name = input("Enter Item Name (e.g., Ruler): ")
            type_detail = input("Enter Type/Detail (e.g., '30cm', 'Red'): ")
            brand = input("Enter Brand Name: ")
            stock = int(input("Enter available stock: "))
            inventory[item_id] = {
                "Name": name, 
                "Type": type_detail, 
                "Brand": brand, 
                "Stock": stock
            }
            print(f" Item '{name}' (ID {item_id}) added successfully!")
    except ValueError:
        print(" Invalid input. Please ensure ID and Stock are numbers.")

def remove_item_logic():
    """Handles the full logic for removing an item."""
    print("\n--- Remove Item ---")
    try:
        item_id = int(input("Enter Item ID to remove: "))
        if inventory.pop(item_id, None):
            print(f"Item ID {item_id} successfully removed.")
        else:
            print(" Item ID not found.")

    except ValueError:
        print(" Invalid input. Please enter a numerical ID.")
