import pandas as pd
df = pd.read_csv("employees.csv")
salary = float(input("Enter salary: "))
result = df[df["Salary"] > salary]
print("\nEmployees earning above", salary)
print(result)

