#1.Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.
with open("student.txt", "w") as file:
        file.write("Name: Srushti patil\n")
        file.write("Roll Number: 101\n")
        file.write("Branch: Computer Engineering\n")
        file.write("Semester: 6\n")
print("Student information written successfully.")
#2.Write a program to open a text file and display its complete contents.
with open("student.txt", "r") as file:
    c=file.read()
print("content:",c)
#3.Write a program to append additional student information to an existing file without deleting its previous contents.
with open("student.txt", "a") as file:
        file.write("subject: python programming \n")
        file.write("marks: 96")
print("Student information appended successfully")
#4.Write a program to read a text file line by line and display each line separately.
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())
#5.Write a program to count and display the total number of lines present in a text file.
with open("student.txt", "r") as file:
    lines = file.readlines()
print("Total number of lines:", len(lines))
#6.Write a program to count the total number of words present in a text file.
with open("student.txt", "r") as file:
    line=file.read()
words = line.split()
print("Total number of words:", len(words))
#7.Write a program to count the total number of characters in a text file, including spaces.
with open("student.txt", "r") as file:
    line=file.read()
print("total no. of characters:",len(line))
#8.Write a program to read a text file and display its lines in reverse order
with open("student.txt", "r") as file:
    line=file.readlines()
print("Lines in reverse order:")
for line in reversed(lines):
        print(line.strip())
#9.Read a text file and count the number of vowels and consonants present in the file.
with open("student.txt", "r") as file:
      data = file.read().lower()
vowels = 0
consonants = 0
for ch in data:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
#10.Read a text file and calculate the number of alphabets, digits, spaces, and special characters.
with open("student.txt", "r") as file:
      data = file.read().lower()
alph=0
d=0
s=0
sc=0
for ch in data:
    if ch.isalpha():
        alph+=1
    elif ch.isdigit():
        d+=1
    elif ch.isspace():
            s += 1
    else:
            sc += 1
print("Alphabets:", alph)
print("Digits:", d)
print("Spaces:", s)
print("Special characters:", sc)
#11.Read a text file and find the longest word present in the file.
with open("student.txt", "r") as file:
      data = file.read().lower()
words = data.split()
if words:
        longest = max(words, key=len)
        print("Longest word:", longest)
        print("Length:", len(longest))
#12.Read a text file and count how many times each word occurs. Display the result using a dictiona  
with open("student.txt", "r") as file:
    data = file.read().lower()
f={}
word=data.split()
for ch in word:
    f[ch]=f.get(ch,0)+1
print("frequency of each word")    
for key,value in f.items():
    print(key,":",value)
#13.Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
search_word = input("Enter word to search: ")
count = 0
line_numbers = []
with open("student.txt", "r") as file:
 for line_no, line in enumerate(file, start=1):
            words = line.lower().split()
            for word in words:
                word = word.strip(".,!?;:")
                if word == search_word.lower():
                    count += 1
                    line_numbers.append(line_no)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)
#14.Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
with open("student.txt", "r") as file:
    data = file.read()
if old_word in data:
    data = data.replace(old_word, new_word)
    with open("student_modified.txt", "w") as file:
        file.write(data)
    print("Word replaced successfully.")
else:
    print("Word not found in file.")
#15.Read a Python source file and create another file after removing single-line comments.    
source_file = "sample.py"
output_file = "without_comments.py"
    # Create sample Python file
with open(source_file, "w") as file:
        file.write("# This is a comment\n")
        file.write("x = 10\n")
        file.write("print(x)  # display value\n")
        file.write("# Another comment\n")
with open(source_file, "r") as source:
        lines = source.readlines()
with open(output_file, "w") as output:
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if "#" in line:
                line = line.split("#")[0].rstrip() + "\n"
            output.write(line)
print("Comments removed successfully.")            
#16.	Read a text file and create another file containing the same text in uppercase.
with open("student.txt", "r") as file:
        data = file.read()
with open("uppercase.txt", "w") as file:
        file.write(data.upper())
print("Uppercase file created successfully.")
#17.	Create a file containing student records in the format:RollNo,Name,Marks101,Amit,85102,Priya,92103,Rahul,78
#Write a program to:
#Display all records. 
#•	Find the student with the highest marks. 
#•	Calculate average marks. 
#•	Display students who scored more than 80.
with open("stud.txt","w") as f:
    f.write("RollNo,Name,Marks \n")
    f.write("101,Amit,85\n")
    f.write("102,Priya,92 \n")
    f.write("103,Rahul,78 \n")
with open("stud.txt", "r") as file:
    lines = file.readlines()
print("All Student Records:")
for line in lines:
    print(line.strip())
highest = 0
highest_name = ""
total = 0
count = 0
print("\nStudents who scored more than 80:")
for line in lines[1:]:
    data = line.strip().split(",")

    rollno = data[0]
    name = data[1]
    marks = int(data[2])

    total = total + marks
    count = count + 1

    if marks > highest:
        highest = marks
        highest_name = name

    if marks > 80:
        print(rollno, name, marks)

average = total / count

print("\nStudent with Highest Marks:")
print(highest_name, highest)

