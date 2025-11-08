#!/usr/bin/env python3
"""
Todo App Launcher
Simple script to run the Todo application
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

def check_requirements():
    """Check if all required modules are available"""
    required_modules = ['tkinter', 'datetime', 'csv', 'shutil']
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    return missing_modules

def main():
    """Main launcher function"""
    print("Starting Todo App...")
    
    # Check requirements
    missing = check_requirements()
    if missing:
        print(f"Missing required modules: {', '.join(missing)}")
        print("Please install the missing modules before running the app.")
        return False
    
    # Check if we can import our modules
    try:
        from enhanced_todo_app import EnhancedTodoApp
        print("Todo app modules loaded successfully.")
    except ImportError as e:
        print(f"Error importing Todo app modules: {e}")
        print("Make sure all files are in the same directory.")
        return False
    
    try:
        # Create and run the application
        root = tk.Tk()
        
        # Set window icon if available
        try:
            # You can add an icon file here if you have one
            # root.iconbitmap('icon.ico')
            pass
        except:
            pass
        
        # Create the app
        app = EnhancedTodoApp(root)
        
        print("Todo App started successfully!")
        print("Close the application window to exit.")
        
        # Start the GUI main loop
        root.mainloop()
        
        print("Todo App closed.")
        return True
        
    except Exception as e:
        error_msg = f"Error starting Todo App: {str(e)}"
        print(error_msg)
        
        # Try to show error in a messagebox if tkinter is available
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            messagebox.showerror("Todo App Error", error_msg)
        except:
            pass
        
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)