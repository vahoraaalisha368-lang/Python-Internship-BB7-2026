def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  
print(counter1())  
print(counter1())  

print(counter2())  

print(f"Counter1: {counter1()}") 
print(f"Counter2: {counter2()}")  