print("\nAverage Marks:", average)
#18.	Store employee ID, name, department, and salary in a file. Write functions to: 
#•	Display all employees. 
#•	Find the highest-paid employee. 
#•	Calculate average salary. 
#•	Display employees earning above a given salary.
# Store employee records
file = open("employee.txt", "w")
file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,45000\n")
file.write("103,Rahul,Sales,60000\n")
file.write("104,Neha,IT,55000\n")
file.close()
file = open("employee.txt", "r")
print("All Employees:")
for line in file:
    print(line.strip())
file.close()
# Highest salary
file = open("employee.txt", "r")
high = 0
name = ""

for line in file:
    id, empname, dept, salary = line.strip().split(",")
    salary = int(salary)
    if salary > high:
        high = salary
        name = empname
file.close()
print("Highest Paid Employee:", name, high)
# Average salary
file = open("employee.txt", "r")
total = 0
count = 0
for line in file:
    id, name, dept, salary = line.strip().split(",")
    total += int(salary)
    count += 1
file.close()
print("Average Salary:", total / count)
# Employees earning above 50000
file = open("employee.txt", "r")
print("Employees earning above 50000:")
for line in file:
    id, name, dept, salary = line.strip().split(",")
    if int(salary) > 50000:
        print(id, name, dept, salary)
file.close()
#19.	Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
# Store attendance records
file = open("attendance.txt", "w")
file.write("101,Amit,40,50\n")
file.write("102,Priya,45,50\n")
file.write("103,Rahul,30,50\n")
file.write("104,Neha,35,50\n")
file.close()
# Calculate attendance percentage
file = open("attendance.txt", "r")
print("Students having attendance below 75%:")
for line in file:
    roll, name, present, total = line.strip().split(",")
    percentage = (int(present) / int(total)) * 100
    if percentage < 75:
        print("Below 75%:", name)
        print(name, "Attendance:", percentage, "%")
file.close()
#20.	Store deposits and withdrawals in a file. Read the file and calculate: 
#•	Total deposits 
#•	Total withdrawals 
#•	Final balance 
#•	Largest transaction
# Store transactions
file = open("bank.txt", "w")

file.write("Deposit,5000\n")
file.write("Withdrawal,2000\n")
file.write("Deposit,3000\n")
file.write("Withdrawal,1000\n")

file.close()

# Read file and calculate
file = open("bank.txt", "r")

deposit = 0
withdrawal = 0
largest = 0

for line in file:
    type, amount = line.strip().split(",")
    amount = int(amount)

    if type == "Deposit":
        deposit += amount
    else:
        withdrawal += amount

    if amount > largest:
        largest = amount

file.close()

balance = deposit - withdrawal

print("Total Deposits:", deposit)
print("Total Withdrawals:", withdrawal)
print("Final Balance:", balance)
print("Largest Transaction:", largest)
#21.	Maintain book records containing book ID, title, author, and availability status. Implement operations to: 
#•	Add a book. 
#•	Search for a book. 
#•	Issue a book. 
#•	Return a book. 
#•	Display available books.
# Store book records
file = open("books.txt", "w")

file.write("101,Python Basics,Guido,Available\n")
file.write("102,Java Programming,James,Available\n")
file.write("103,Data Science,John,Issued\n")

file.close()


# Add a book
file = open("books.txt", "a")
file.write("104,Cloud Computing,Andrew,Available\n")
file.close()

print("Book added successfully.")


# Search for a book
search_id = input("Enter Book ID to search: ")

file = open("books.txt", "r")

for line in file:
    id, title, author, status = line.strip().split(",")

    if id == search_id:
        print("Book Found:", title, author, status)

file.close()


# Issue a book
issue_id = input("Enter Book ID to issue: ")

file = open("books.txt", "r")
books = file.readlines()
file.close()

file = open("books.txt", "w")

for line in books:
    id, title, author, status = line.strip().split(",")

    if id == issue_id and status == "Available":
        status = "Issued"
        print("Book Issued")

    file.write(id + "," + title + "," + author + "," + status + "\n")

file.close()


# Return a book
return_id = input("Enter Book ID to return: ")

file = open("books.txt", "r")
books = file.readlines()
file.close()

file = open("books.txt", "w")

for line in books:
    id, title, author, status = line.strip().split(",")

    if id == return_id:
        status = "Available"
        print("Book Returned")

    file.write(id + "," + title + "," + author + "," + status + "\n")

file.close()


# Display available books
print("\nAvailable Books:")

file = open("books.txt", "r")

for line in file:
    id, title, author, status = line.strip().split(",")

    if status == "Available":
        print(id, title, author)

file.close()
#22.	Read the contents of two text files and create a third file containing the contents of both files.
# Read first file
file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

# Read second file
file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

# Create third file
file3 = open("file3.txt", "w")
file3.write(data1)
file3.write(data2)
file3.close()

print("Contents copied to file3.txt")
#23.	Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

line_no = 1
same = True

while True:
    line1 = file1.readline()
    line2 = file2.readline()

    if line1 != line2:
        print("Files are different.")
        print("First different line:", line_no)
        same = False
        break

    if line1 == "":
        break

    line_no += 1

file1.close()
file2.close()

if same:
    print("Files are identical.")












    
    
    
