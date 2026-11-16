# 1. List of visited locations represented as (latitude, longitude) tuples
visited_locations = [
    (12.9, 77.5), 
    (19.0, 72.8), 
    (28.6, 77.2), 
    (13.0, 80.2)
]

print("--- Visited Locations Report ---")

# 2. Loop through the list and unpack each tuple into 'lat' and 'lon' variables
for lat, lon in visited_locations:
    print(f"Latitude: {lat}, Longitude: {lon}")