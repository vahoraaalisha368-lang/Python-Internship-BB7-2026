import random

numbers = [random.randint(1, 100) for _ in range(15)]
print("Original List:", numbers)

unique_numbers = []
for num in numbers:
  if num not in unique_numbers:
    unique_numbers.append(num)

print("Result (Without Duplicates):", unique_numbers)