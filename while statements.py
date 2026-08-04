# ---------- 1. Natural numbers ----------

n = int(input())
for i in range(1, n+1):
print(i)

# ---------- 2. Even numbers ----------

n = int(input())
for i in range(2, n+1, 2):
print(i)

# ---------- 3. Odd numbers ----------

n = int(input())
for i in range(1, n+1, 2):
print(i)

# ---------- 4. Sum of natural numbers ----------

n = int(input())
s = 0
for i in range(1, n+1):
s += i
print(s)

# ---------- 5. Sum of odd numbers ----------

n = int(input())
s = 0
for i in range(1, n+1, 2):
s += i
print(s)

# ---------- 6. Sum of even numbers ----------

n = int(input())
s = 0
for i in range(2, n+1, 2):
s += i
print(s)

# ---------- 7. Reverse natural numbers ----------

n = int(input())
for i in range(n, 0, -1):
print(i)

# ---------- 8. Fibonacci ----------

n = int(input())
a, b = 0, 1
for i in range(n):
print(a)
a, b = b, a+b

# ---------- 9. Factorial ----------

n = int(input())
fact = 1
for i in range(1, n+1):
fact *= i
print(fact)

# ---------- 10. Prime check ----------

n = int(input())
flag = 0
if n > 1:
for i in range(2, n):
if n % i == 0:
flag = 1
break
if flag == 0 and n > 1:
print("Prime")
else:
print("Not Prime")

# ---------- 11. Sum of digits ----------

n = int(input())
s = 0
while n > 0:
s += n % 10
n //= 10
print(s)

# ---------- 12. Palindrome ----------

n = int(input())
temp = n
rev = 0
while n > 0:
rev = rev*10 + n%10
n //= 10

if temp == rev:
print("Palindrome")
else:
print("Not Palindrome")

# ---------- 13. Reverse number ----------

n = int(input())
rev = 0
while n > 0:
rev = rev*10 + n%10
n //= 10
print(rev)

# ---------- 14. Multiplication table ----------

n = int(input())
for i in range(1, 11):
print(n * i)

# ---------- 15. Largest ----------

nums = list(map(int, input().split()))
print(max(nums))

# ---------- 16. Smallest ----------

nums = list(map(int, input().split()))
print(min(nums))
