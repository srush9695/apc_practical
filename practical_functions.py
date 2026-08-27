# -------------------- 1. Factorial --------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("1. Factorial:", factorial(5))


# -------------------- 2. Even or Odd --------------------
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print("2. Even/Odd:", check_even_odd(7))


# -------------------- 3. Greater of Two Numbers --------------------
def greater(a, b):
    return a if a > b else b

print("3. Greater:", greater(10, 20))


# -------------------- 4. Simple Interest --------------------
def simple_interest(p, r, t):
    return (p * r * t) / 100

print("4. Simple Interest:", simple_interest(10000, 5, 2))


# -------------------- 5. Prime Number --------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("5. Prime:", is_prime(17))


# -------------------- 6. Area of Circle --------------------
def circle_area(radius):
    return 3.14159 * radius * radius

print("6. Circle Area:", circle_area(5))


# -------------------- 7. Sum of First n Natural Numbers --------------------
def natural_sum(n):
    return n * (n + 1) // 2

print("7. Natural Number Sum:", natural_sum(10))


# -------------------- 8. Power --------------------
def power(base, exponent):
    return base ** exponent

print("8. Power:", power(2, 5))


# -------------------- 9. Largest Without max() --------------------
def largest(numbers):
    big = numbers[0]
    for n in numbers:
        if n > big:
            big = n
    return big

print("9. Largest:", largest([10, 25, 5, 40, 15]))


# -------------------- 10. Count Vowels --------------------
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print("10. Vowels:", count_vowels("Hello World"))


# -------------------- 11. Reverse String --------------------
def reverse_string(text):
    return text[::-1]

print("11. Reverse:", reverse_string("Python"))


# -------------------- 12. Palindrome --------------------
def is_palindrome(value):
    text = str(value)
    return text == text[::-1]

print("12. Palindrome:", is_palindrome("madam"))


# -------------------- 13. Average of List --------------------
def average(numbers):
    return sum(numbers) / len(numbers)

print("13. Average:", average([10, 20, 30, 40, 50]))


# -------------------- 14. Count Occurrences --------------------
def count_occurrences(items, element):
    count = 0
    for item in items:
        if item == element:
            count += 1
    return count

print("14. Occurrences:", count_occurrences([1, 2, 2, 3, 2], 2))


