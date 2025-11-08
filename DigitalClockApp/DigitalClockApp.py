import tkinter as tk
from tkinter import ttk
from ClockApp import ClockApp
from StopwatchGUI import StopwatchGUI

class DigitalClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock & Stopwatch")
        self.root.geometry("650x650")
        self.root.resizable(False, False)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each tab
        self.clock_frame = ttk.Frame(self.notebook)
        self.stopwatch_frame = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.clock_frame, text="Clock")
        self.notebook.add(self.stopwatch_frame, text="Stopwatch")
        
        # Initialize tab applications
        self.clock_app = ClockApp(self.clock_frame)
        self.stopwatch_app = StopwatchGUI(self.stopwatch_frame)

def main():
    root = tk.Tk()
    app = DigitalClockApp(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()