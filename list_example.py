# ============================================================
# 1. Create a list of five fruits and display the list
# ============================================================

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
print("1. Fruits:", fruits)


# ============================================================
# 2. Display first, last and third element
# ============================================================

numbers = [10, 20, 30, 40, 50]
print("\n2. First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# ============================================================
# 3. Replace third color
# ============================================================

colors = ["Red", "Blue", "Green", "Yellow", "White"]
colors[2] = "Pink"
print("\n3. Updated colors:", colors)


# ============================================================
# 4. Add element at end, beginning and specified position
# ============================================================

numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(0, 5)
numbers.insert(2, 15)
print("\n4. Updated list:", numbers)


# ============================================================
# 5. Remove first, last and specific student
# ============================================================

students = ["Amit", "Rahul", "Sneha", "Priya", "Rohit"]

students.pop(0)
students.pop()
students.remove("Sneha")

print("\n5. Remaining students:", students)


# ============================================================
# 6. Find largest and smallest without max() and min()
# ============================================================

numbers = [45, 12, 78, 23, 9, 56]

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("\n6. Largest:", largest)
print("Smallest:", smallest)


# ============================================================
# 7. Accept 10 numbers and calculate sum and average
# ============================================================

numbers = []

for i in range(10):
    n = int(input("\n7. Enter number: "))
    numbers.append(n)

total = 0

for n in numbers:
    total += n

average = total / 10

print("Sum:", total)
print("Average:", average)


# ============================================================
# 8. Store 15 integers and count even and odd
# ============================================================

numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 11, 22, 33, 44, 55, 66]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("\n8. Even numbers:", even)
print("Odd numbers:", odd)


# ============================================================
# 9. Search city in list
# ============================================================

cities = ["Pune", "Mumbai", "Delhi", "Nashik", "Nagpur"]

city = input("\n9. Enter city name: ")

if city in cities:
    print("City exists in the list")
else:
    print("City does not exist in the list")


# ============================================================
# 10. Reverse list without reverse()
# ============================================================

numbers = [10, 20, 30, 40, 50]
reverse = []

for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])

print("\n10. Original list:", numbers)
print("Reversed list:", reverse)


# ============================================================
# 11. List slicing
# ============================================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("\n11. First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])


# ============================================================
# 12. Elements at even index positions
# ============================================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("\n12. Elements at even indexes:")

for i in range(0, len(numbers), 2):
    print(numbers[i])


# ============================================================
# 13. Accept 10 numbers and sort ascending and descending
# ============================================================

numbers = []

for i in range(10):
    n = int(input("\n13. Enter number: "))
    numbers.append(n)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)


# ============================================================
# 14. Display only unique elements
# ============================================================

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("\n14. Unique elements:", unique)


# ============================================================
# 15. Find second largest element
# ============================================================

numbers = [10, 50, 30, 80, 60, 80]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

unique.sort()

second_largest = unique[-2]

print("\n15. Second largest element:", second_largest)


# ============================================================
# 16. Nested list storing student details
# ============================================================

students = [
    ["Amit", 101, 85],
    ["Sneha", 102, 90],
    ["Rahul", 103, 78],
    ["Priya", 104, 88]
]

print("\n16. Student Details:")

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()


# ============================================================
# 17. Addition of two 3 x 3 matrices
# ============================================================

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("\n17. Matrix Addition:")

for row in result:
    print(row)


# ============================================================
# 18. Shopping cart
# ============================================================

cart = []

while True:
    print("\n18. Shopping Cart")
    print("1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display cart")
    print("5. Count total items")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        cart.append(item)
        print("Item added")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print("Item found")
        else:
            print("Item not found")

    elif choice == 4:
        print("Cart:", cart)

    elif choice == 5:
        print("Total items:", len(cart))

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# ============================================================
# 19. Student attendance
# ============================================================

students = ["Amit", "Sneha", "Rahul", "Priya"]

print("\n19. Total students:", len(students))

