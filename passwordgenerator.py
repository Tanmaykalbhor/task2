import string
import random
import tkinter as tk


def generate_password():
    length = int(password_length.get())
    use_uppercase = include_uppercase.get()
    use_digits = include_digits.get()
    use_special_chars = include_special_chars.get()

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    password_characters = lowercase_chars
    if use_uppercase:
        password_characters += uppercase_chars
    if use_digits:
        password_characters += digits
    if use_special_chars:
        password_characters += special_chars

    password = ''.join(random.choice(password_characters) for i in range(length))
    generated_password.set(password)


root = tk.Tk()
root.title("Password Generator")

# Set a font
custom_font = ("Helvetica", 12)


password_length = tk.StringVar(value="12")
include_uppercase = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_special_chars = tk.BooleanVar(value=True)
generated_password = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0)

tk.Label(frame, text="Password Length:", font=custom_font).grid(row=0, column=0, sticky="W")
tk.Entry(frame, textvariable=password_length, width=5, font=custom_font).grid(row=0, column=1, sticky="W")

tk.Checkbutton(frame, text="Include uppercase letters", variable=include_uppercase, font=custom_font).grid(row=1, column=0, columnspan=2, sticky="W")
tk.Checkbutton(frame, text="Include digits", variable=include_digits, font=custom_font).grid(row=2, column=0, columnspan=2, sticky="W")
tk.Checkbutton(frame, text="Include special characters", variable=include_special_chars, font=custom_font).grid(row=3, column=0, columnspan=2, sticky="W")

button = tk.Button(frame, text="Generate Password", command=generate_password, font=custom_font, bg="#1E90FF", fg="white", padx=5, pady=5, relief="raised", activebackground="#104E8B")
button.grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Generated Password:", font=custom_font).grid(row=5, column=0, sticky="W")
tk.Entry(frame, textvariable=generated_password, state="readonly", width=30, font=custom_font).grid(row=5, column=1, sticky="W")

root.mainloop()