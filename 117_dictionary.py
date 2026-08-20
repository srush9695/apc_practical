# 1. Student details - display all key-value pairs
print("\n--- 1. Student Details ---")

student = {
    "roll_no": 101,
    "name": "Srushti",
    "department": "CSE",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# 2. Employee information - display value of specified key
print("\n--- 2. Employee Information ---")

employee = {
    "id": 1001,
    "name": "Rahul",
    "department": "IT",
    "salary": 55000
}

key = "name"
print("Value of", key, ":", employee[key])


# 3. Add new product
print("\n--- 3. Add Product ---")

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

products["Printer"] = 10000
print(products)


# 4. Update student marks
print("\n--- 4. Update Marks ---")

marks = {
    "Amit": 75,
    "Rahul": 82,
    "Sneha": 90
}

marks["Rahul"] = 88
print(marks)


# 5. Remove specified city
print("\n--- 5. Remove City ---")

cities = {
    "Mumbai": 20,
    "Pune": 7,
    "Delhi": 19,
    "Chennai": 11
}

del cities["Pune"]
print(cities)


# 6. Check employee ID
print("\n--- 6. Employee ID Search ---")

employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists:", employees[emp_id])
else:
    print("Employee does not exist")


# 7. Count key-value pairs
print("\n--- 7. Number of Records ---")

records = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90,
    "Priya": 85
}

print("Total key-value pairs:", len(records))


# 8. Display keys, values and pairs
print("\n--- 8. Keys, Values and Items ---")

data = {
    "Name": "Srushti",
    "Age": 20,
    "Department": "CSE"
}

print("Keys:", data.keys())
print("Values:", data.values())
print("Key-Value pairs:", data.items())


# 9. Programming languages and creators
print("\n--- 9. Programming Languages ---")

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}

for language, creator in languages.items():
    print(language, ":", creator)


# 10. Accept five students and marks
print("\n--- 10. Five Students ---")

students = {}

for i in range(5):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    students[name] = mark

print("Student Dictionary:", students)


# 11. Student with highest marks
print("\n--- 11. Highest Marks ---")

students = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 95,
    "Priya": 82
}

highest = max(students, key=students.get)

print("Student with highest marks:", highest)
print("Marks:", students[highest])


# 12. Student with lowest marks
print("\n--- 12. Lowest Marks ---")

lowest = min(students, key=students.get)

print("Student with lowest marks:", lowest)
print("Marks:", students[lowest])


# 13. Average marks
print("\n--- 13. Average Marks ---")

average = sum(students.values()) / len(students)

print("Average marks:", average)


# 14. Character frequency
print("\n--- 14. Character Frequency ---")

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:", frequency)


# 15. Word frequency
print("\n--- 15. Word Frequency ---")

sentence = input("Enter a sentence: ")

words = sentence.split()
word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Word frequency:", word_frequency)


# 16. Merge two dictionaries
print("\n--- 16. Merge Dictionaries ---")

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:", merged)


# 17. Common keys
print("\n--- 17. Common Keys ---")

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}

common_keys = dict1.keys() & dict2.keys()

print("Common keys:", common_keys)


# 18. Common values
print("\n--- 18. Common Values ---")

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 30, "z": 40}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:", common_values)


# 19. Remove duplicate values
print("\n--- 19. Remove Duplicate Values ---")

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

unique_data = {}

for key, value in data.items():
    if value not in unique_data.values():
        unique_data[key] = value

print("Original:", data)
print("After removing duplicates:", unique_data)


# 20. Display dictionary in ascending order of keys
print("\n--- 20. Ascending Order of Keys ---")

data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

for key in sorted(data):
    print(key, ":", data[key])


# 21. Squares from 1 to 10
print("\n--- 21. Squares 1 to 10 ---")

squares = {}

for i in range(1, 11):
    squares[i] = i ** 2

print(squares)


# 22. Squares of even numbers from 1 to 20
print("\n--- 22. Even Numbers and Squares ---")

even_squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        even_squares[i] = i ** 2

print(even_squares)


# 23. Frequency of unique numbers in a list
print("\n--- 23. Number Frequency ---")

numbers = [1, 2, 3, 2, 4, 1, 3, 2, 5]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Frequency:", frequency)


# 24. Cubes from 1 to 10
print("\n--- 24. Cubes 1 to 10 ---")

cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print(cubes)


# 25. Student Management System
print("\n--- 25. Student Management System ---")

students = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 95
}

