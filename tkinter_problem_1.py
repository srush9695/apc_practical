
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Management System")
root.geometry("1100x720")
root.configure(bg="#f1f5f9")

# Colors
NAVY = "#172554"
BLUE = "#2563eb"
WHITE = "#ffffff"
BG = "#f1f5f9"
GREEN = "#16a34a"
RED = "#dc2626"

students = []

# ================= HEADER =================
header = tk.Frame(root, bg=NAVY, height=85)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header, text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 23, "bold"),
    bg=NAVY, fg=WHITE
).pack(pady=(12, 2))

tk.Label(
    header, text="Manage student information easily",
    font=("Arial", 10),
    bg=NAVY, fg="#bfdbfe"
).pack()

# ================= MAIN AREA =================
main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=18, pady=15)

# Left form
form = tk.Frame(main, bg=WHITE, padx=20, pady=15)
form.pack(side="left", fill="y", padx=(0, 15))

tk.Label(
    form, text="Student Details",
    font=("Arial", 17, "bold"),
    bg=WHITE, fg=NAVY
).pack(anchor="w", pady=(0, 15))

def make_label(text):
    tk.Label(
        form, text=text,
        font=("Arial", 10, "bold"),
        bg=WHITE, fg="#334155"
    ).pack(anchor="w", pady=(7, 3))

make_label("Student ID")
id_entry = ttk.Entry(form, width=30)
id_entry.pack()

make_label("Full Name")
name_entry = ttk.Entry(form, width=30)
name_entry.pack()

make_label("Email Address")
email_entry = ttk.Entry(form, width=30)
email_entry.pack()

make_label("Gender")
gender = tk.StringVar(value="Female")

gender_frame = tk.Frame(form, bg=WHITE)
gender_frame.pack(anchor="w")

for value in ["Female", "Male", "Other"]:
    tk.Radiobutton(
        gender_frame, text=value,
        variable=gender, value=value,
        bg=WHITE
    ).pack(side="left")

make_label("Course")
course = ttk.Combobox(
    form, width=27, state="readonly",
    values=[
        "Computer Science",
        "Information Technology",
        "Mechanical",
        "Civil",
        "Electronics"
    ]
)
course.set("Computer Science")
course.pack()

make_label("Year of Study")
year = ttk.Combobox(
    form, width=27, state="readonly",
    values=["First Year", "Second Year",
            "Third Year", "Final Year"]
)
year.set("First Year")
year.pack()

make_label("Skills")
python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
sql_var = tk.BooleanVar()

skill_frame = tk.Frame(form, bg=WHITE)
skill_frame.pack(anchor="w")

tk.Checkbutton(
    skill_frame, text="Python",
    variable=python_var, bg=WHITE
).pack(side="left")

tk.Checkbutton(
    skill_frame, text="Java",
    variable=java_var, bg=WHITE
).pack(side="left")

tk.Checkbutton(
    skill_frame, text="SQL",
    variable=sql_var, bg=WHITE
).pack(side="left")

make_label("Attendance (%)")
attendance = tk.Spinbox(
    form, from_=0, to=100, width=8
)
attendance.pack(anchor="w")

# ================= RIGHT PANEL =================
right = tk.Frame(main, bg=BG)
right.pack(side="right", fill="both", expand=True)

# Search section
search_box = tk.Frame(right, bg=WHITE, padx=15, pady=13)
search_box.pack(fill="x", pady=(0, 12))

tk.Label(
    search_box, text="Search Student",
    font=("Arial", 12, "bold"),
    bg=WHITE, fg=NAVY
).pack(side="left", padx=(0, 10))

search_entry = ttk.Entry(search_box, width=25)
search_entry.pack(side="left", padx=5)

# Student table
table_box = tk.Frame(right, bg=WHITE, padx=12, pady=12)
table_box.pack(fill="both", expand=True)

tk.Label(
    table_box, text="Student Records",
    font=("Arial", 16, "bold"),
    bg=WHITE, fg=NAVY
).pack(anchor="w", pady=(0, 10))

columns = (
    "id", "name", "gender", "course",
    "year", "attendance"
)

table = ttk.Treeview(
    table_box, columns=columns,
    show="headings", height=12
)

headings = {
    "id": "Student ID",
    "name": "Name",
    "gender": "Gender",
    "course": "Course",
    "year": "Year",
    "attendance": "Attendance"
}

for col, heading in headings.items():
    table.heading(col, text=heading)
    table.column(col, width=100, anchor="center")

table.column("name", width=140)
table.column("course", width=140)

scrollbar = ttk.Scrollbar(
    table_box, orient="vertical",
    command=table.yview
)
table.configure(yscrollcommand=scrollbar.set)

