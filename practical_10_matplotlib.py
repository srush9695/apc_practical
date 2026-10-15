#1Write a Python program to display the sales of a shop over five days using a line graph.
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [100, 150, 120, 180, 200]

plt.plot(days, sales, marker='o')
plt.title("Daily Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
#2.Write a program to compare the marks obtained by five students using a bar chart.
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [85, 70, 90, 65, 80]
plt.bar(students,marks,color="skyblue")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

#3.Create a horizontal bar chart to represent the number of books read by five students.
import matplotlib.pyplot as plt
stud=["A","B","C","D","E"]
book=[1,3,5,6,7]
plt.barh(stud,book,color="pink")
plt.title("Books read by students")
plt.xlabel("Students")
plt.ylabel("No. of books")
plt.show()

#4.Write a program to display a family's monthly expenses as a pie chart.
import matplotlib.pyplot as plt
categories = ["Food", "Rent", "Travel", "Education", "Savings"]
expenses = [30, 35, 10, 15, 10]
plt.pie(expenses,labels=categories,autopct='1.1f%%',startangle=90)
plt.title("Monthly Expenses")
plt.show()

#5.Create a scatter plot to show the relationship between hours studied and marks obtained by students.
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 55, 65, 75, 90]
plt.scatter(hours,marks,color='red')
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

#6.Write a program to display the distribution of students' marks using a histogram.
import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 72, 75, 80, 82, 85,
         90, 92, 60, 68, 74, 78, 88, 95]
