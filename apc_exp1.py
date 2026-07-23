# Combined Program: Data Types and Operators in Python

print("----- DATA TYPES -----")

# Integer
a = 10
print("Integer:", a, type(a))

# Float
b = 5.5
print("Float:", b, type(b))

# String
c = "Hello Python"
print("String:", c, type(c))

# Boolean
d = True
print("Boolean:", d, type(d))

# List
e = [1, 2, 3]
print("List:", e, type(e))

# Tuple
f = (10, 20, 30)
print("Tuple:", f, type(f))

# Set
g = {1, 2, 3, 3}
print("Set:", g, type(g))

# Dictionary
h = {"name": "Srushti", "age": 21}
print("Dictionary:", h, type(h))


print("\n----- OPERATORS -----")

x = 10
y = 5

# Arithmetic Operators
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Power:", x ** y)
print("Floor Division:", x // y)

# Comparison Operators
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Logical Operators
p = True
q = False
print("AND:", p and q)
print("OR:", p or q)
print("NOT p:", not p)

# Assignment Operators
z = 10
z += 5
print("z += 5:", z)
z -= 3
print("z -= 3:", z)
z *= 2
print("z *= 2:", z)

# Membership Operators
list1 = [1, 2, 3]
print("2 in list:", 2 in list1)
print("4 not in list:", 4 not in list1)

# Identity Operators
m = [1, 2]
n = [1, 2]
o = m
print("m is o:", m is o)
print("m is n:", m is n)
print("m is not n:", m is not n)