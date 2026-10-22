
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x530")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

# Heading
tk.Label(
    root, text="Student Registration",
    font=("Arial", 21, "bold"),
    bg="#eaf2f8", fg="#1e3a5f"
).pack(pady=20)

# Name
tk.Label(root, text="Full Name:", bg="#eaf2f8").pack()
name = tk.Entry(root, width=32)
name.pack(pady=6)

# Email
tk.Label(root, text="Email:", bg="#eaf2f8").pack()
email = tk.Entry(root, width=32)
email.pack(pady=6)

# Phone
tk.Label(root, text="Phone Number:", bg="#eaf2f8").pack()
phone = tk.Entry(root, width=32)
phone.pack(pady=6)

# Gender
tk.Label(root, text="Gender:", bg="#eaf2f8").pack(pady=5)

gender = tk.StringVar(value="Female")

frame = tk.Frame(root, bg="#eaf2f8")
frame.pack()

for g in ["Female", "Male", "Other"]:
    tk.Radiobutton(
        frame, text=g, variable=gender,
        value=g, bg="#eaf2f8"
    ).pack(side="left", padx=5)

# Course
tk.Label(root, text="Select Course:", bg="#eaf2f8").pack(pady=8)

course = ttk.Combobox(
    root,
    values=["BTech", "BCA", "BSc", "MCA", "MBA"],
    state="readonly", width=28
)
course.set("BTech")
course.pack()

# Submit
def register():
    n = name.get().strip()
    e = email.get().strip()
    p = phone.get().strip()

    if not n or not e or not p:
        messagebox.showwarning(
            "Warning", "Please fill all fields."
        )
        return

    messagebox.showinfo(
        "Registration Successful",
        f"Name: {n}\n"
        f"Email: {e}\n"
        f"Phone: {p}\n"
        f"Gender: {gender.get()}\n"
        f"Course: {course.get()}"
    )

    name.delete(0, tk.END)
    email.delete(0, tk.END)
    phone.delete(0, tk.END)

tk.Button(
    root, text="Register",
    command=register,
    bg="#2563eb", fg="white",
    font=("Arial", 12, "bold"),
    relief="flat", padx=25, pady=8
).pack(pady=25)

root.mainloop()
