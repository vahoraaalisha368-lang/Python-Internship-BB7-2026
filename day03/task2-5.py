# 1. A list of website visitor IDs with repeated values
visitor_ids = [101, 102, 103, 101, 104, 102, 105, 103, 106, 101]

# 2. Convert the list to a set to remove duplicate values and get unique visitors
unique_visitors = set(visitor_ids)

# 3. Count the total number of unique visitors using len()
unique_count = len(unique_visitors)

# Print the results
print("--- Website Visitor Analysis ---")
print(f"Unique Visitors: {unique_visitors}")
print(f"Total count of unique visitors: {unique_count}")