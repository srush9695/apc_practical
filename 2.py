n=int(input("Enter a number"))
original=n
rev=0
while n!=0:
    rem=n%10
    rev=(rev*10)+rem
    n//=10
if rev==original:
    print("Palindrome")
else:
   print(" Not Palindrome") 
