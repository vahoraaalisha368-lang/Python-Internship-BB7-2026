employee_names = ["Aman", "Riya", "Sahil", "Priya"]
salaries = [45000, 60000, 52000, 75000]

print("Employee Details (Using zip):")

for name, salary in zip(employee_names, salaries):
    print(f"Employee Name: {name}, Salary: {salary}")