plt.hist(marks,bins=5,color='orange',edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

#7Compare the monthly sales of two products using a single line graph.
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
product_a = [100, 120, 140, 130, 160]
product_b = [90, 110, 125, 150, 170]
plt.plot(months,product_a,marker='o',label="Product A")
plt.plot(months,product_b,marker='s',label="Product B")
plt.title("Product Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()
#8. Display student marks using both a bar chart and a line graph in the same figure.
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [75, 85, 65, 90]

plt.subplot(1, 2, 1)
plt.bar(students, marks, color='blue')
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.subplot(1, 2, 2)
plt.plot(students, marks, marker='o', color='red')
plt.title("Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()
#9Create a box plot to analyze the distribution of marks obtained by students in an examination.
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 75, 80, 85, 95]

plt.boxplot(marks)
plt.title("Student Marks Distribution")
plt.ylabel("Marks")
plt.show()
#10.Display the monthly electricity consumption of a household using an area plot.
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
units = [120, 135, 110, 150, 170, 160]

plt.fill_between(months, units, color='lightgreen', alpha=0.7)
plt.plot(months, units, color='green', marker='o')

plt.title("Monthly Electricity Consumption")
plt.xlabel("Months")
plt.ylabel("Units Consumed")
plt.show()

#11.Write a Python program to plot a sine wave from 0 to 2π.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, color='blue')
plt.title("Sine Wave")
plt.xlabel("Angle (radians)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

#12.Write a program to plot both sine and cosine waves on the same graph.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x), label="Sine", color='blue')
plt.plot(x, np.cos(x), label="Cosine", color='red')

plt.title("Sine and Cosine Waves")
plt.xlabel("Angle (radians)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
#13.Create a bubble chart to represent the relationship between advertising expenditure and sales for five companies, where bubble size represents the company's market size.
import matplotlib.pyplot as plt

advertising = [10, 20, 30, 40, 50]
sales = [15, 25, 35, 45, 60]
market_size = [100, 200, 300, 400, 500]

plt.scatter(
    advertising, sales,
    s=market_size,
    alpha=0.5,
    color='coral',
    edgecolors='black'
)

plt.title("Advertising vs Sales")
plt.xlabel("Advertising Expenditure")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
#14Compare the distribution of marks for two classes using violin plots.
import matplotlib.pyplot as plt

class_a = [50, 55, 60, 65, 70, 72, 75, 80]
class_b = [45, 52, 58, 63, 68, 75, 85, 90]

plt.violinplot([class_a, class_b], showmeans=True)
plt.xticks([1, 2], ["Class A", "Class B"])
plt.title("Class Marks Distribution")
plt.ylabel("Marks")
plt.show()
#15.Display a set of numerical values using a stem plot.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 12, 20, 18, 25]

plt.stem(x, y)
plt.title("Stem Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

#16.Display average temperatures for five days along with the measurement uncertainty
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temp = [28, 30, 29, 32, 31]
error = [1, 2, 1, 1.5, 1]

plt.errorbar(days, temp, yerr=error,
             fmt="o-", capsize=5)
plt.title("Temperature with Error Bars")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.show()

#17.Compare sales of two products over four months.
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr"]
a = [100, 120, 150, 170]
b = [90, 130, 140, 180]

x = np.arange(len(months))
width = 0.35

plt.bar(x - width/2, a, width, label="Product A")
plt.bar(x + width/2, b, width, label="Product B")

plt.xticks(x, months)
plt.title("Product Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

#18.Show the total monthly sales of two products using a stacked bar chart.
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
a = [100, 120, 150, 170]
b = [50, 60, 70, 80]

plt.bar(months, a, label="Product A")
plt.bar(months, b, bottom=a, label="Product B")

plt.title("Stacked Sales Chart")
plt.xlabel("Months")
plt.ylabel("Total Sales")
plt.legend()
plt.show()
#19.Display changes in a bank account balance over five transactions using a step plot.
import matplotlib.pyplot as plt

transactions = [1, 2, 3, 4, 5]
balance = [1000, 1500, 1200, 1800, 1600]

plt.step(transactions, balance, where="mid")
plt.title("Bank Balance Changes")
plt.xlabel("Transaction")
plt.ylabel("Balance")
plt.grid(True)
plt.show()

#20 Display the marks of five students across four subjects using a heatmap.

import matplotlib.pyplot as plt
import numpy as np

marks = np.array([
    [80, 75, 90, 85],
    [65, 70, 75, 80],
    [90, 85, 95, 92],
    [70, 60, 65, 75],
    [85, 90, 80, 88]
])

plt.imshow(marks, cmap="YlOrRd", aspect="auto")
plt.colorbar(label="Marks")
plt.xticks(range(4), ["Maths", "Science", "English", "IT"])
plt.yticks(range(5), ["A", "B", "C", "D", "E"])
plt.title("Student Marks Heatmap")
plt.show()

#21.Plot the contour lines of the mathematical function z=x2+y2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

plt.contour(X, Y, Z, levels=15)
plt.colorbar(label="Z Value")
plt.title("Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#22.Represent the height, weight, and age of individuals using a three-dimensional scatter plot.
import matplotlib.pyplot as plt

height = [150, 160, 170, 180, 175]
weight = [50, 60, 65, 80, 72]
age = [18, 22, 25, 30, 28]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(height, weight, age, color="red")
ax.set_title("3D Scatter Plot")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
ax.set_zlabel("Age")
plt.show()

#23.Write a Python program to draw a 3D line showing the relationship between X, Y, and Z coordinates.
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
z = [3, 5, 2, 6, 4]

ax.plot(x, y, z, color='blue', marker='o')

ax.set_title("3D Line Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()

#24.Write a program to create a 3D surface plot for the mathematical function z=x2+y2
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title("3D Surface Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()

#25.Write a Python program to create a stem plot showing the values of a dataset at different points.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.stem(x, y)

plt.title("Stem Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

plt.show()

#26.Write a Python program to display the monthly sales of three products using a stack plot.
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]

product_A = [10, 15, 20, 25, 30]
product_B = [5, 10, 15, 20, 25]
product_C = [8, 12, 18, 22, 28]

plt.stackplot(
    months,
    product_A,
    product_B,
    product_C,
    labels=["Product A", "Product B", "Product C"],
    colors=["skyblue", "orange", "lightgreen"]
)

plt.title("Monthly Sales - Stack Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend(loc="upper left")

plt.show()




































































































































































































































































