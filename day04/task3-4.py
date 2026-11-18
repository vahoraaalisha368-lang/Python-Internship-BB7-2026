def read_file_safely(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

print(read_file_safely("data.txt")) 
print(read_file_safely("task3-4.py"))      