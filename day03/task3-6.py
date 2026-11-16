employees = {
    "Aman": 45000,
    "Priya": 75000,
    "Rahul": 60000,
    "Sneha": 90000,
    "Vikram": 30000,
    "Karan": 82000
}

top_3_employees = sorted(employees.items(), key=lambda item: item[1], reverse=True)[:3]

print("Top 3 Highest Paid Employees:")
for name, salary in top_3_employees:
    print(f"Name: {name}, Salary: {salary}")
    