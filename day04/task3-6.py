def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as e:
        print(f"Error: Missing key {e} in order!")
    else:
        print(f"Order: {item} costs Rs.{price}")
    finally:
        print("Processing complete")

process_order({"item": "Cake", "price": 250})
print("---")
process_order({"item": "Cake"})