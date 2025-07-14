import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select an operation")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Number 1
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Number 2
tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Operation choice
tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar()
operation_var.set("Add")  # default value

operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
