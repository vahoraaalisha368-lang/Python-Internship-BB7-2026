# 1. Two sets of email addresses
newsletter_subscribers = {
    "alice@example.com", 
    "bob@example.com", 
    "charlie@example.com", 
    "david@example.com"
}

purchased_customers = {
    "charlie@example.com", 
    "david@example.com", 
    "eve@example.com", 
    "frank@example.com"
}

# 2. Find subscribers who never made a purchase (Subscribers - Purchasers)
subscribers_no_purchase = newsletter_subscribers.difference(purchased_customers)

# 3. Find customers who made a purchase but never subscribed (Purchasers - Subscribers)
customers_no_subscription = purchased_customers.difference(newsletter_subscribers)

# Print the results
print("--- Newsletter & Purchase Analysis ---")
print(f"Subscribers who never made a purchase: {subscribers_no_purchase}")
print(f"Customers who made a purchase but never subscribed: {customers_no_subscription}")