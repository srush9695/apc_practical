#1
import re

# Input string
text = "Hello123 World456!"

# Extract all digits
digits = re.findall(r'\d', text)

# Display the result
print("Digits:", digits)
print("All digits:", ''.join(digits))

#2.Accept a sentence and display all words beginning with the letter A or a.
import re
text="This apple is sp sweet and i like ants"
res=re.findall(r'\b[Aa]\w*',text)
print(res)

#3Write a program to extract all uppercase letters from a given string.
import re
text = "Hello PYTHON World"
result = re.findall(r'[A-Z]', text)

print(result)

#4Count the occurrences of vowels in a given string using regular expressions.
import re

text = "Hello Python Programming"
result = re.findall(r'[aeiou]', text, re.I)

print("Number of vowels:", len(result))

#5.Identify all spaces, tabs, and newline characters in a text.
import re

text = "Hello World\tPython\nProgramming"
result = re.findall(r'[ \t\n]', text)

print("Whitespace characters:", len(result))
print(result)

#6.Replace multiple consecutive spaces with a single space.
import re

text = "Python    is   very    easy"
result = re.sub(r' +', ' ', text)

print(result)

#7.Accept a sentence and display all words containing exactly five characters.
import re

text = "Hello there Python world today"
result = re.findall(r'\b[A-Za-z]{5}\b', text)

print(result)

#8.Write a program to identify all words ending with the letter s.
import re

text = "Cats and dogs are good pets"
result = re.findall(r'\b\w+s\b', text, re.I)

print(result)

#9.remove all special characters while retaining letters, digits, and spaces.
import re

text = "Hello@Python#123! Welcome$"
result = re.sub(r'[^A-Za-z0-9 ]', '', text)

print(result)

#10.Count the number of words in a sentence using regular expressions.

import re

text = "Python is easy to learn"
words = re.findall(r'\b\w+\b', text)

print("Number of words:", len(words))

#11.Validate an Indian mobile number containing exactly 10 digits and beginning with 6, 7, 8, or 9.
import re

number = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

#12.Accept an email address and check whether it follows a reasonable email format.
import re

email = input("Enter email: ")

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

if re.fullmatch(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")

#13.Extract all dates in DD-MM-YYYY format from a paragraph.
import re

text = "Events are on 15-08-2025 and 26-01-2026"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

print(dates)
#14.import re

text = "Visit https://google.com and http://example.org"

urls = re.findall(r'https?://[^\s]+', text)

print(urls)
#15.
import re

text = "Learning #Python and #Regex is fun #Programming"

hashtags = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text)

print(hashtags)

#16
import re

password = input("Enter password: ")

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}'

if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")

#17
import re

text = "This is is a test TEST sentence"

pattern = r'\b(\w+)\s+\1\b'
matches = re.findall(pattern, text, re.I)

print("Repeated words:", matches)

#18
import re

text = "Pune PIN is 411001 and another PIN is 110001"

pattern = r'\b[1-9]\d{5}\b'
pins = re.findall(pattern, text)

print(pins)

#19
import re

number = input("Enter vehicle number: ").upper()

pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'

if re.fullmatch(pattern, number):
    print("Format is valid")
else:
    print("Invalid format")

#20    
import re

text = "Files: report.pdf image.png notes.txt program.py"

extensions = re.findall(
    r'\b[\w-]+\.(\w+)\b', text
)
print(extensions)
#21
import re

text = "<p>Hello!!!   Python,   is <b>easy</b>.</p>"

text = re.sub(r'<[^>]+>', '', text)
text = re.sub(r'[^\w\s.!?]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print(text)

#22
import re

text = """
Invoice No: INV-12345
Date: 15-08-2025
Amount: Rs. 2500.50
"""

invoice = re.search(r'INV-\d+', text)
date = re.search(r'\d{2}-\d{2}-\d{4}', text)
amount = re.search(r'Rs\.?\s*[\d,]+(?:\.\d{2})?', text)

print("Invoice:", invoice.group())
print("Date:", date.group())
print("Amount:", amount.group())

#23
import re

code = '''
x = 10  # variable
# This is a comment
print("Hello # Python")
'''

pattern = r'^\s*#.*$|(?<=\s)#.*$'
comments = re.findall(pattern, code, re.M)

print(comments)

#24
import re

code = input("Enter product code: ")

pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'

if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")

#25    
import re

text = """
Name: Rahul, Roll: 101, Marks: 85
Name: Priya, Roll: 102, Marks: 92
"""

pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'

students = re.findall(pattern, text)

for name, roll, marks in students:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print()

#26
import re

text = """
Research paper published in 2023.
DOI: 10.1234/abcd.5678
Email: author@example.com
URL: https://example.com/paper
"""

dois = re.findall(
    r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b',
    text, re.I
)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    text
)
urls = re.findall(r'https?://[^\s]+', text)

print("DOIs:", dois)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)






















































































































    

















































































