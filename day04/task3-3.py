class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be between 0 and 120.")
    return f"User registered with age {age}"

try:
    print(register_user(25))   
    print(register_user(150))  
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    print(register_user(-5))
except InvalidAgeError as e:
    print(f"Error: {e}")