# -------------------- 15. Unique Elements --------------------
def unique_elements(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print("15. Unique:", unique_elements([1, 2, 2, 3, 1, 4]))


# -------------------- 16. Second Largest --------------------
def second_largest(numbers):
    unique = unique_elements(numbers)
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

print("16. Second Largest:", second_largest([10, 30, 20, 40, 30]))


# -------------------- 17. Fibonacci --------------------
def fibonacci(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print("17. Fibonacci:", fibonacci(8))


# -------------------- 18. Percentage and Grade --------------------
def percentage_grade(marks):
    percentage = sum(marks) / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade

print("18. Percentage and Grade:", percentage_grade([85, 90, 78, 88, 92]))


# -------------------- 19. Electricity Bill by Slabs --------------------
def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7
    return bill

print("19. Electricity Bill:", electricity_bill(250))


# -------------------- 20. Gross Salary --------------------
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

print("20. Gross Salary:", gross_salary(30000))


# -------------------- 21. Bill After Discount --------------------
def total_bill(prices, quantities, discount=10):
    total = 0
    for price, quantity in zip(prices, quantities):
        total += price * quantity
    return total - (total * discount / 100)

print("21. Discounted Bill:", total_bill([100, 200, 50], [2, 1, 3], 10))


# -------------------- 22. Min, Max, Sum, Average --------------------
def list_statistics(numbers):
    smallest = numbers[0]
    biggest = numbers[0]

    for n in numbers:
        if n < smallest:
            smallest = n
        if n > biggest:
            biggest = n

    total = sum(numbers)
    avg = total / len(numbers)

    return smallest, biggest, total, avg

print("22. Statistics:", list_statistics([10, 20, 5, 40, 30]))


# -------------------- 23. Student Records --------------------
def student_details(name, roll, marks):
    total = sum(marks)
    percentage, grade = percentage_grade(marks)
    return {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

def process_students(students):
    records = []
    for student in students:
        records.append(student_details(student[0], student[1], student[2]))

    class_average = sum(r["percentage"] for r in records) / len(records)
    highest = max(records, key=lambda x: x["percentage"])
    lowest = min(records, key=lambda x: x["percentage"])

    return records, class_average, highest, lowest

students = [
    ("Asha", 1, [80, 85, 90, 75, 88]),
    ("Riya", 2, [70, 78, 75, 80, 72]),
    ("Neha", 3, [92, 90, 95, 94, 91])
]

records, class_avg, high, low = process_students(students)
print("23. Student Records:", records)
print("    Class Average:", class_avg)
print("    Highest Scorer:", high["name"])
print("    Lowest Scorer:", low["name"])


# -------------------- 24. Bank Account --------------------
balance = 1000
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited " + str(amount))
    return balance

def withdrawal(amount):
    global balance
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    transactions.append("Withdrawn " + str(amount))
    return balance

def balance_enquiry():
    return balance

def transaction_history():
    return transactions

print("24. Deposit:", deposit(500))
print("    Withdrawal:", withdrawal(200))
print("    Balance:", balance_enquiry())
print("    History:", transaction_history())


# -------------------- 25. Library Management --------------------
books = {}

def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return "Book issued"
    return "Book not available"

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        return "Book returned"
    return "Book not found"

def search_book(title):
    result = []
    for book in books.values():
        if title.lower() in book["title"].lower():
            result.append(book["title"])
    return result

def display_available():
    return [book["title"] for book in books.values() if book["available"]]

add_book(1, "Python Programming")
add_book(2, "Data Structures")
print("25. Search:", search_book("Python"))
print("    Issue:", issue_book(1))
print("    Available:", display_available())
print("    Return:", return_book(1))


# -------------------- 26. Modular Electricity Bill --------------------
def slab_charge(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return 200 + (units - 100) * 3
    elif units <= 300:
        return 500 + (units - 200) * 5
    return 1000 + (units - 300) * 7

def fixed_charge():
    return 100

def electricity_tax(amount):
    return amount * 0.05

def electricity_discount(amount):
    return amount * 0.10 if amount > 2000 else 0

def final_electricity_bill(units):
    amount = slab_charge(units) + fixed_charge()
    tax = electricity_tax(amount)
    discount = electricity_discount(amount)
    return amount + tax - discount

print("26. Modular Electricity Bill:", final_electricity_bill(350))


# -------------------- 27. Hospital Bill --------------------
def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(amount):
    return amount

def hospital_final_bill(category, consultation, laboratory, medicine, room):
    total = (consultation_charges(consultation) +
             laboratory_charges(laboratory) +
             medicine_charges(medicine) +
             room_charges(room))

    discount_rate = {"general": 0, "senior": 0.10, "child": 0.05}
    discount = total * discount_rate.get(category.lower(), 0)
    return total - discount

print("27. Hospital Final Bill:",
      hospital_final_bill("senior", 500, 1000, 800, 1500))


# -------------------- 28. Product Invoice --------------------
cart = {}

def add_product(name, price, quantity):
    cart[name] = {"price": price, "quantity": quantity}

def remove_product(name):
    if name in cart:
        del cart[name]

def subtotal():
    return sum(p["price"] * p["quantity"] for p in cart.values())

def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    return 0

def calculate_gst(amount):
    return amount * 0.18

def final_invoice(coupon=""):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    taxable = sub - discount
    gst = calculate_gst(taxable)
    return sub, discount, gst, taxable + gst

add_product("Pen", 20, 5)
add_product("Notebook", 100, 2)
print("28. Invoice:", final_invoice("SAVE10"))


# -------------------- 29. Recursive Binary Search --------------------
def binary_search(numbers, target, low=0, high=None):
    if high is None:
        high = len(numbers) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, high)

print("29. Binary Search Index:",
      binary_search([10, 20, 30, 40, 50], 40))


# -------------------- 30. Decimal to Binary Using Recursion --------------------
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

print("30. Decimal to Binary:", decimal_to_binary(10))


# -------------------- 31. Recursive Palindrome --------------------
def recursive_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return recursive_palindrome(text[1:-1])

print("31. Recursive Palindrome:", recursive_palindrome("madam"))


# -------------------- 32. Passing Functions as Arguments --------------------
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

print("32. Addition:", calculate(10, 5, addition))
print("    Subtraction:", calculate(10, 5, subtraction))
print("    Multiplication:", calculate(10, 5, multiplication))
print("    Division:", calculate(10, 5, division))


# ============================================================
# LAMBDA PROGRAMS
# ============================================================

# -------------------- 33. Lambda Square --------------------
square = lambda n: n * n
print("33. Square:", square(5))


# -------------------- 34. Lambda Cube --------------------
cube = lambda n: n * n * n
print("34. Cube:", cube(3))


# -------------------- 35. Lambda Even --------------------
even = lambda n: n % 2 == 0
print("35. Even:", even(8))


# -------------------- 36. Lambda Maximum --------------------
lambda_max = lambda a, b: a if a > b else b
print("36. Maximum:", lambda_max(10, 20))


# -------------------- 37. Lambda Simple Interest --------------------
lambda_si = lambda p, r, t: (p * r * t) / 100
print("37. Simple Interest:", lambda_si(10000, 5, 2))


# -------------------- 38. map() + lambda Squares --------------------
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("38. Squares:", squares)


# -------------------- 39. map() + lambda Cubes --------------------
cubes = list(map(lambda x: x ** 3, numbers))
print("39. Cubes:", cubes)


# -------------------- 40. map() + lambda Corresponding Sum --------------------
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = list(map(lambda a, b: a + b, list1, list2))
print("40. Corresponding Sums:", sums)


# -------------------- 41. filter() + lambda Even Numbers --------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("41. Even Numbers:", even_numbers)


# -------------------- 42. filter() + lambda Prime Numbers --------------------
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("42. Prime Numbers:", prime_numbers)


# -------------------- 43. filter() + lambda Positive Numbers --------------------
numbers = [-5, 3, -2, 8, 0, 10]
positive = list(filter(lambda x: x > 0, numbers))
print("43. Positive Numbers:", positive)


# -------------------- 44. filter() + lambda Greater Than 50 --------------------
numbers = [20, 55, 70, 40, 90, 10]
greater_50 = list(filter(lambda x: x > 50, numbers))
print("44. Greater Than 50:", greater_50)


# -------------------- 45. filter() + lambda Words > 5 Characters --------------------
words = ["apple", "banana", "cat", "orange", "book", "python"]
long_words = list(filter(lambda word: len(word) > 5, words))
print("45. Long Words:", long_words)


# -------------------- 46. Sort Words by Length --------------------
words = ["apple", "hi", "banana", "cat", "elephant"]
words.sort(key=lambda word: len(word))
print("46. Words by Length:", words)


# -------------------- 47. Sort Students by Marks --------------------
students_marks = [
    ("Asha", 85),
    ("Riya", 70),
    ("Neha", 95),
    ("Pooja", 80)
]
students_marks.sort(key=lambda student: student[1])
print("47. Students by Marks:", students_marks)


# -------------------- 48. Sort Employees by Salary --------------------
employees = [
    ("Amit", 45000),
    ("Ravi", 60000),
    ("Neha", 50000),
    ("Priya", 75000)
]
employees.sort(key=lambda employee: employee[1])
print("48. Employees by Salary:", employees)


# -------------------- 49. Student Names and Marks --------------------
def student_average(records):
    return sum(mark for name, mark in records) / len(records)

def students_above_75(records):
    return list(filter(lambda x: x[1] > 75, records))

def sort_students(records):
    return sorted(records, key=lambda x: x[1])

student_list = [
    ("Asha", 80),
    ("Riya", 70),
    ("Neha", 90),
    ("Pooja", 76)
]

print("49(a). Average Marks:", student_average(student_list))
print("49(b). Above 75:", students_above_75(student_list))
print("49(c). Sorted:", sort_students(student_list))


# -------------------- 50. Employee Records --------------------
employee_records = [
    ("Amit", "IT", 60000),
    ("Ravi", "HR", 45000),
    ("Neha", "IT", 70000),
    ("Priya", "Sales", 55000)
]

high_salary = list(filter(lambda e: e[2] > 50000, employee_records))

increased_salary = list(map(
    lambda e: (e[0], e[1], e[2] * 1.10),
    employee_records
))

sorted_employees = sorted(employee_records, key=lambda e: e[2])

print("50(a). Salary > 50000:", high_salary)
print("50(b). Salary +10%:", increased_salary)
print("50(c). Sorted by Salary:", sorted_employees)


# -------------------- 51. Product Records --------------------
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Pen", 20, 10)
]

def product_values(products):
    return list(map(
        lambda p: (p[0], p[1], p[2], p[1] * p[2]),
        products
    ))

def products_above_1000(products):
    return list(filter(lambda p: p[1] > 1000, products))

def sort_products_by_value(products):
    return sorted(products, key=lambda p: p[1] * p[2])

print("51(a). Product Values:", product_values(products))
print("51(b). Price > 1000:", products_above_1000(products))
print("51(c). Sorted by Total Value:", sort_products_by_value(products))


# -------------------- 52. Process Words --------------------
word_list = ["apple", "banana", "cat", "elephant", "book", "computer"]

def word_lengths(words):
    return list(map(lambda word: len(word), words))

def words_more_than_five(words):
    return list(filter(lambda word: len(word) > 5, words))

def sort_words_by_length(words):
    return sorted(words, key=lambda word: len(word))

print("52(a). Word Lengths:", word_lengths(word_list))
print("52(b). More Than 5 Characters:", words_more_than_five(word_list))
print("52(c). Sorted by Length:", sort_words_by_length(word_list))
