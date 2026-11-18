class OutOfRangeError(Exception):
    pass

while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        
        if num < 1 or num > 10:
            raise OutOfRangeError("Number must be between 1 and 10!")
        
        print(f"Valid number: {num}")
        break  

    except ValueError:
        print("Error: Please enter numbers only! Letters nahi chalenge.")
    except OutOfRangeError as e:
        print(f"Error: {e}")