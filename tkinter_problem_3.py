
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")
root.configure(bg="#e8f0fe")
root.resizable(False, False)

# Display
display = tk.Entry(
    root, font=("Arial", 22),
    justify="right", bd=5
)
display.pack(fill="x", padx=15, pady=20, ipady=10)

# Button click function
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

frame = tk.Frame(root, bg="#e8f0fe")
frame.pack(expand=True, fill="both", padx=10, pady=5)

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        if value == "=":
            command = calculate
            color = "#16a34a"
        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: click(v)
            color = "#2563eb"
        else:
            command = lambda v=value: click(v)
            color = "#ffffff"

        tk.Button(
            frame, text=value,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white" if color != "#ffffff" else "#1e293b",
            command=command
        ).grid(
            row=r, column=c,
            sticky="nsew", padx=4, pady=4
        )

    frame.rowconfigure(r, weight=1)

for c in range(4):
    frame.columnconfigure(c, weight=1)

tk.Button(
    root, text="CLEAR",
    font=("Arial", 12, "bold"),
    bg="#dc2626", fg="white",
    command=clear
).pack(fill="x", padx=15, pady=10)

root.mainloop()
