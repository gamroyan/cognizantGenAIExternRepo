# Project: Implement Your own Data Structures

def inventory():
    # key: item name, value: tuple containing the quantity and price
    inventory = {}
    inventory["mango"] = (15, 3.0)
    inventory["apple"] = (10, 2.5)
    inventory["banana"] = (20, 1.7)
    del inventory["apple"]
    total_value = 0

    # tuples are immuatable so I'm creating a new tuple to update the price
    inventory["mango"] = (15, 2.8)

    # iterating over the key, value pairs
    for key, (quantity, price) in inventory.items():
        total_value += (quantity * price) # should be $76
        print("Item: " + str(key) + ", Quantity: " + str(quantity) + ", Price: $" + str(price))
        
    print("Total value of inventory; $" + str(total_value))
    return

inventory()