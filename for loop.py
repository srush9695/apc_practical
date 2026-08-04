# -------------------------------
# 1. Natural numbers up to n
# -------------------------------
n = int(input("Enter n for natural numbers: "))
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")


# -------------------------------
# 2. Even numbers up to n
# -------------------------------
n = int(input("Enter n for even numbers: "))
for i in range(2, n + 1, 2):
    print(i, end=" ")
print("\n")


# -------------------------------
# 3. Odd numbers up to n
# -------------------------------
n = int(input("Enter n for odd numbers: "))
for i in range(1, n + 1, 2):
    print(i, end=" ")
print("\n")


# -------------------------------
# 4. Series: 1 2 4 8 16 ... (2^n)
# -------------------------------
n = int(input("Enter n for power series: "))
for i in range(n + 1):
    print(2 ** i, end=" ")
print("\n")


# -------------------------------
# 5. Sum of series:
# 1 + 1/1! + 1/2! + ... + 1/n!
# -------------------------------
n = int(input("Enter n for sum of series: "))
fact = 1
total = 1

for i in range(1, n + 1):
    fact *= i
    total += (1 / fact)
print("Sum =", total)

# -------------------------------
# 6. Cosine Series
# cos(x) = 1 – x^2/2! + x^4/4! – x^6/6! + ...
# -------------------------------
x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))

cos_x = 1
fact = 1
sign = -1

for i in range(2, 2*n, 2):
    fact *= i * (i - 1)   # calculate factorial stepwise
    term = (x ** i) / fact
    cos_x += sign * term
    sign *= -1

print("cos(x) =", cos_x)
print()


# -------------------------------
# 7. Check whether square root is prime
# -------------------------------
num = int(input("Enter a number: "))

sqrt_num = int(num ** 0.5)

# check prime
is_prime = True
if sqrt_num < 2:
    is_prime = False
else:
    for i in range(2, int(sqrt_num ** 0.5) + 1):
        if sqrt_num % i == 0:
            is_prime = False
            break

print("Square root =", sqrt_num)
if is_prime:
    print("Square root is PRIME")
else:
    print("Square root is NOT PRIME")
print()


# -------------------------------
# 8. Pattern Design
# A B C
# A B C
# A B C
# -------------------------------
rows = 3

for i in range(rows):
    for ch in ['A', 'B', 'C']:
        print(ch, end=" ")
    print()
# -------------------------------
# 9. Pattern:
# A
# A B
# A B C
# A B C D
# A B C D E
# -------------------------------
n = int(input("Enter n for pattern 9: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# -------------------------------
# 10. Pattern:
# A B C D E
# A B C D
# A B C
# A B
# A
# -------------------------------
n = int(input("Enter n for pattern 10: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
# -------------------------------
# 11. Pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# -------------------------------
n = int(input("Enter n for pattern 11: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# -------------------------------
# 12. Pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# -------------------------------
n = int(input("Enter n for pattern 12: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()    
