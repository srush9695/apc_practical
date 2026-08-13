#1.Write a Python program to create a tuple of five integers and display it.
t=(1,2,3,4,5)
print(t)
#2.	Create a tuple containing five city names. Display:
#•	First city 
#•	Last city 
#•	Third city
t=("pune","mumbai","solapur","Kolhapur","Sangli")
print("First City:",t[0])
print("Last City:",t[4])
print("Third City:",t[2])
#3.Create a tuple of student names and display the total number of students using the len() function.
s=("srushti","anagha","adarsha","samruddhi","rajvardhan")
print("length:",len(s))
#4.Create a tuple of colors. Check whether a given color exists in the tuple.
c=("pink","black","red","blue")
if "pink" in c:
   print("Pink is exist")
else:
    print("pink is not exist")
#5.Create a tuple of fruits and display each fruit using a loop.
f=("apple","banana","orange","guava","mango")
for i in f:
    print("Fruit:",i)
#6Create a tuple with repeated numbers and count how many times a particular number appears.
t1=(1,2,2,4,4,5,6,7,7,6)
print("number of 4's:",t1.count(4))
#7.Create a tuple of employee IDs and find the index of a given ID.
e=("e1","e2","e3","e4","e5","e6")
print("index of emp 5:",e.index("e5"))
#8.Create two tuples of numbers and concatenate them into a single tuple.
tup1=(1,2,3,4,5)
tup2=(6,7,8,9)
tup=tup1+tup2
print("concatenate tuple :",tup)
#9.Create a tuple containing three elements and repeat it four times.
tu=(1,2,3)*3
print("Tuple:",tu)
#10.	Create a tuple of 10 numbers and display:
	First five elements 
	Last five elements 
	Middle four elements 
	Alternate elements 
	Reverse tuple
tupp=(1,2,3,4,5,6,7,8,9,10)
print("First five:",tupp[:6])
print("Last Five:",tupp[5:])
print("middle four element:",tupp[3:7])
print("Alternate elements:",tupp[::2])
print("Reverse Tuple:",tupp[::-1])
#11.Convert a tuple into a list and add a new element.
tp=(1,2,3,4,5)
l=list(tp)
l.append(6)
print("After adding element:",l,tuple(l))
#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple
li=[]
for i in range(5):
    li.append(int(input("Enter a number")))
tc=tuple(li)
print("Tuple:",tc)
#13.Modify a tuple by converting it into a list and then back into a tuple.
tm=(1,2,3,4,5,6,7)
lm=list(tm)
lm.append(8)
lm.insert(1,9)
lm.remove(5)
lm.pop(3)
tm=tuple(lm)
print("Tuple after modifying:",tm)
#14.Create a tuple and delete it completely.
td=(1,2,3,4,5)
print("Tuple:",td)
del td
#15.Create a nested tuple containing student details and display each record.
tn=(("srushti",1),("Samruddhi",2))
for i in tn:
    print(i[0],i[1])
#16.Store ten numbers in a tuple and calculate their sum.
s=0
ts=(1,2,3,4,5,6,7,8,9,10)
for i in ts:
    s+=i
print("sum:",s)    
#17.Find the largest and smallest number in a tuple without using max() and min().
t=(1,2,3,4,5,6,7,8)
la=t[0]
sm=t[0]
for i in t:
    if la<i:
        la=i
    if sm>i:
        sm=i
print("Largest:",la)
print("Smallest:",sm)
#18.Calculate the average of elements stored in a tuple.
ta=(1,2,3,4,5,6,7,8,9)
avg=sum(ta)/len(ta)
print("Average:",avg)
#19.	Store 15 integers in a tuple and count:

•	Even numbers 
•	Odd numbers
te=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
e=0
o=0
for i in te:
    if i%2==0:
        e+=1
    else:
        o+=1
print("even numbers:",e)
print("odd numbers:",o)
#20.Accept a number from the user and determine whether it exists in the tuple.
tu=(1,2,3,4,5,6)
n=int(input("Enter a number"))
if n in tu:
    print("Number exist")
else:
    print("NUmber not exists")
#21.	Store student details in a tuple:
•	Roll Number 
•	Name 
•	Department 
•	Marks 
Display all the details.
ts=(1,"srushti","CSE",95)
for i in ts:
    print(i)
#22.	Create tuples containing:
•	Employee ID 
•	Name 
•	Salary 
Display all employee information.
tmp=(1,"srushti",100000)
print("Employee Id:",tmp[0])
print("Employee Name:",tmp[1])
print("Employee salary:",tmp[2])
#23.	Store item prices in a tuple and calculate:
•	Total bill 
•	Average price 
•	Highest-priced item 
•	Lowest-priced item

titem=(45,69,78,100,34,90,50)
print("Total bill:",sum(titem))
print("Average Price:",sum(titem)/len(titem))
print("Highest-priced item:",max(titem))
print("Lowest-priced item:",min(titem))
#24.	Store temperatures of seven days in a tuple and determine:
•	Maximum temperature 
•	Minimum temperature 
•	Average temperature 
temp=(34,23,32,21,46,33,31)
print("Maximum Temp:",max(temp))
print("Minimum Temp:",min(temp))
print("Average Temp:",sum(temp)/len(temp))
#25.	Store runs scored in 10 matches and calculate:
•	Total runs 
•	Highest score 
•	Lowest score 
•	Average score

runs = (45, 60, 30, 80, 55, 70, 40, 90, 65, 50)

print("\nTotal runs:", sum(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", sum(runs) / len(runs))
#26.Create two tuples and find the common elements between them.
tc1=(1,2,3,4,5)
tc2=(3,4,6,7,8,9)
comm=()
for i in tc1:
    if i in tc2:
        comm+=(i,)
print(comm)
#27.Merge two tuples and remove duplicate elements.
# Merge two tuples and remove duplicate elements.
merged_tuple = tuple_a + tuple_b

unique_tuple = tuple(set(merged_tuple))

print("\nTuple after removing duplicates:", unique_tuple)

# Count the frequency of each element in a tuple.
frequency_tuple = (1, 2, 1, 3, 2, 4, 1)

print("\nFrequency of each element:")

for item in set(frequency_tuple):
    print(item, ":", frequency_tuple.count(item))

# Convert a tuple into a sorted tuple in ascending and descending order.
sort_tuple = (8, 2, 5, 1, 9, 4)

ascending = tuple(sorted(sort_tuple))
descending = tuple(sorted(sort_tuple, reverse=True))

print("\nAscending order:", ascending)
print("Descending order:", descending)

# Create a tuple containing patient records:
# Patient ID
# Name
# Age
# Blood Group
# Perform the following operations:
# Display all records
# Search for a patient by ID
# Count the total number of patients
# Display patients with a specific blood group
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Rahul", 30, "B+"),
    (103, "Priya", 28, "A+")
)

print("\nPatient records:")

for patient in patients:
    print(patient)

patient_id = int(input("\nEnter patient ID: "))

for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:", patient)

print("Total number of patients:", len(patients))

blood_group = input("Enter blood group: ")

print("Patients with the same blood group:")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)













