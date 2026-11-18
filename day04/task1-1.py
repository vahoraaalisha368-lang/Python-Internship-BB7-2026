def build_invoice(customer_name, *item_prices, **extra_details):
    print(f"Customer: {customer_name}")
    print(f"Total: {sum(item_prices)}")
    for key, value in extra_details.items():
        print(f"{key}: {value}")

# Example
build_invoice("Alisha", 200, 350, 150, discount=50, tax=18)
build_invoice("Aaysa", 500, tax=10)