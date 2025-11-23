# stock_management.py
from inventory_data import inventory

def update_stock_logic():
    """Handles the full logic for updating an item's stock."""
    print("\n--- Update Stock ---")
    try:
        item_id = int(input("Enter Item ID to update stock: "))
        if item_id not in inventory:
                print(" Item ID not found.")
        else:
                item = inventory[item_id]
                print(f"Current Stock for {item['Name']}: {item['Stock']}")
                update_choice = input("Increase (I) or Decrease (D) stock? (I/D): ").upper()
                qty = int(input("Enter quantity: "))
                if update_choice == 'I':
                    item["Stock"] += qty
                    print(f"Stock Increased. New Stock: **{item['Stock']}**")
                elif update_choice == 'D':
                    if item["Stock"] >= qty:
                        item["Stock"] -= qty
                        print(f" Stock Decreased. New Stock: **{item['Stock']}**")
                    else:
                        print(f" Error: Insufficient stock. Current stock is only {item['Stock']}.")
                else:
                    print("Invalid choice.")
    except ValueError:
        print(" Invalid input. Please enter numbers for ID and Quantity.")
