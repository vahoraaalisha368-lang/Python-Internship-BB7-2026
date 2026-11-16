students_data = [("Riya", 88), ("Aman", 95), ("Sara", 72)]

print("Original List of Students:")
print(students_data)

sorted_students = sorted(students_data, key=lambda x: x[1], reverse=True)

print("\nSorted List (Topper Appears First):")
print(sorted_students)