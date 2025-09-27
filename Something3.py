# import tkinter as tk

# root = tk.Tk()
# root.title("Something")

# def is_number(string):
#     for c in string:
#         if not c in "1234567890":
#             return False
#     return True

# def calculator():
#     n1 = number1.get()
#     n1 = str(n1)
#     if not is_number(n1):
#         Answer.config(text=f"Error, invalid number", fg="#f94449")
#     operation = operator.get()
#     operation = str(operation)
#     if operation in "1234567890":
#         Answer.config(text=f"Error, invalid operation", fg="#f94449")
#         return
#     else:
#         if not operation in ["+", "-", "*", "/"]:
#             Answer.config(text=f"Error, invalid operation", fg="#f94449")
#             return
#     n2 = number2.get()
#     n2 = str(n2)
#     if not is_number(n2):
#         Answer.config(text=f"Error, invalid number", fg="#f94449")
#     if n2 == "0":
#         if operation == "/":
#             Answer.config(text=f"Error, invalid equation", fg="#f94449")
#             return
#     equation = n1 + operation + n2 
#     Ans = eval(equation)
#     Answer.config(text=f"Answer = {Ans}", fg = "#FFFFFF")

# tk.Label(root, text="Enter a number:").pack(pady=5)

# number1 = tk.Entry(root, width=30)
# number1.pack(pady=5)

# tk.Label(root, text="Enter an operation:").pack(pady=5)

# operator = tk.Entry(root, width=30)
# operator.pack(pady=5)

# tk.Label(root, text="Enter a number:").pack(pady=5)

# number2 = tk.Entry(root, width=30)
# number2.pack(pady=5)

# calculate_button = tk.Button(root, text="Calculate", command=calculator)
# calculate_button.pack(pady=5)

# Answer = tk.Label(root, text="")
# Answer.pack(pady=10)

# exit_button = tk.Button(root, text = "Exit Application", command=root.quit)
# exit_button.pack(pady=20)

# Grid layout example
# tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
# tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)
# tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
# tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)
# tk.Button(root, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)

# Checkbutton example
# check_var = tk.BooleanVar()
# check = tk.Checkbutton(root, text="Subscribe to newsletter", variable=check_var)
# check.pack(pady=5)

# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Something")

# def click():
#     # while (True):
#         messagebox.showwarning(title='WARNING!',message='You have A VIRUS!!!!')

# button = tk.Button(root,command=click,text='click me')
# button.pack()

# root.mainloop()

import tkinter as tk

def on_click(char):
    """Function to be called when a number or operator button is clicked"""
    entry.insert(tk.END, char)

def calculate():
    """Function to be called when the '=' button is clicked"""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    """Function to be called when the 'C' button is clicked"""
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

# Create an entry widget to display the calculations
entry = tk.Entry(window, width=25, font=('Arial', 16), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons in the grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 12), command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 12), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 12), command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create the clear button separately
clear_button = tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 12), command=clear)
clear_button.grid(row=row_val, column=col_val, columnspan=4, sticky='we')


# Start the GUI event loop
window.mainloop()