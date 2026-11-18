from functools import reduce

numbers = [10, 45, 3, 99, 23]
largest = reduce(lambda a, b: a if a > b else b, numbers)
print(largest) 