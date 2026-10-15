import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x450")
root.configure(bg="#EAF2F8")

# Heading
tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 16, "bold"),
    bg="#154360",
    fg="white",
    pady=12
).pack(fill="x")

# Roll Number
tk.Label(root, text="Roll Number:",
         font=("Arial", 11, "bold"),
         bg="#EAF2F8", fg="#154360").pack(pady=(15, 3))

roll = tk.Entry(root, font=("Arial", 11),
                bg="white", fg="black",
                relief="solid", bd=1)
roll.pack()

# Name
tk.Label(root, text="Name:",
         font=("Arial", 11, "bold"),
         bg="#EAF2F8", fg="#154360").pack(pady=(12, 3))

name = tk.Entry(root, font=("Arial", 11),
                bg="white", fg="black",
                relief="solid", bd=1)
name.pack()

# Subjects
tk.Label(root, text="Select Subjects:",
         font=("Arial", 11, "bold"),
         bg="#EAF2F8", fg="#154360").pack(pady=10)

s1 = tk.IntVar()
s2 = tk.IntVar()
s3 = tk.IntVar()
s4 = tk.IntVar()

subjects = [
    ("Python", s1),
    ("Java", s2),
    ("DBMS", s3),
    ("Mathematics", s4)
]

for subject, var in subjects:
    tk.Checkbutton(
        root,
        text=subject,
        variable=var,
        font=("Arial", 10),
        bg="#EAF2F8",
        fg="#1B2631",
        activebackground="#D4E6F1",
        selectcolor="#AED6F1"
    ).pack(anchor="center")

# Submit function
def submit():
    r = roll.get().strip()
    n = name.get().strip()

    if not r or not n:
        messagebox.showwarning(
            "Warning", "Please enter roll number and name."
        )
        return

    selected = [
        subject for subject, var in subjects if var.get()
    ]

    messagebox.showinfo(
        "Student Details",
        f"Roll Number: {r}\n"
        f"Name: {n}\n"
        f"Subjects: {', '.join(selected) if selected else 'None'}"
    )

# Submit button
tk.Button(
    root,
    text="SUBMIT",
    command=submit,
    font=("Arial", 11, "bold"),
    bg="#148F77",
    fg="white",
    activebackground="#0E6655",
    activeforeground="white",
    padx=25,
    pady=6,
    relief="flat",
    cursor="hand2"
).pack(pady=18)

root.mainloop()
