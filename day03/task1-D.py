matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print("\nTransposed Matrix (Rows become Columns):")
for row in transpose_matrix:
    print(row)