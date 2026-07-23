import math
print("------no is zero or non zero------")
n=int(input("Enter number"))
if(n==0):
    print("Number is zero")
else:
    print("Number is non zero")
n1=int(input("Enter number1"))
n2=int(input("Enter number2"))
print("-----greatest of two numbers----")
if(n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater")

print("-----positive or negative-----")
p=int(input("Enter number"))
if(p>0):
    print("positive")
elif(p<0):
    print("negative")
print("-----character or consonant-----")
ch=input("enter character").lower()
if ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("character is vowel")
else:
    print("character is consonant")
print("-----student performance-----")
per=float(input("Enter student percentage"))
if(per>=90):
    print("Excellent Performance")
elif(per>=80):
    print("very good performance")
elif(per>=70):
    print("good performance")
elif(per>=60):
    print("average performance")
else:
    print("poor performance")
print("--largest of three numbers----")
l1=int(input("Enter number1"))
l2=int(input("Enter number2"))
l3=int(input("Enter number3"))
if(l1>l2):
    if(l1>l3):
        print("number1 is largest")
    else:
        print("number3 is largest")
else:
    if(l2>l3):
        print("number2 is largest")
    else:
        print("number3 is largest")
print("--smallest of three numbers----")
s1=int(input("Enter number1"))
s2=int(input("Enter number2"))
s3=int(input("Enter number3"))
if(s1<s2 and s1<s3):
        print("number1 is smallest")
elif(s2<s1 and s2<s3):
        print("number2 is smallest")
else:
        print("number3 is smallest")
print("--------number is even or odd-------")
b=int(input("Enter number"))
if(b%2==0):
    print("Number is even")
else:
    print("Number is odd")
print("-----a year for leap year-----")
y=int(input("Enter a year"))
if y % 4 == 0:
    
    if y % 100 == 0:
        if y % 400 == 0:
            
            print("Leap year") 
        else:
            print("Not a leap year")  
    else:
        print("Leap year") 
else:
    print("Not a leap year")
print("company insurance")
m=input("married?")
a=int(input("Enter age"))
g=input("Enter Gender")
if m=="yes":
    print("driver is issured")
elif (m=="no" and a>30) and g="male":
    print("driver is issured")
elif (m=="no" and a>25) and g="female":
    print("driver is issured")
else:
    print("driver is not issured")
print("-----area of traingle-----")
ba=float(input("Enter base"))
h=float(input("Enter base"))
area=0.5*ba*h
print("Area of Traingle",area)
print("volume of sphere")
r=float(input("Enter Radius"))
vs=(4/3)*math.pi*(r**3)
print("Volume of sphere=",vs)
print("Total Surface Area Cylinder")
ra=float(input("Enter Radius"))
hc=float(input("Enter Height"))
t=2*math.pi*ra(ra+h)
print("Total Surface Area Of Cylinder=",t)
print("area of square")
side=float(input("Enter Side"))
area=side*side
print("Area of Square=",area)
print("pounds to kg")
po=int(input("Enter pounds"))
kg=po*0.45359237
print("Kilograms",kg)
print("km into miles")
km=float(input("Enter kilometers"))
mile=km%1.609344
print("mile=",mile)
print("Fact of num")
f=int(input("Enter Number"))
fact=1
for i in range(1,f+1):
    fact*=i
print("Factorial=",fact)    
print("prime ")
num=int(input("Enter number"))
flag=0
for i in range(2,num/2):
    if num%i==0:
        flag=1
        break
if f==1:
    print("not prime")
else:
    print("prime")
print("palindrome")
nm=int(input("Enter Number"))
org=nm
rev=0
while nm!=0:
    d=nm%10
    rev=(rev*10)+d
    nm/=10
if(org==rev):
    print("palindrome")
else:
    print("not palindrome")
print("decimal to binary")
nu= 7  # decimal number
res = ''  # binary result

while nu > 0:
    res = str(nu % 2) + res
    nu //= 2
print(res)
print("decimal to octal")
decimal = 148
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")
print("dec to hex")
num = 255
hex_digits = "0123456789abcdef"
result = ""
while num > 0:
    result = hex_digits[num % 16] + result
    num //= 16
print(result)
print("factors of number")
num = int(input("Enter a number: "))
print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
print("ascii character")
ch = input("Enter a character: ")

for i in range(0, 128):   # ASCII range
    if chr(i) == ch:
        print("ASCII value of", ch, "is", i)
        break

























































    
