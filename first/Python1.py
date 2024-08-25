print("Python-Editted")
# Sample inventory: a dictionary where the key is the item ID and the value is a list containing name, price, and quantity
inventory = {
    101: ["Apple", 0.5, 100],
    102: ["Banana", 0.2, 150],
    103: ["Orange", 0.8, 80],
    104: ["Mango", 1.5, 50],
    105: ["Grapes", 2.0, 200],
}

def display_inventory():
    """Displays the current inventory."""
    print("\nCurrent Inventory:")
    print(f"{'ID':<5} {'Name':<10} {'Price':<10} {'Quantity':<10}")
    print("-" * 35)
    for item_id, details in inventory.items():
        print(f"{item_id:<5} {details[0]:<10} ${details[1]:<9.2f} {details[2]:<10}")

def add_item(item_id, name, price, quantity):
    """Adds a new item to the inventory."""
    if item_id in inventory:
        print("Item ID already exists. Use a different ID.")
    else:
        inventory[item_id] = [name, price, quantity]
        print(f"Added item: {name} (ID: {item_id})")

def update_item(item_id, name=None, price=None, quantity=None):
    """Updates the details of an existing item."""
    if item_id in inventory:
        if name:
            inventory[item_id][0] = name
        if price:
            inventory[item_id][1] = price
        if quantity:
            inventory[item_id][2] = quantity
        print(f"Updated item with ID: {item_id}")
    else:
        print("Item ID not found in inventory.")

def delete_item(item_id):
    """Deletes an item from the inventory."""
    if item_id in inventory:
        deleted_item = inventory.pop(item_id)
        print(f"Deleted item: {deleted_item[0]} (ID: {item_id})")
    else:
        print("Item ID not found in inventory.")

def search_item(name):
    """Searches for items by name."""
    print(f"\nSearching for items containing '{name}':")
    found = False
    for item_id, details in inventory.items():
        if name.lower() in details[0].lower():
            print(f"Found: ID: {item_id}, Name: {details[0]}, Price: ${details[1]:.2f}, Quantity: {details[2]}")
            found = True
    if not found:
        print("No items found with that name.")

def calculate_total_value():
    """Calculates the total value of the inventory."""
    total_value = sum(details[1] * details[2] for details in inventory.values())
    print(f"\nTotal inventory value: ${total_value:.2f}")

# Example usage:
display_inventory()

add_item(106, "Pineapple", 3.0, 25)
update_item(103, quantity=90)
delete_item(102)

search_item("Apple")
search_item("berry")

calculate_total_value()
display_inventory()

