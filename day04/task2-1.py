count = 0  

def my_function():
    global count
    count += 1
    print(f"Called {count} times")

my_function()
my_function()
my_function()
my_function()
print(f"Final count: {count}")