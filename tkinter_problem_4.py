
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x450")
root.configure(bg="#e8f0fe")

tk.Label(
    root, text="MY TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="#e8f0fe", fg="#1e3a8a"
).pack(pady=20)

entry = tk.Entry(root, font=("Arial", 13), width=25)
entry.pack(pady=10, ipady=5)

tasks = tk.Listbox(
    root, font=("Arial", 12),
    width=32, height=10,
    selectbackground="#2563eb"
)
tasks.pack(pady=10)

def add_task():
    task = entry.get().strip()

    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    selected = tasks.curselection()

    if selected:
        tasks.delete(selected[0])
    else:
        messagebox.showwarning(
            "Warning", "Select a task to delete!"
        )

tk.Button(
    root, text="Add Task",
    command=add_task,
    bg="#16a34a", fg="white",
    font=("Arial", 12, "bold"),
    width=15
).pack(pady=5)

tk.Button(
    root, text="Delete Task",
    command=delete_task,
    bg="#dc2626", fg="white",
    font=("Arial", 12, "bold"),
    width=15
).pack(pady=5)

root.mainloop()
