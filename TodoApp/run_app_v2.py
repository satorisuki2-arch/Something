#!/usr/bin/env python3
"""
Todo App V2 Launcher - Sticky Notes Design
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

def main():
    """Launch the Todo App V2"""
    print("=" * 50)
    print("  📝 Todo App V2 - Sticky Notes Design")
    print("=" * 50)
    print()
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        return False
    
    print("✅ Python version OK")
    
    # Check if required files exist
    if not os.path.exists("todo_app_v2.py"):
        print("❌ todo_app_v2.py not found")
        return False
    
    if not os.path.exists("file_manager.py"):
        print("❌ file_manager.py not found")
        return False
    
    print("✅ Required files found")
    print()
    
    try:
        # Import and run the app
        from todo_app_v2 import TodoAppV2
        
        print("🚀 Starting Todo App V2...")
        print("   Close the window to exit")
        print()
        
        root = tk.Tk()
        app = TodoAppV2(root)
        root.mainloop()
        
        print()
        print("👋 Todo App V2 closed")
        return True
        
    except ImportError as e:
        error_msg = f"❌ Import error: {e}"
        print(error_msg)
        print("\n💡 Make sure all files are in the same directory")
        return False
    
    except Exception as e:
        error_msg = f"❌ Error starting app: {e}"
        print(error_msg)
        
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", error_msg)
        except:
            pass
        
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
