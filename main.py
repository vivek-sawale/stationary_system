# main.py
from operations import add_item_logic, remove_item_logic
from stock_management import update_stock_logic
from query_and_display import check_availability_logic, search_varieties_logic, list_all_items_logic

running = True
while running:
    print("\n--- 📖 Stationery Inventory Manager (Basic Mode) ---")
    print("1. Add New Item")
    print("2. Check Item Availability (By ID)")
    print("3. Search by Item Detail (Find Varieties)")
    print("4. List All Items")
    print("5. Update Stock (Increase/Decrease)")
    print("6. Remove Item")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        add_item_logic()
    elif choice == '2':
        check_availability_logic()
    elif choice == '3':
        search_varieties_logic()
    elif choice == '4':
        list_all_items_logic()
    elif choice == '5':
        update_stock_logic()
    elif choice == '6':
        remove_item_logic()
    elif choice == '7':
        print("Thank you! Inventory Manager Shutting Down.")
        running = False 
    else:
        print("Please enter a valid option between 1 and 7.")
        
print("-----------------------------------------")
