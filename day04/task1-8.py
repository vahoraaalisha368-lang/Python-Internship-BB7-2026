def require_positive(func):
    def wrapper(*args, **kwargs):
        
        for num in args:
            if num <= 0:
                print("Error: All arguments must be positive numbers!")
                return None 
        
        return func(*args, **kwargs)
    return wrapper

@require_positive
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, -2))
print(divide(0, 5))   