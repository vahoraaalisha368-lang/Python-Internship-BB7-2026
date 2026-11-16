numbers = [12, 45, 67, 23, 89, 90, 34, 89]

print("Original List:", numbers)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == float('-inf'):
    print("List me koi second largest number nahi mila.")
else:
    print("The Second Largest Number is:", second_largest)