table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ================= FUNCTIONS =================
def add_student():
    sid = id_entry.get().strip()
    name = name_entry.get().strip()
    email = email_entry.get().strip()

    if not sid or not name or not email:
        messagebox.showwarning(
            "Missing Details",
            "Please enter Student ID, Name and Email."
        )
        return

    if any(student["id"] == sid for student in students):
        messagebox.showerror(
            "Duplicate ID", "Student ID already exists."
        )
        return

    try:
        att = int(attendance.get())
        if not 0 <= att <= 100:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Attendance",
            "Enter attendance between 0 and 100."
        )
        return

    skills = []
    if python_var.get():
        skills.append("Python")
    if java_var.get():
        skills.append("Java")
    if sql_var.get():
        skills.append("SQL")

    student = {
        "id": sid,
        "name": name,
        "email": email,
        "gender": gender.get(),
        "course": course.get(),
        "year": year.get(),
        "attendance": att,
        "skills": skills
    }

    students.append(student)
    refresh_table()

    messagebox.showinfo(
        "Success", "Student added successfully!"
    )
    clear_form()


def refresh_table(records=None):
    for item in table.get_children():
        table.delete(item)

    if records is None:
        records = students

    for s in records:
        table.insert(
            "", tk.END,
            values=(
                s["id"], s["name"], s["gender"],
                s["course"], s["year"],
                str(s["attendance"]) + "%"
            )
        )

    count_label.config(
        text=f"Total Students: {len(students)}"
    )


def clear_form():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender.set("Female")
    course.set("Computer Science")
    year.set("First Year")
    attendance.delete(0, tk.END)
    attendance.insert(0, "0")
    python_var.set(False)
    java_var.set(False)
    sql_var.set(False)


def delete_student():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Select Student", "Please select a student to delete."
        )
        return

    sid = str(table.item(selected[0], "values")[0])

    if messagebox.askyesno(
        "Confirm Delete",
        "Do you want to delete this student?"
    ):
        students[:] = [
            s for s in students if s["id"] != sid
        ]
        refresh_table()


def search_student():
    query = search_entry.get().strip().lower()

    results = [
        s for s in students
        if query in s["id"].lower()
        or query in s["name"].lower()
        or query in s["course"].lower()
    ]

    refresh_table(results)


def show_details():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Select Student", "Please select a student."
        )
        return

    sid = str(table.item(selected[0], "values")[0])
    student = next(
        s for s in students if s["id"] == sid
    )

    messagebox.showinfo(
        "Student Details",
        f"ID: {student['id']}\n"
        f"Name: {student['name']}\n"
        f"Email: {student['email']}\n"
        f"Gender: {student['gender']}\n"
        f"Course: {student['course']}\n"
        f"Year: {student['year']}\n"
        f"Attendance: {student['attendance']}%\n"
        f"Skills: {', '.join(student['skills']) or 'None'}"
    )


# ================= ACTION BUTTONS =================
button_frame = tk.Frame(right, bg=BG)
button_frame.pack(fill="x", pady=12)

def make_button(parent, text, command, color):
    return tk.Button(
        parent, text=text, command=command,
        bg=color, fg=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat", padx=13, pady=9,
        cursor="hand2"
    )

make_button(
    button_frame, "Search", search_student, BLUE
).pack(side="left", padx=(0, 7))

make_button(
    button_frame, "Show All",
    lambda: refresh_table(), NAVY
).pack(side="left", padx=7)

make_button(
    button_frame, "View Details",
    show_details, GREEN
).pack(side="left", padx=7)

make_button(
    button_frame, "Delete",
    delete_student, RED
).pack(side="left", padx=7)

make_button(
    form, " + Add Student",
    add_student, BLUE
).pack(fill="x", pady=(18, 7))

make_button(
    form, "Clear Form",
    clear_form, "#64748b"
).pack(fill="x")

# ================= FOOTER =================
footer = tk.Frame(root, bg="#dbeafe", padx=15, pady=9)
footer.pack(fill="x", side="bottom")

count_label = tk.Label(
    footer, text="Total Students: 0",
    bg="#dbeafe", fg=NAVY,
    font=("Arial", 10, "bold")
)
count_label.pack(side="left")

tk.Label(
    footer, text="Developed using Python Tkinter",
    bg="#dbeafe", fg=NAVY,
    font=("Arial", 10)
).pack(side="right")

# ================= STYLING =================
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview.Heading",
    background="#dbeafe",
    foreground=NAVY,
    font=("Arial", 10, "bold"),
    padding=8
)

style.configure(
    "Treeview",
    rowheight=30,
    font=("Arial", 10),
    background=WHITE,
    fieldbackground=WHITE
)

style.map(
    "Treeview",
    background=[("selected", BLUE)],
    foreground=[("selected", WHITE)]
)

root.mainloop()
