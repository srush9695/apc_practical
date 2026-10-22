
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x550")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

# Heading
tk.Label(
    root, text="Feedback Form",
    font=("Arial", 23, "bold"),
    bg="#eaf2f8", fg="#1e3a5f"
).pack(pady=20)

# Name
tk.Label(root, text="Name:", bg="#eaf2f8",
         font=("Arial", 11)).pack(anchor="w", padx=35)

name = tk.Entry(root, width=35, font=("Arial", 11))
name.pack(pady=5)

# Email
tk.Label(root, text="Email:", bg="#eaf2f8",
         font=("Arial", 11)).pack(anchor="w", padx=35)

email = tk.Entry(root, width=35, font=("Arial", 11))
email.pack(pady=5)

# Rating
tk.Label(root, text="Rate Our Service:",
         bg="#eaf2f8", font=("Arial", 11)).pack(pady=8)

rating = tk.StringVar(value="Excellent")

for option in ["Excellent", "Good", "Average", "Poor"]:
    tk.Radiobutton(
        root, text=option,
        variable=rating, value=option,
        bg="#eaf2f8", font=("Arial", 10)
    ).pack(anchor="w", padx=45)

# Feedback
tk.Label(root, text="Your Feedback:",
         bg="#eaf2f8", font=("Arial", 11)).pack(
             anchor="w", padx=35, pady=(8, 0)
         )

feedback = tk.Text(root, width=35, height=5,
                   font=("Arial", 10))
feedback.pack(pady=7)

# Submit function
def submit():
    if not name.get().strip() or not email.get().strip():
        messagebox.showwarning(
            "Warning", "Please enter your name and email."
        )
        return

    if not feedback.get("1.0", tk.END).strip():
        messagebox.showwarning(
            "Warning", "Please enter your feedback."
        )
        return

    messagebox.showinfo(
        "Thank You",
        f"Thank you, {name.get()}!\n"
        f"Your rating: {rating.get()}\n"
        "Your feedback has been submitted."
    )

    name.delete(0, tk.END)
    email.delete(0, tk.END)
    feedback.delete("1.0", tk.END)
    rating.set("Excellent")

# Submit button
tk.Button(
    root, text="Submit Feedback",
    command=submit,
    bg="#2563eb", fg="white",
    font=("Arial", 12, "bold"),
    padx=15, pady=8, relief="flat"
).pack(pady=12)

root.mainloop()
