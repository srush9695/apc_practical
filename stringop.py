# 1. String Length (without len)
s = input("Enter String: ")
c = 0
for i in s:
    c += 1
print("Length:", c)


# 2. Character Count
st = input("\nEnter String: ").lower()
v = c = d = sp = sc = 0
for i in st:
    if i.isalpha():
        if i in "aeiou":
            v += 1
        else:
            c += 1
    elif i.isdigit():
        d += 1
    elif i == " ":
        sp += 1
    else:
        sc += 1
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", sp)
print("Special Characters:", sc)


# 3. Reverse String
s = input("\nEnter String: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reverse:", rev)


# 4. Palindrome Check
s = input("\nEnter String: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 5. Uppercase & Lowercase Count
s = input("\nEnter String: ")
u = l = 0
for ch in s:
    if ch.islower():
        l += 1
    elif ch.isupper():
        u += 1
print("Uppercase:", u)
print("Lowercase:", l)


# 6. Replace Characters
s = input("\nEnter String: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("Result:", s.replace(old, new))


# 7. Remove Spaces
s = input("\nEnter String: ")
print("Without spaces:", s.replace(" ", ""))


# 8. Frequency of Character
s = input("\nEnter String: ")
ch = input("Enter character to count: ")
count = 0
for i in s:
    if i == ch:
        count += 1
print("Frequency:", count)


# 9. First and Last Character
s = input("\nEnter String: ")
print("First:", s[0])
print("Last:", s[-1])


# 10. ASCII Values
s = input("\nEnter String: ")
for ch in s:
    print(ch, ":", ord(ch))
