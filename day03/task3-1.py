products = {
    "pen": 20,
    "notebook": 150,
    "bag": 1200,
    "bottle": 90,
    "shoes": 2500
}

expensive_products = {name: price for name, price in products.items() if price > 100}

#Print the results
print("All Products:", products)
print("Products priced above 100:", expensive_products)