
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("850x600")
root.configure(bg="#f1f5f9")

expenses = []

# Colors
NAVY = "#1e293b"
GREEN = "#059669"
WHITE = "#ffffff"
BG = "#f1f5f9"

# ---------- HEADER ----------
header = tk.Frame(root, bg=NAVY, pady=18)
header.pack(fill="x")

tk.Label(
    header,
    text="PERSONAL EXPENSE TRACKER",
    font=("Arial", 22, "bold"),
    bg=NAVY, fg=WHITE
).pack()

tk.Label(
    header,
    text="Track your daily spending easily",
    font=("Arial", 11),
    bg=NAVY, fg="#cbd5e1"
).pack(pady=5)

# ---------- INPUT FORM ----------
form = tk.Frame(root, bg=WHITE, padx=20, pady=15)
form.pack(fill="x", padx=20, pady=15)

tk.Label(
    form, text="Add New Expense",
    font=("Arial", 15, "bold"),
    bg=WHITE, fg=NAVY
).grid(row=0, column=0, columnspan=4,
       sticky="w", pady=(0, 12))

tk.Label(form, text="Expense Name", bg=WHITE).grid(
    row=1, column=0, sticky="w", padx=5
)

name_entry = ttk.Entry(form, width=22)
name_entry.grid(row=2, column=0, padx=5, pady=5)

tk.Label(form, text="Amount (₹)", bg=WHITE).grid(
    row=1, column=1, sticky="w", padx=5
)

amount_entry = ttk.Entry(form, width=18)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form, text="Category", bg=WHITE).grid(
    row=1, column=2, sticky="w", padx=5
)

category = ttk.Combobox(
    form,
    values=["Food", "Travel", "Shopping",
            "Education", "Bills", "Other"],
    state="readonly",
    width=17
)
category.set("Food")
category.grid(row=2, column=2, padx=5, pady=5)

tk.Label(form, text="Payment Method", bg=WHITE).grid(
    row=1, column=3, sticky="w", padx=5
)

payment = ttk.Combobox(
    form,
    values=["Cash", "UPI", "Card", "Net Banking"],
    state="readonly",
    width=16
)
payment.set("UPI")
payment.grid(row=2, column=3, padx=5, pady=5)

# ---------- EXPENSE TABLE ----------
table_frame = tk.Frame(root, bg=WHITE, padx=15, pady=15)
table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 12))

tk.Label(
    table_frame, text="Expense History",
    font=("Arial", 15, "bold"),
    bg=WHITE, fg=NAVY
).pack(anchor="w", pady=(0, 10))

columns = ("name", "amount", "category", "payment")

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=8
)

table.heading("name", text="Expense Name")
table.heading("amount", text="Amount (₹)")
table.heading("category", text="Category")
table.heading("payment", text="Payment Method")

table.column("name", width=200)
table.column("amount", width=130, anchor="center")
table.column("category", width=160, anchor="center")
table.column("payment", width=160, anchor="center")

table.pack(fill="both", expand=True)

# ---------- FUNCTIONS ----------
def update_total():
    total = sum(expense[1] for expense in expenses)
    total_label.config(text=f"Total Expenses: ₹{total:.2f}")


def add_expense():
    name = name_entry.get().strip()
    amount_text = amount_entry.get().strip()

    if not name or not amount_text:
        messagebox.showwarning(
            "Missing Details",
            "Please enter expense name and amount."
        )
        return

    try:
        amount = float(amount_text)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Amount",
            "Enter an amount greater than zero."
        )
        return

    expense = (
        name, amount, category.get(), payment.get()
    )
    expenses.append(expense)

    table.insert(
        "", tk.END,
        values=(
            name, f"₹{amount:.2f}",
            category.get(), payment.get()
        )
    )

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    update_total()


def delete_expense():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Selection Required",
            "Select an expense to delete."
        )
        return

    for item in selected:
        index = table.index(item)
        table.delete(item)
        expenses.pop(index)

    update_total()


def clear_form():
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category.set("Food")
    payment.set("UPI")


# ---------- BUTTONS ----------
buttons = tk.Frame(root, bg=BG)
buttons.pack(fill="x", padx=20, pady=(0, 10))

tk.Button(
    buttons, text=" + Add Expense",
    command=add_expense,
    bg=GREEN, fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat", padx=15, pady=8
).pack(side="left", padx=(0, 8))

tk.Button(
    buttons, text="Delete Selected",
    command=delete_expense,
    bg="#dc2626", fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat", padx=15, pady=8
).pack(side="left", padx=8)

tk.Button(
    buttons, text="Clear Form",
    command=clear_form,
    bg="#64748b", fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat", padx=15, pady=8
).pack(side="left", padx=8)

total_label = tk.Label(
    buttons,
    text="Total Expenses: ₹0.00",
    font=("Arial", 13, "bold"),
    bg=BG, fg=GREEN
)
total_label.pack(side="right")

# ---------- TABLE STYLE ----------
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview.Heading",
    background="#d1fae5",
    foreground=NAVY,
    font=("Arial", 10, "bold"),
    padding=8
)

style.configure(
    "Treeview",
    rowheight=28,
    font=("Arial", 10),
    background=WHITE,
    fieldbackground=WHITE
)

root.mainloop()
