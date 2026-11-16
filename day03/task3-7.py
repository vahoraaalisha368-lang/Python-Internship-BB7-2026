inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

print("Initial Inventory:", inventory)

#Function to add new stock
def add_stock(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity
    print(f"Added {quantity} of '{product}'. Updated inventory: {inventory}")

def sell_product(product, quantity):
    if product not in inventory:
        print(f"Error: Product '{product}' does not exist in the inventory.")
    elif inventory[product] < quantity:
        print(f"Error: Not enough stock for '{product}'. Available quantity: {inventory[product]}")
    else:
        inventory[product] -= quantity
        print(f"Sold {quantity} of '{product}'. Remaining stock: {inventory[product]}")

# --- Example Usage ---
print("\n--- Adding New Stock ---")
add_stock("headphones", 20)

print("\n--- Selling an Item ---")
sell_product("mouse", 5)

print("\n--- Trying to Sell a Non-existent Product ---")
sell_product("monitor", 2)