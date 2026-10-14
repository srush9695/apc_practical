
import pandas as pd

# ============================================================
# 1. STUDENT MARKS USING DATAFRAME
# ============================================================
print("\n========== 1. STUDENT MARKS ==========")

students = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Python": [85, 70, 90, 65, 80],
    "DBMS": [80, 75, 88, 70, 85],
    "Maths": [90, 72, 92, 68, 78]
}

df = pd.DataFrame(students)
df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

print(df)
print("\nStudents with average above 75%:")
print(df[df["Average"] > 75])


# ============================================================
# 2. EMPLOYEE SALARY
# ============================================================
print("\n========== 2. EMPLOYEE SALARY ==========")

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [45000, 60000, 55000, 75000, 40000],
    "Experience": [2, 5, 7, 8, 3]
}

df = pd.DataFrame(employees)
print(df[df["Salary"] > 50000])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Employee with highest experience:")
print(df.loc[df["Experience"].idxmax()])


# ============================================================
# 3. PRODUCT TOTAL SALES
# ============================================================
print("\n========== 3. PRODUCT SALES ==========")

products = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories",
                 "Electronics", "Electronics"],
    "Price": [50000, 500, 1500, 12000, 8000],
    "Quantity": [3, 20, 10, 5, 4]
}

df = pd.DataFrame(products)
df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)
print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# ============================================================
# 4. PATIENT MEDICAL CHARGES
# ============================================================
print("\n========== 4. PATIENT CHARGES ==========")

patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Age": [65, 45, 72, 30, 61],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [60000, 15000, 90000, 25000, 55000]
}

df = pd.DataFrame(patients)

print("Patients above 60:")
print(df[df["Age"] > 60])
print("Average medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())
print("Patients with charges above 50000:")
print(df[df["Medical_Charges"] > 50000])


# ============================================================
# 5. ORDER DETAILS
# ============================================================
print("\n========== 5. ORDER DETAILS ==========")

orders = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Product": ["Laptop", "Mobile", "Book", "Tablet", "Monitor"],
    "Quantity": [1, 2, 5, 1, 2],
    "Price": [60000, 15000, 500, 20000, 12000],
    "Discount": [5000, 1000, 100, 2000, 500]
}

df = pd.DataFrame(orders)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:")
print(df)
print("Orders above 5000:")
print(df[df["Final_Amount"] > 5000])
print("Highest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("Average order value:", df["Final_Amount"].mean())


# ============================================================
# 6. STUDENT ATTENDANCE
# ============================================================
print("\n========== 6. STUDENT ATTENDANCE ==========")

attendance = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [80, 65, 90, 70, 75]
}

df = pd.DataFrame(attendance)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)
print("Students with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# ============================================================
# 7. RETAIL SHOP SALES
# ============================================================
print("\n========== 7. RETAIL SHOP SALES ==========")

retail = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories",
                 "Electronics", "Electronics"],
    "Price": [50000, 500, 1500, 12000, 8000],
    "Quantity": [3, 20, 10, 5, 4]
}

