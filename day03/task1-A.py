# 1. Take a list of at least 10 product prices
prices = [150, 450, 1200, 300, 850, 620, 950, 2400, 1100, 500]

# Calculate the average price
avg_price = sum(prices) / len(prices)

# Create a new list using a list comprehension for prices above the average price
above_avg_prices = [p for p in prices if p > avg_price]

# Print the results
print(f"All Prices: {prices}")
print(f"Average Price: {avg_price}")
print(f"Prices Above Average: {above_avg_prices}")