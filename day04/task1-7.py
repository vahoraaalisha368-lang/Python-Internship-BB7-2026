import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start} seconds")
        return result
    return wrapper

@timer
def sum_1_to_n():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

print(sum_1_to_n())