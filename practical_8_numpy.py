#1
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print("size:",a.size)
print("data type:",a.dtype)
print("no. of dim:",a.ndim)
#2
a1=np.array([1,2,3,4,5])
a2=np.array([6,7,8,9,10])
print("Addition :",a1+a2)
print("Subtraction :",a2-a1)
print("mul:",a1*a2)
print("div:",a1/a2)
print("mod:",a1%a2)
#3
n=np.array([1,2,3,4,5,6,7,8,9,10])
print("max:",np.max(n))
print("min:",np.min(n))
print("sum:",np.sum(n))
print("avg:",np.mean(n))
#4
a = np.arange(1, 21)
even = a[a % 2 == 0]
odd = a[a % 2 != 0]
print("Original Array:", a)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
#5
a = np.arange(1, 13)
print("2 × 6 matrix :",a.reshape(2,6))
print("3 × 4 matrix :",a.reshape(3,4))
print("4 × 3 matrix :",a.reshape(4,3))
#6
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix addition
result = a + b

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Addition:")
print(result)
#7
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Matrix multiplication using np.dot()
result = np.dot(a, b)

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Multiplication:")
print(result)
#8
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("Transpose:",a.T)
#9
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Original Array:")
print(a)

# Display first row
print("First Row:", a[0])

# Display last column
print("Last Column:", a[:, -1])

# Display diagonal elements
print("Diagonal Elements:", np.diag(a))

# Display second and third rows
print("Second and Third Rows:")
print(a[1:3])
#10
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
print("Matrix:")
print(a)

# Sum of each row
row_sum = np.sum(a, axis=1)

# Sum of each column
column_sum = np.sum(a, axis=0)

print("Sum of each row:", row_sum)
print("Sum of each column:", column_sum)
#11
a=np.arange(1,21)
print(a)
print("First 5 elements :",a[:5])
print("Last 5 elements :",a[-5:])
print("Alternate elements:",a[::2])
print("Alternate elements:",a[1::2])
print("Elements in reverse order",a[::-1])
#12
a = np.array([10, 25, 60, 45, 75, 30, 90, 50, 65, 40])

print("Original Array:")
print(a)

# Replace elements greater than 50 with 0
a[a > 50] = 0

print("Array after replacement:")
print(a)
#13
# Create an unsorted array
a = np.array([45, 12, 78, 23, 56, 9, 34])

print("Original Array:")
print(a)

# Ascending order
ascending = np.sort(a)

# Descending order
descending = np.sort(a)[::-1]

print("Ascending Order:")
print(ascending)

print("Descending Order:")
print(descending)
#14
a = np.array([10, 20, 30, 20, 40, 10, 50, 30, 60, 40])

print("Original Array:")
print(a)

# Find unique elements
unique = np.unique(a)

print("Unique Elements:")
print(unique)
#15
# Create two NumPy arrays
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Array A:")
print(a)

print("Array B:")
print(b)

# Horizontal concatenation
horizontal = np.hstack((a, b))

# Vertical concatenation
vertical = np.vstack((a, b))

print("Horizontal Concatenation:")
print(horizontal)

print("Vertical Concatenation:")
print(vertical)
#16
marks = np.array([75, 82, 68, 90, 55, 73, 88, 95, 60, 79])
print("Marks:", marks)
# Calculate statistics
highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)
median = np.median(marks)
standard_deviation = np.std(marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Median:", median)
print("Standard Deviation:", standard_deviation)
#17
marks = np.array([65, 78, 55, 89, 92, 45, 70, 84, 76, 60,
                  95, 68, 73, 88, 50, 81, 67, 90, 72, 58])

# Calculate class average
average = np.mean(marks)

# Students scoring above average
above_average = marks[marks > average]

print("Marks of 20 Students:")
print(marks)

print("Class Average:", average)

print("Students who scored above average:")
print(above_average)
#18
import numpy as np

# Create 3D array containing numbers from 1 to 24
a = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(a)

print("Number of Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
#19
import numpy as np

# Create 3D array of shape (2, 3, 4)
a = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(a)

# Access elements
print("First Element:", a[0, 0, 0])
print("Last Element:", a[1, 2, 3])
print("Element at [0,1,2]:", a[0, 1, 2])
print("Element at [1,2,3]:", a[1, 2, 3])
#20
import numpy as np

# Create a (2, 3, 4) array
a = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(a)

# Sum of all elements
print("Sum of all elements:", np.sum(a))

# Sum of each layer
print("Sum of each layer:", np.sum(a, axis=(1, 2)))

# Sum along rows
print("Sum along rows:")
print(np.sum(a, axis=2))

# Sum along columns
print("Sum along columns:")
print(np.sum(a, axis=1))
#21
import numpy as np

# Create random 3D array
a = np.random.randint(1, 101, (2, 3, 4))

print("Original Array:")
print(a)

# Replace values greater than 50 with 0
a[a > 50] = 0

print("Array after replacement:")
print(a)
#22
import numpy as np

# Create random 3D array
a = np.random.randint(1, 101, (3, 4, 5))

print("3D Array:")
print(a)

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
#23
import numpy as np

# Create 3D array from 1 to 24
a = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array:")
print(a)

# Flatten the array
b = a.flatten()

print("Flattened Array:")
print(b)
#24
import numpy as np

# Create 3D array from 1 to 27
a = np.arange(1, 28).reshape(3, 3, 3)

# Flatten the array
b = a.flatten()

print("3D Array:")
print(a)

print("Flattened Array:")
print(b)

print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))
#25
import numpy as np

# Create random 3D array
a = np.random.randint(1, 101, (3, 4, 5))

# Flatten the array
b = a.flatten()

# Calculate average
average = np.mean(b)

print("Original 3D Array:")
print(a)

print("Flattened Array:")
print(b)

# Elements greater than 50
print("Elements greater than 50:")
print(b[b > 50])

# Even numbers
print("Even numbers:")
print(b[b % 2 == 0])

# Elements less than average
print("Average:", average)
print("Elements less than average:")
print(b[b < average])





























































