import tkinter as tk
from tkinter import ttk
from ClockApp import ClockApp
from StopwatchGUI import StopwatchGUI
from ColorSchema import ColorSchema


# Create main window
root = tk.Tk()
root.title("Notebook Example")
root.geometry("400x300")

# Create Notebook widget
notebook = ttk.Notebook(root)

# Create frames for each tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add tabs to notebook
notebook.add(tab1, text="Clock")
notebook.add(tab2, text="Stopwatch")

# Pack the notebook
notebook.pack(expand=True, fill='both')

# Initialize entity
clock = ClockApp(tab1)
stopwatch = StopwatchGUI(tab2)

# root.mainloop()

print(ColorSchema.colors["background"])  # Example usage of ColorSchema