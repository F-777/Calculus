import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) != 0:
            result.set(float(entry1.get()) / float(entry2.get()))
        else:
            messagebox.showerror("Error", "Division by zero is not allowed")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

app = tk.Tk()
app.title("Simple Calculator")

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

result = tk.StringVar()
result.set("Result")

label_result = tk.Label(app, textvariable=result)
label_result.grid(row=2, column=1)

tk.Label(app, text="First Number").grid(row=0)
tk.Label(app, text="Second Number").grid(row=1)

tk.Button(app, text='Add', command=add).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(app, text='Subtract', command=subtract).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(app, text='Multiply', command=multiply).grid(row=3, column=2, sticky=tk.W, pady=4)
tk.Button(app, text='Divide', command=divide).grid(row=3, column=3, sticky=tk.W, pady=4)

app.mainloop()
