students = [
    {"name": "Riya", "marks": 88},
    {"name": "Aman", "marks": 95},
    {"name": "Kabir", "marks": 91},
    {"name": "Neha", "marks": 79}
]

# Assume the first student has the highest marks initially
highest_student = students[0]

for student in students:
    if student["marks"] > highest_student["marks"]:
        highest_student = student

print("Student with the highest marks:")
print(f"Name: {highest_student['name']}, Marks: {highest_student['marks']}")