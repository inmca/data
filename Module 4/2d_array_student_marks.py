import numpy as np

# Dataset: [RollNo, Marks1, Marks2, Marks3]
data = np.array([
    [1, 85, 78, 92],
    [2, 76, 88, 85],
    [3, 90, 92, 94],
    [4, 70, 75, 80],
    [5, 88, 85, 91]
])

# Extract marks only (ignore RollNo column)
marks = data[:, 1:]  # all rows, columns from index 1 onwards

# Calculate total marks for each student
total_marks = np.sum(marks, axis=1)

# Calculate average marks for each student
average_marks = np.mean(marks, axis=1)

# Combine results with RollNo for display
results = np.column_stack((data[:, 0], total_marks, average_marks))

# Display the results
print("RollNo  Total Marks  Average Marks")
for row in results:
    print(f"{int(row[0]):<7} {int(row[1]):<11} {row[2]:.2f}")

