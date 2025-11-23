# query_and_display.py
from inventory_data import inventory

def check_availability_logic():
    """Handles the full logic for checking item availability by ID."""
    print("\n--- Check Availability ---")
    try:
        item_id = int(input("Enter Item ID to check: "))
        if item_id in inventory:
            item = inventory[item_id]
            print(f"\n✨ Item Found: {item['Name']}")
            print(f"  Brand: {item['Brand']} | Stock: {item['Stock']}")
        else:
            print("Item not found.")
    except ValueError:
        print(" Invalid input. Please enter a numerical ID.")

def search_varieties_logic():
    """Handles the full logic for searching by name and detail."""
    print("\n--- Search Varieties ---")
    search_name = input("Enter the main Item Name (e.g., Notebook): ")
    search_detail = input("Enter the specific detail (e.g., 200Page, Gel-Blue): ")
    found_count = 0
    print(f"\n🔎 Results for '{search_name}' with detail '{search_detail}':")
    for item_id, item_data in inventory.items():
        if item_data.get("Name", "").lower() == search_name.lower():
            if search_detail.lower() in item_data.get("Type", "").lower():
                print(f"  - ID: **{item_id}** | Brand: **{item_data['Brand']}** | Stock: **{item_data['Stock']}**")
                found_count += 1
    if found_count == 0:
        print(f" No matching items found.")

def list_all_items_logic():
    """Handles the full logic for listing all inventory items."""
    print("\n--- All Stationery Inventory Items ---")
    if not inventory:
        print("The inventory is currently empty.")
    else:
        for item_id, item_data in inventory.items():
            print(f"--- ID: {item_id} ({item_data['Name']}) ---")
            print(f"  Type/Detail: {item_data['Type']}")
            print(f"  Brand: {item_data['Brand']}")
            print(f"  Stock: {item_data['Stock']}")
        print("-----------------------------------------")
