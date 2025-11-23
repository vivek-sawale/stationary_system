Features
The application provides essential inventory management tools:

Add/Remove Items: Create new items or delete existing ones by ID.

Stock Control: Increase or decrease stock quantity (Option 5).

Query & Search: Check availability by ID (Option 2) or search for product varieties by name and detail (Option 3).

List All: View the complete inventory list (Option 4).

🚀 Getting Started
Prerequisites
Python 3.x

Execution
Clone the repository and navigate to the project directory.

Ensure all five Python files (main.py, inventory_data.py, operations.py, stock_management.py, query_and_display.py) are present.

Run the main file from your terminal:

Bash

python main.py
📂 Project Structure
The code is organized into modules to separate concerns:

File Name	Responsibility
main.py	Runs the main menu and directs program flow.
inventory_data.py	Holds the core inventory data dictionary.
operations.py	Handles Add and Remove item logic.
stock_management.py	Handles Stock Update (Increase/Decrease) logic.
query_and_display.py	Handles Check Availability, Search, and List logic.

📝 Example Usage
Run the program and choose an option:

--- 📖 Stationery Inventory Manager (Basic Mode) ---
...
5. Update Stock (Increase/Decrease)
...
Enter your choice (1-7): 5

Enter Item ID to update stock: 101
Current Stock for Pen: 50
Increase (I) or Decrease (D) stock? (I/D): I
Enter quantity: 10
Stock Increased. New Stock: **60**
