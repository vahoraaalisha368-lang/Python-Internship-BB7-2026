words = ["apple", "ant", "banana", "bat", "cat", "carrot"]

grouped_words = {}

for word in words:
    first_letter = word[0]
    grouped_words.setdefault(first_letter, []).append(word)

# Print the result
print("Grouped words by their first letter:")
print(grouped_words)