import tkinter as tk
from tkinter import messagebox, filedialog
import secrets
import string
import random

# Password Generator Function
def generate_password():
    length = int(length_var.get())

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    avoid_ambiguous = ambiguous_var.get()

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    ambiguous_chars = "0O1lI"

    # Build character set
    char_pool = ""
    if use_upper:
        char_pool += upper
    if use_lower:
        char_pool += lower
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    if avoid_ambiguous:
        char_pool = ''.join(c for c in char_pool if c not in ambiguous_chars)

    if not char_pool:
        messagebox.showerror("Error", "At least one character type must be selected!")
        return

    # Ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(secrets.choice(upper))
    if use_lower:
        password.append(secrets.choice(lower))
    if use_digits:
        password.append(secrets.choice(digits))
    if use_symbols:
        password.append(secrets.choice(symbols))

    # Fill remaining characters randomly
    password += [secrets.choice(char_pool) for _ in range(length - len(password))]

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    # Display password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, ''.join(password))

# Function to copy password
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Function to save password
def save_password():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "No password to save!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(password)
        messagebox.showinfo("Saved", "Password saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x500")
root.resizable(False, False)

# Title Label
tk.Label(root, text="🔐 Advanced Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Password Length
tk.Label(root, text="Password Length:", font=("Arial", 10)).pack()
length_var = tk.StringVar(value="16")
tk.Entry(root, textvariable=length_var, width=5, font=("Arial", 12)).pack()

# Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
ambiguous_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Symbols (!@#$...)", variable=symbols_var).pack()
tk.Checkbutton(root, text="Avoid Ambiguous Characters", variable=ambiguous_var).pack()

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

# Password Display Entry
password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)

# Buttons for Copy and Save
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Save to File", command=save_password).pack(pady=5)

# Run the GUI
root.mainloop()
