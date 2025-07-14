import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold")).pack(pady=10)

        # Password length
        tk.Label(root, text="Length:", font=("Helvetica", 12)).pack()
        self.length_var = tk.IntVar(value=12)
        tk.Entry(root, textvariable=self.length_var, font=("Helvetica", 12), width=5).pack()

        # Options
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_upper).pack(anchor="w", padx=40)
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.include_lower).pack(anchor="w", padx=40)
        tk.Checkbutton(root, text="Include Numbers", variable=self.include_digits).pack(anchor="w", padx=40)
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols).pack(anchor="w", padx=40)

        # Generate button
        tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12)).pack(pady=10)

        # Output
        self.output = tk.Entry(root, font=("Helvetica", 14), justify="center")
        self.output.pack(pady=5, fill="x", padx=20)

        # Copy button
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4.")
            return

        chars = ""
        if self.include_upper.get():
            chars += string.ascii_uppercase
        if self.include_lower.get():
            chars += string.ascii_lowercase
        if self.include_digits.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("No Options", "Please select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.output.delete(0, tk.END)
        self.output.insert(0, password)

    def copy_to_clipboard(self):
        password = self.output.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