name = input("Search student: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

name = input("Enter new student: ")
students.append(name)

name = input("Enter absent student to remove: ")

if name in students:
    students.remove(name)

print("Updated student list:", students)


# ============================================================
# 20. Book management
# ============================================================

books = ["Python", "Java", "C++", "HTML"]

while True:
    print("\n20. Book Management")
    print("1. Add book")
    print("2. Search book")
    print("3. Remove book")
    print("4. Display books")
    print("5. Count books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added")

    elif choice == 2:
        book = input("Enter book name: ")
        if book in books:
            print("Book found")
        else:
            print("Book not found")

    elif choice == 3:
        book = input("Enter book to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed")
        else:
            print("Book not found")

    elif choice == 4:
        print("Books:", books)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# ============================================================
# 21. Merge two lists
# ============================================================

list1 = [10, 20, 30]
list2 = [40, 50, 60]

merged = list1 + list2

print("\n21. Merged list:", merged)


# ============================================================
# 22. Common elements between two lists
# ============================================================

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for n in list1:
    if n in list2 and n not in common:
        common.append(n)

print("\n22. Common elements:", common)


# ============================================================
# 23. Frequency of each element
# ============================================================

numbers = [10, 20, 10, 30, 20, 10, 40, 30]

frequency = []

for n in numbers:
    if n not in frequency:
        count = 0

        for x in numbers:
            if x == n:
                count += 1

        frequency.append(n)
        print("\n23.", n, ":", count)


# ============================================================
# 24. Rotate list left and right by one position
# ============================================================

numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("\n24. Original:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)


# ============================================================
# 25. Remove duplicates preserving original order
# ============================================================

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("\n25. List after removing duplicates:", unique)


# ============================================================
# 26. Marks of 20 students
# ============================================================

marks = [
    75, 82, 65, 90, 55,
    88, 72, 95, 60, 78,
    85, 67, 92, 58, 80,
    70, 96, 62, 76, 89
]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total += mark

average = total / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("\n26. Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above)
print("Students below average:", below)


# ============================================================
# 27. Employee salaries
# ============================================================

salaries = [25000, 35000, 55000, 60000, 45000, 75000, 28000, 52000]

highest = salaries[0]
lowest = salaries[0]
total = 0

for salary in salaries:
    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

    total += salary

average = total / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("\n27. Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above Rs.50000:", above_50000)
print("Employees earning below Rs.30000:", below_30000)


# ============================================================
# 28. Batsman scores in 10 matches
# ============================================================

scores = [45, 67, 102, 55, 120, 34, 89, 150, 76, 42]

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for score in scores:

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    total += score

    if score >= 100:
        centuries += 1

    elif score >= 50:
        half_centuries += 1

average = total / len(scores)

print("\n28. Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)


# ============================================================
# 29. Temperature of 30 days
# ============================================================

temperatures = [
    25, 28, 30, 27, 32,
    29, 31, 26, 24, 33,
    35, 30, 29, 28, 34,
    36, 31, 27, 25, 32,
    30, 29, 35, 33, 28,
    26, 37, 34, 30, 29
]

hottest = temperatures[0]
coldest = temperatures[0]
total = 0

for temperature in temperatures:

    if temperature > hottest:
        hottest = temperature

    if temperature < coldest:
        coldest = temperature

    total += temperature

average = total / len(temperatures)

above_average = 0
below_average = 0

for temperature in temperatures:

    if temperature > average:
        above_average += 1

    elif temperature < average:
        below_average += 1

print("\n29. Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above_average)
print("Days below average:", below_average)


# ============================================================
# 30. Patient management using two lists
# ============================================================

patient_names = ["Amit", "Sneha", "Rahul"]
patient_ages = [25, 30, 45]

while True:
    print("\n30. Patient Management")
    print("1. Add patient")
    print("2. Delete patient")
    print("3. Search patient")
    print("4. Display all patients")
    print("5. Count total patients")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))

        patient_names.append(name)
        patient_ages.append(age)

        print("Patient added")

    elif choice == 2:

        name = input("Enter patient name to delete: ")

        if name in patient_names:
            index = patient_names.index(name)

            patient_names.pop(index)
            patient_ages.pop(index)

            print("Patient deleted")
        else:
            print("Patient not found")

    elif choice == 3:

        name = input("Enter patient name to search: ")

        if name in patient_names:
            index = patient_names.index(name)

            print("Patient found")
            print("Name:", patient_names[index])
            print("Age:", patient_ages[index])
        else:
            print("Patient not found")

    elif choice == 4:

        print("Patient Details:")

        for i in range(len(patient_names)):
            print("Name:", patient_names[i])
            print("Age:", patient_ages[i])

    elif choice == 5:

        print("Total patients:", len(patient_names))

    elif choice == 6:
        break

    else:
        print("Invalid choice")