df = pd.DataFrame(retail)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
print("Sales above 10000:")
print(df[df["Total_Sales"] > 10000])
print("Product with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("Average sales:", df["Total_Sales"].mean())


# ============================================================
# 8. STUDENT MARKS USING SERIES
# ============================================================
print("\n========== 8. STUDENT MARKS SERIES ==========")

marks = pd.Series({
    "Amit": 85,
    "Priya": 90,
    "Rahul": 68,
    "Sneha": 78,
    "Neha": 95
})

print(marks)
print("Marks of Priya:", marks["Priya"])
print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Average marks:", marks.mean())
print("Students scoring above 75:")
print(marks[marks > 75])


# ============================================================
# 9. EMPLOYEE SALARY USING SERIES
# ============================================================
print("\n========== 9. EMPLOYEE SALARY SERIES ==========")

salary = pd.Series({
    "Amit": 45000,
    "Priya": 60000,
    "Rahul": 55000,
    "Sneha": 75000,
    "Neha": 40000
})

print(salary)
print("Highest salary:", salary.max())
print("Lowest salary:", salary.min())
print("Average salary:", salary.mean())
print("Employees earning above 50000:")
print(salary[salary > 50000])


# ============================================================
# 10. PRODUCT PRICES USING SERIES
# ============================================================
print("\n========== 10. PRODUCT PRICE SERIES ==========")

prices = pd.Series({
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8000
})

print("All products and prices:")
print(prices)

prices = prices * 1.10
print("Prices after 10% increase:")
print(prices)

print("Most expensive product:")
print(prices.idxmax(), prices.max())

print("Products costing above 1000:")
print(prices[prices > 1000])


# ============================================================
# 11. PATIENT AGES USING SERIES
# ============================================================
print("\n========== 11. PATIENT AGE SERIES ==========")

ages = pd.Series({
    101: 65,
    102: 45,
    103: 72,
    104: 30,
    105: 61
})

print("Average age:", ages.mean())
print("Oldest patient:", ages.idxmax(), ages.max())
print("Youngest patient:", ages.idxmin(), ages.min())
print("Patients above 60:")
print(ages[ages > 60])


# ============================================================
# 12. STUDENT ATTENDANCE USING SERIES
# ============================================================
print("\n========== 12. ATTENDANCE SERIES ==========")

att = pd.Series({
    "Amit": 80,
    "Priya": 95,
    "Rahul": 65,
    "Sneha": 92,
    "Neha": 70
})

print("Average attendance:", att.mean())
print("Attendance below 75%:")
print(att[att < 75])
print("Attendance above 90%:")
print(att[att > 90])
print("Highest attendance:", att.max())


# ============================================================
# 13. STUDENTS.CSV
# ============================================================
print("\n========== 13. STUDENTS CSV ==========")

try:
    df = pd.read_csv("students.csv")
    print("First 5 records:")
    print(df.head())
    print("Last 5 records:")
    print(df.tail())

    subjects = ["Python", "DBMS", "Maths"]
    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1)

    print("Total and average marks:")
    print(df)
    print("Students with average above 75:")
    print(df[df["Average"] > 75])
    print("Student with highest average:")
    print(df.loc[df["Average"].idxmax()])
    print("Subject-wise average:")
    print(df[subjects].mean())

except FileNotFoundError:
    print("students.csv file not found.")


# ============================================================
# 14. EMPLOYEES.CSV
# ============================================================
print("\n========== 14. EMPLOYEES CSV ==========")

try:
    df = pd.read_csv("employees.csv")

    print("Employees in CSE department:")
    print(df[df["Department"] == "CSE"])
    print("Average salary:", df["Salary"].mean())
    print("Highest salary:", df["Salary"].max())
    print("Lowest salary:", df["Salary"].min())
    print("Employees earning above 50000:")
    print(df[df["Salary"] > 50000])
    print("Department-wise average salary:")
    print(df.groupby("Department")["Salary"].mean())

except FileNotFoundError:
    print("employees.csv file not found.")


# ============================================================
# 15. PATIENTS.CSV
# ============================================================
print("\n========== 15. PATIENTS CSV ==========")

try:
    df = pd.read_csv("patients.csv")

    print("Patients above 60:")
    print(df[df["Age"] > 60])
    print("Average medical expense:", df["Medical_Expense"].mean())
    print("Patient with highest medical expense:")
    print(df.loc[df["Medical_Expense"].idxmax()])
    print("Disease-wise patient count:")
    print(df["Disease"].value_counts())
    print("Patients with expense above 50000:")
    print(df[df["Medical_Expense"] > 50000])

except FileNotFoundError:
    print("patients.csv file not found.")


# ============================================================
# 16. WEATHER.CSV
# ============================================================
print("\n========== 16. WEATHER CSV ==========")

try:
    df = pd.read_csv("weather.csv")

    print("Maximum temperature:", df["Temperature"].max())
    print("Minimum temperature:", df["Temperature"].min())
    print("Average temperature:", df["Temperature"].mean())
    print("Records with temperature above 35:")
    print(df[df["Temperature"] > 35])
    print("City-wise average temperature:")
    print(df.groupby("City")["Temperature"].mean())

except FileNotFoundError:
    print("weather.csv file not found.")
