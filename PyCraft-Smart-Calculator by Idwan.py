import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition (+)":
            result = num1 + num2

        elif operation == "Subtraction (-)":
            result = num1 - num2

        elif operation == "Multiplication (×)":
            result = num1 * num2

        elif operation == "Division (÷)":
            if num2 == 0:
                messagebox.showerror(
                    "Error",
                    "Cannot divide by zero."
                )
                return

            result = num1 / num2

        result_label.config(
            text=f"Result: {result}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )


# Main Window
window = tk.Tk()
window.title("PyCraft Smart Calculator")
window.geometry("450x500")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="PyCraft Smart Calculator",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=(30, 5))

subtitle_label = tk.Label(
    window,
    text="A simple calculator built with Python",
    font=("Arial", 10)
)

subtitle_label.pack(pady=(0, 25))

# First Number
label_num1 = tk.Label(
    window,
    text="First Number",
    font=("Arial", 11)
)

label_num1.pack()

entry_num1 = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center",
    width=25
)

entry_num1.pack(pady=(5, 15))

# Second Number
label_num2 = tk.Label(
    window,
    text="Second Number",
    font=("Arial", 11)
)

label_num2.pack()

entry_num2 = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center",
    width=25
)

entry_num2.pack(pady=(5, 15))

# Operation
operation_label = tk.Label(
    window,
    text="Choose Operation",
    font=("Arial", 11)
)

operation_label.pack()

operation_var = tk.StringVar(
    value="Addition (+)"
)

operations = [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (×)",
    "Division (÷)"
]

operation_menu = tk.OptionMenu(
    window,
    operation_var,
    *operations
)

operation_menu.config(
    font=("Arial", 11),
    width=20
)

operation_menu.pack(pady=(5, 20))

# Calculate Button
calculate_button = tk.Button(
    window,
    text="Calculate",
    command=calculate,
    font=("Arial", 12, "bold"),
    width=20,
    height=2
)

calculate_button.pack()

# Result
result_label = tk.Label(
    window,
    text="Result: -",
    font=("Arial", 18, "bold")
)

result_label.pack(pady=25)

# Footer
footer_label = tk.Label(
    window,
    text="Built with Python & Tkinter | Idwan",
    font=("Arial", 9)
)

footer_label.pack(side="bottom", pady=20)

window.mainloop()