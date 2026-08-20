#1.
s={1,2,3,4,5}
for i in s:
    print(i)
#2
l=[1,2,2,3,4,4,5,5]
s1=set(l)
print("Resulting set:",s1)
#3
f={"apple","banana","mango","guava","jamun"}
print(f)
f.add("orange")
f.add("jackfruit")
print(f)
#4
n={1,2,3,4,5}
n.remove(2)
#5
sn={"srushti","sam","raj","adarsha","anagha"}
n=input("Enter a name")
if n in s:
    print(n,"is present")
else:
    print(n,"is not present")
#6.
c={"mumbai","pune","kolhapur","nagpur","nashik"}
print("No of cities:",len(c))
#7
p={"c","c++","java","python","ruby"}
for i in p:
    print(i)
#8
l1=[1,2,2,3,4,4,5,5]
s2=set(l1)
print("Resulting set:",s2)
#9
si1={1,2,3,4}
si2={3,4,5,6}
print("Union:",si1.union(si2))
#10
sc1={1,2,3,4}
sc2={3,4,5,6}
print("Common elements:",sc1.intersection(sc2))
#11
sd1={1,2,3,4}
sd2={3,4,5,6}
print("Difference sd1 and sd2:",sd1.difference(sd2))
print("Difference sd2 and sd1:",sd2.difference(sd1))
#12
sd1={1,2,3,4}
sd2={3,4,5,6}
print("Difference sd1 and sd2:",sd1.symmetric_difference(sd2))
#13
ss1={1,2,3}
ss2={1,2,3,4,5,6,7}
if ss1.issubset(ss2):
    print("s1 is subset of s2")
else:
    print("s1 is not subset of s2")
#14
ss2={1,2,3}
ss1={1,2,3,4,5,6,7}
if ss1.issuperset(ss2):
    print("s1 is superset of s2")
else:
    print("s1 is not superset of s2")
#15
set1={1,2,3}
set2={4,5,6}
if set1.isdisjoint(set2):
    print("no common ele")
else:
    print("common elements")
#16
se1={1,2,3}
se2={1,2,3}
if se1==se2:
    print("equal")
else:
    print("not equal")
#17
student1 = {"Python", "Java", "DBMS", "Maths"}
student2 = {"Java", "Python", "Networking", "OS"}

common_subjects = student1.intersection(student2)
print("Subjects studied by both students:", common_subjects)
#18
se=input("Enter a sentence").split()
su=set(se)
print("unique words:",su)
for word in su:
    print(word)
#19
morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Neha", "Riya"}
print("prsent in both sessions:",morning.intersection(afternoon))
print("present only in the morning:",morning-afternoon)
print("present only in the afternoon :",afternoon - morning)
print("present in at least one session:",morning.union(afternoon))
#20,21
python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Neha", "Riya"}

both_courses = python_students.intersection(java_students)

only_python = python_students - java_students
only_java = java_students - python_students

only_one_course = python_students.symmetric_difference(java_students)

print(" Students in both courses:", both_courses)
print("Students only in Python:", only_python)
print("Students only in Java:", only_java)
print("Students in only one course:", only_one_course)
#22
employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "C++", "SQL", "JavaScript"}

common_skills = employee1.intersection(employee2)
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1.union(employee2)
print("\n22. Common Skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All Skills:", all_skills)
#23
available_books = {
    "Python Programming",
    "Java Programming",
    "Data Science",
    "Web Development"
}

requested_books = {
    "Python Programming",
    "Data Science",
    "Machine Learning"
}

available_requested = available_books.intersection(requested_books)

print("\n23. Requested Books:", requested_books)
print("Books Available:", available_requested)
#24
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

unique_visitors = day1.union(day2)
returning_visitors = day1.intersection(day2)
only_day1 = day1 - day2
only_day2 = day2 - day1

print("\n24. Unique Visitors:", unique_visitors)
print("Returning Visitors:", returning_visitors)
print("Visitors only on Day 1:", only_day1)
print("Visitors only on Day 2:", only_day2)
electronics = {"Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"}

accessories = {"Headphones", "Smartwatch", "Mouse", "Keyboard", "Charger"}

common_products = electronics.intersection(accessories)

print("Electronics Products:", electronics)
print("Accessories Products:", accessories)
print("Products belonging to both categories:", common_products)

#25
user1 = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
user2 = {"Sneha", "Priya", "Riya", "Karan", "Amit"}

mutual_friends = user1.intersection(user2)
unique_user1 = user1 - user2
unique_user2 = user2 - user1
total_unique_friends = user1.union(user2)

print("\n25. Mutual Friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total Unique Friends:", total_unique_friends)   