# Add student
name = input("Enter student name to add: ")
mark = float(input("Enter marks: "))
students[name] = mark

# Update marks
name = input("Enter student name to update: ")

if name in students:
    students[name] = float(input("Enter new marks: "))
else:
    print("Student not found")

# Delete student
name = input("Enter student name to delete: ")

if name in students:
    del students[name]
else:
    print("Student not found")

# Search student
name = input("Enter student name to search: ")

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

# Display all students
print("All students:")

for name, mark in students.items():
    print(name, ":", mark)

# Highest marks
if students:
    highest = max(students, key=students.get)
    print("Highest:", highest, students[highest])

# Average
if students:
    print("Average:", sum(students.values()) / len(students))


# 26. Employee salaries
print("\n--- 26. Employee Salary ---")

employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Priya": 50000
}

highest_employee = max(employees, key=employees.get)
lowest_employee = min(employees, key=employees.get)

print("Highest salary:",
      highest_employee, employees[highest_employee])

print("Lowest salary:",
      lowest_employee, employees[lowest_employee])

average_salary = sum(employees.values()) / len(employees)

print("Average salary:", average_salary)

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


# 27. Product quantity management
print("\n--- 27. Product Management ---")

products = {
    "Pen": 20,
    "Book": 15,
    "Pencil": 5,
    "Bag": 8
}

# Add
name = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity

# Update
name = input("Enter product to update: ")

if name in products:
    products[name] = int(input("Enter new quantity: "))
else:
    print("Product not found")

# Delete
name = input("Enter product to delete: ")

if name in products:
    del products[name]
else:
    print("Product not found")

# Search
name = input("Enter product to search: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

# Products below 10
print("Products with quantity below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, ":", quantity)


# 28. Contact management
print("\n--- 28. Contact Management ---")

contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234"
}

# Add contact
name = input("Enter contact name: ")
phone = input("Enter phone number: ")
contacts[name] = phone

# Search contact
name = input("Enter contact to search: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

# Update contact
name = input("Enter contact to update: ")

if name in contacts:
    contacts[name] = input("Enter new phone number: ")
else:
    print("Contact not found")

# Delete contact
name = input("Enter contact to delete: ")

if name in contacts:
    del contacts[name]
else:
    print("Contact not found")

# Display all
print("All Contacts:")

for name, phone in contacts.items():
    print(name, ":", phone)


# 29. Book management
print("\n--- 29. Book Management ---")

books = {
    101: "Python Programming",
    102: "Java Programming",
    103: "Data Structures"
}

# Add book
book_id = int(input("Enter book ID to add: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

# Search book
book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")

# Remove book
book_id = int(input("Enter book ID to remove: "))

if book_id in books:
    del books[book_id]
else:
    print("Book not found")

# Display books
print("All Books:")

for book_id, book_name in books.items():
    print(book_id, ":", book_name)

# Count books
print("Total books:", len(books))


# 30. Group students according to department
print("\n--- 30. Group Students by Department ---")

students = {
    "Amit": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Neha": "IT"
}

groups = {}

for name, department in students.items():

    if department not in groups:
        groups[department] = []

    groups[department].append(name)

print(groups)


# 31. Group words according to length
print("\n--- 31. Words Grouped by Length ---")

words = ["cat", "dog", "apple", "bat", "banana", "car"]

word_groups = {}

for word in words:

    length = len(word)

    if length not in word_groups:
        word_groups[length] = []

    word_groups[length].append(word)

print(word_groups)


# 32. Two numbers whose sum equals target
print("\n--- 32. Two Sum ---")

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for number in numbers:

    required = target - number

    if required in seen:
        print("Numbers:", required, "and", number)
        break

    seen[number] = True
else:
    print("No pair found")


# 33. First character occurring only once
print("\n--- 33. First Non-Repeating Character ---")

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

found = False

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        found = True
        break

if not found:
    print("No non-repeating character")


# 34. First character occurring more than once
print("\n--- 34. First Repeating Character ---")

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

found = False

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        found = True
        break

if not found:
    print("No repeating character")


# 35. Paragraph - word length and number of words
print("\n--- 35. Word Length Frequency ---")

paragraph = input("Enter a paragraph: ")

words = paragraph.split()

length_frequency = {}

for word in words:

    # Remove common punctuation
    word = word.strip(".,!?;:")

    length = len(word)

    length_frequency[length] = length_frequency.get(length, 0) + 1

print("Word length : Number of words")

for length, count in sorted(length_frequency.items()):
    print(length, ":", count)
