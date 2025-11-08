import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from datetime import datetime
import os
from file_manager import TodoFileManager
from config import APP_CONFIG

class EnhancedTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_CONFIG['window_title'])
        self.root.geometry(APP_CONFIG['window_size'])
        self.root.configure(bg=APP_CONFIG['theme']['bg_color'])
        
        # Initialize file manager
        self.file_manager = TodoFileManager(
            APP_CONFIG['data_file'], 
            APP_CONFIG['backup_file']
        )
        
        # Create menu bar
        self.create_menu()
        
        # Create the GUI
        self.create_widgets()
        
        # Load existing todos
        self.load_todos()
        
        # Update statistics
        self.update_statistics()
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Backup", command=self.create_backup)
        file_menu.add_command(label="Restore", command=self.restore_backup)
        file_menu.add_separator()
        file_menu.add_command(label="Export as TXT", command=lambda: self.export_todos('txt'))
        file_menu.add_command(label="Export as CSV", command=lambda: self.export_todos('csv'))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Search", command=self.search_todos)
        edit_menu.add_command(label="Clear All", command=self.clear_all)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Show Statistics", command=self.show_statistics)
        view_menu.add_command(label="Refresh", command=self.refresh_display)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg=APP_CONFIG['theme']['bg_color'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Title
        title_label = tk.Label(main_frame, text=APP_CONFIG['window_title'], 
                              font=(APP_CONFIG['theme']['font_family'], 18, "bold"), 
                              bg=APP_CONFIG['theme']['bg_color'], 
                              fg=APP_CONFIG['theme']['text_color'])
        title_label.pack(pady=(0, 10))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=APP_CONFIG['theme']['bg_color'])
        input_frame.pack(fill='x', pady=(0, 10))
        
        # Task entry
        self.task_entry = tk.Entry(input_frame, 
                                  font=(APP_CONFIG['theme']['font_family'], 
                                       APP_CONFIG['theme']['font_size']), 
                                  width=40)
        self.task_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        
        # Priority selection
        self.priority_var = tk.StringVar(value="Medium")
        priority_combo = ttk.Combobox(input_frame, textvariable=self.priority_var,
                                     values=APP_CONFIG['priorities'], 
                                     state="readonly", width=8)
        priority_combo.pack(side='left', padx=(0, 5))
        
        # Add button
        add_button = tk.Button(input_frame, text="Add Task", 
                              command=self.add_task,
                              bg=APP_CONFIG['theme']['primary_color'], 
                              fg='white', 
                              font=(APP_CONFIG['theme']['font_family'], 10, "bold"))
        add_button.pack(side='left')
        
        # Search frame
        search_frame = tk.Frame(main_frame, bg=APP_CONFIG['theme']['bg_color'])
        search_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(search_frame, text="Search:", 
                font=(APP_CONFIG['theme']['font_family'], 10), 
                bg=APP_CONFIG['theme']['bg_color']).pack(side='left')
        
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side='left', padx=(5, 5))
        self.search_entry.bind('<KeyRelease>', self.on_search)
        
        search_clear_btn = tk.Button(search_frame, text="Clear", 
                                    command=self.clear_search,
                                    bg=APP_CONFIG['theme']['warning_color'],
                                    fg='white', font=("Arial", 8))
        search_clear_btn.pack(side='left')
        
        # Statistics frame
        stats_frame = tk.Frame(main_frame, bg=APP_CONFIG['theme']['bg_color'])
        stats_frame.pack(fill='x', pady=(0, 10))
        
        self.stats_label = tk.Label(stats_frame, text="", 
                                   font=(APP_CONFIG['theme']['font_family'], 9),
                                   bg=APP_CONFIG['theme']['bg_color'])
        self.stats_label.pack()
        
        # Listbox frame
        list_frame = tk.Frame(main_frame, bg=APP_CONFIG['theme']['bg_color'])
        list_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        # Scrollbars
        v_scrollbar = tk.Scrollbar(list_frame, orient='vertical')
        v_scrollbar.pack(side='right', fill='y')
        
        h_scrollbar = tk.Scrollbar(list_frame, orient='horizontal')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Listbox for tasks
        self.task_listbox = tk.Listbox(list_frame, 
                                      yscrollcommand=v_scrollbar.set,
                                      xscrollcommand=h_scrollbar.set,
                                      font=(APP_CONFIG['theme']['font_family'], 10),
                                      selectmode='single',
                                      height=12)
        self.task_listbox.pack(fill='both', expand=True)
        
        v_scrollbar.config(command=self.task_listbox.yview)
        h_scrollbar.config(command=self.task_listbox.xview)
        
        # Double click to edit
        self.task_listbox.bind('<Double-1>', lambda event: self.edit_task())
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg=APP_CONFIG['theme']['bg_color'])
        button_frame.pack(fill='x', pady=(0, 10))
        
        # Left buttons
        left_buttons = tk.Frame(button_frame, bg=APP_CONFIG['theme']['bg_color'])
        left_buttons.pack(side='left')
        
        complete_button = tk.Button(left_buttons, text="Complete",
                                   command=self.complete_task,
                                   bg=APP_CONFIG['theme']['secondary_color'], 
                                   fg='white',
                                   font=(APP_CONFIG['theme']['font_family'], 9, "bold"))
        complete_button.pack(side='left', padx=(0, 5))
        
        edit_button = tk.Button(left_buttons, text="Edit",
                               command=self.edit_task,
                               bg=APP_CONFIG['theme']['warning_color'], 
                               fg='white',
                               font=(APP_CONFIG['theme']['font_family'], 9, "bold"))
        edit_button.pack(side='left', padx=(0, 5))
        
        delete_button = tk.Button(left_buttons, text="Delete",
                                 command=self.delete_task,
                                 bg=APP_CONFIG['theme']['danger_color'], 
                                 fg='white',
                                 font=(APP_CONFIG['theme']['font_family'], 9, "bold"))
        delete_button.pack(side='left')
        
        # Right buttons
        right_buttons = tk.Frame(button_frame, bg=APP_CONFIG['theme']['bg_color'])
        right_buttons.pack(side='right')
        
        clear_completed_button = tk.Button(right_buttons, text="Clear Completed",
                                          command=self.clear_completed,
                                          bg='#9E9E9E', fg='white',
                                          font=(APP_CONFIG['theme']['font_family'], 9, "bold"))
        clear_completed_button.pack()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             relief='sunken', anchor='w',
                             bg='#e0e0e0', 
                             font=(APP_CONFIG['theme']['font_family'], 8))
        status_bar.pack(side='bottom', fill='x')
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        priority = self.priority_var.get()
        
        if self.file_manager.add_todo(task_text, priority):
            self.task_entry.delete(0, tk.END)
            self.load_todos()
            self.update_statistics()
            self.status_var.set(f"Task added: {task_text}")
        else:
            messagebox.showerror("Error", "Failed to add task!")
    
    def load_todos(self):
        self.task_listbox.delete(0, tk.END)
        todos = self.file_manager.read_todos()
        
        for todo in todos:
            if todo['status'] == "Completed":
                display_text = f"✓ [{todo['priority']}] {todo['task']} ({todo['timestamp']})"
                self.task_listbox.insert(tk.END, display_text)
                index = self.task_listbox.size() - 1
                self.task_listbox.itemconfig(index, {'fg': APP_CONFIG['priority_colors']['Completed']})
            else:
                display_text = f"[{todo['priority']}] {todo['task']} ({todo['timestamp']})"
                self.task_listbox.insert(tk.END, display_text)
                index = self.task_listbox.size() - 1
                color = APP_CONFIG['priority_colors'].get(todo['priority'], 'black')
                self.task_listbox.itemconfig(index, {'fg': color})
    
    def complete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")
            return
        
        index = selection[0]
        if self.file_manager.update_todo_status(index, "Completed"):
            self.load_todos()
            self.update_statistics()
            self.status_var.set("Task marked as completed!")
        else:
            messagebox.showerror("Error", "Failed to update task!")
    
    def edit_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to edit!")
            return
        
        index = selection[0]
        todos = self.file_manager.read_todos()
        
        if index >= len(todos):
            return
        
        current_todo = todos[index]
        if current_todo['status'] == "Completed":
            messagebox.showwarning("Warning", "Cannot edit completed tasks!")
            return
        
        new_task = simpledialog.askstring("Edit Task", 
                                         "Edit task:", 
                                         initialvalue=current_todo['task'])
        if new_task and new_task.strip():
            if self.file_manager.update_todo_task(index, new_task.strip()):
                self.load_todos()
                self.status_var.set("Task updated!")
            else:
                messagebox.showerror("Error", "Failed to update task!")
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            index = selection[0]
            if self.file_manager.delete_todo(index):
                self.load_todos()
                self.update_statistics()
                self.status_var.set("Task deleted!")
            else:
                messagebox.showerror("Error", "Failed to delete task!")
    
    def clear_completed(self):
        if messagebox.askyesno("Confirm Clear", "Remove all completed tasks?"):
            if self.file_manager.clear_completed():
                self.load_todos()
                self.update_statistics()
                self.status_var.set("Completed tasks cleared!")
            else:
                messagebox.showerror("Error", "Failed to clear completed tasks!")
    
    def update_statistics(self):
        stats = self.file_manager.get_statistics()
        stats_text = (f"Total: {stats['total']} | "
                     f"Pending: {stats['pending']} | "
                     f"Completed: {stats['completed']} | "
                     f"High: {stats['high_priority']} | "
                     f"Medium: {stats['medium_priority']} | "
                     f"Low: {stats['low_priority']}")
        self.stats_label.config(text=stats_text)
    
    def search_todos(self):
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if search_term:
            self.search_entry.delete(0, tk.END)
            self.search_entry.insert(0, search_term)
            self.on_search()
    
    def on_search(self, event=None):
        search_term = self.search_entry.get().strip()
        if search_term:
            results = self.file_manager.search_todos(search_term)
            self.display_search_results(results)
        else:
            self.load_todos()
    
    def display_search_results(self, results):
        self.task_listbox.delete(0, tk.END)
        for todo in results:
            if todo['status'] == "Completed":
                display_text = f"✓ [{todo['priority']}] {todo['task']} ({todo['timestamp']})"
                self.task_listbox.insert(tk.END, display_text)
                index = self.task_listbox.size() - 1
                self.task_listbox.itemconfig(index, {'fg': APP_CONFIG['priority_colors']['Completed']})
            else:
                display_text = f"[{todo['priority']}] {todo['task']} ({todo['timestamp']})"
                self.task_listbox.insert(tk.END, display_text)
                index = self.task_listbox.size() - 1
                color = APP_CONFIG['priority_colors'].get(todo['priority'], 'black')
                self.task_listbox.itemconfig(index, {'fg': color})
    
    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.load_todos()
    
    def refresh_display(self):
        self.load_todos()
        self.update_statistics()
        self.status_var.set("Display refreshed!")
    
    def new_file(self):
        if messagebox.askyesno("New File", "This will clear all current todos. Continue?"):
            try:
                if os.path.exists(self.file_manager.data_file):
                    os.remove(self.file_manager.data_file)
                self.load_todos()
                self.update_statistics()
                self.status_var.set("New file created!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create new file: {str(e)}")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Open Todo File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.file_manager.data_file = file_path
            self.load_todos()
            self.update_statistics()
            self.status_var.set(f"Opened file: {os.path.basename(file_path)}")
    
    def create_backup(self):
        if self.file_manager.create_backup():
            messagebox.showinfo("Backup", "Backup created successfully!")
            self.status_var.set("Backup created!")
        else:
            messagebox.showerror("Error", "Failed to create backup!")
    
    def restore_backup(self):
        if messagebox.askyesno("Restore Backup", "This will replace current data. Continue?"):
            if self.file_manager.restore_backup():
                self.load_todos()
                self.update_statistics()
                messagebox.showinfo("Restore", "Backup restored successfully!")
                self.status_var.set("Backup restored!")
            else:
                messagebox.showerror("Error", "Failed to restore backup!")
    
    def export_todos(self, format_type):
        file_extension = format_type.lower()
        file_path = filedialog.asksaveasfilename(
            title=f"Export as {format_type.upper()}",
            defaultextension=f".{file_extension}",
            filetypes=[(f"{format_type.upper()} files", f"*.{file_extension}"), ("All files", "*.*")]
        )
        if file_path:
            if self.file_manager.export_todos(file_path, format_type):
                messagebox.showinfo("Export", f"Exported successfully to {file_path}")
                self.status_var.set(f"Exported to {os.path.basename(file_path)}")
            else:
                messagebox.showerror("Error", "Export failed!")
    
    def clear_all(self):
        if messagebox.askyesno("Clear All", "This will delete ALL todos. This cannot be undone. Continue?"):
            if self.new_file():
                self.status_var.set("All todos cleared!")
    
    def show_statistics(self):
        stats = self.file_manager.get_statistics()
        stats_text = f"""Todo Statistics:
        
Total Tasks: {stats['total']}
Pending Tasks: {stats['pending']}
Completed Tasks: {stats['completed']}

Priority Breakdown (Pending):
High Priority: {stats['high_priority']}
Medium Priority: {stats['medium_priority']}
Low Priority: {stats['low_priority']}

Completion Rate: {(stats['completed'] / stats['total'] * 100) if stats['total'] > 0 else 0:.1f}%"""
        
        messagebox.showinfo("Statistics", stats_text)
    
    def show_about(self):
        about_text = f"""Todo App v1.0

A simple and efficient task management application.

Features:
• Add, edit, and delete tasks
• Priority levels (High, Medium, Low)
• Task completion tracking
• Search functionality
• Export capabilities (TXT, CSV)
• Backup and restore
• Statistics and analytics

Tech Stack: Python + Tkinter
Data Storage: Text files

Created for learning purposes."""
        
        messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedTodoApp(root)
    root.mainloop()