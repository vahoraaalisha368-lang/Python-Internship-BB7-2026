def calculate_marks_stats(marks):
    """
    This function takes a list of marks and 
    returns a tuple of (lowest, highest, average).
    """
    if not marks:
        return 0, 0, 0
        
    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)
    
    return lowest, highest, average

# A sample list of student marks
student_marks = [78, 85, 92, 64, 90, 88]

# Calling the function and unpacking the result into three separate variables
lowest_mark, highest_mark, average_mark = calculate_marks_stats(student_marks)

# Printing the results
print(f"Lowest Mark: {lowest_mark}")
print(f"Highest Mark: {highest_mark}")
print(f"Average Mark: {average_mark}")