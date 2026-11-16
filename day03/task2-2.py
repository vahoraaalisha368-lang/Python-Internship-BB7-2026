#  Create a tuple representing a product record (name, price, quantity)
product = ("Laptop", 45000, 5)
print(f"Original Product Record: {product}")

updated_product = (product[0], 42000, product[2])

print(f"Updated Product Record: {updated_product}")