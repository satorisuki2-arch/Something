import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo App")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Data file path
        self.data_file = "todos.txt"
        
        # Create the GUI
        self.create_widgets()
        
        # Load existing todos
        self.load_todos()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="My ToDo App", 
                              font=("Arial", 20, "bold"), 
                              bg='#f0f0f0', fg='#333')
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')
        
        # Task entry
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=40)
        self.task_entry.pack(side='left', padx=(0, 10), fill='x', expand=True)
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        
        # Add button
        add_button = tk.Button(input_frame, text="Add Task", 
                              command=self.add_task,
                              bg='#4CAF50', fg='white', 
                              font=("Arial", 10, "bold"))
        add_button.pack(side='right')
        
        # Priority frame
        priority_frame = tk.Frame(self.root, bg='#f0f0f0')
        priority_frame.pack(pady=5, padx=20, fill='x')
        
        tk.Label(priority_frame, text="Priority:", 
                font=("Arial", 10), bg='#f0f0f0').pack(side='left')
        
        self.priority_var = tk.StringVar(value="Medium")
        priority_combo = ttk.Combobox(priority_frame, textvariable=self.priority_var,
                                     values=["High", "Medium", "Low"], 
                                     state="readonly", width=10)
        priority_combo.pack(side='left', padx=(5, 0))
        
        # Listbox frame
        list_frame = tk.Frame(self.root, bg='#f0f0f0')
        list_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Listbox for tasks
        self.task_listbox = tk.Listbox(list_frame, 
                                      yscrollcommand=scrollbar.set,
                                      font=("Arial", 10),
                                      selectmode='single',
                                      height=15)
        self.task_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10, padx=20, fill='x')
        
        # Complete button
        complete_button = tk.Button(button_frame, text="Mark Complete",
                                   command=self.complete_task,
                                   bg='#2196F3', fg='white',
                                   font=("Arial", 10, "bold"))
        complete_button.pack(side='left', padx=(0, 5))
        
        # Edit button
        edit_button = tk.Button(button_frame, text="Edit Task",
                               command=self.edit_task,
                               bg='#FF9800', fg='white',
                               font=("Arial", 10, "bold"))
        edit_button.pack(side='left', padx=(0, 5))
        
        # Delete button
        delete_button = tk.Button(button_frame, text="Delete Task",
                                 command=self.delete_task,
                                 bg='#f44336', fg='white',
                                 font=("Arial", 10, "bold"))
        delete_button.pack(side='left', padx=(0, 5))
        
        # Clear completed button
        clear_button = tk.Button(button_frame, text="Clear Completed",
                                command=self.clear_completed,
                                bg='#9E9E9E', fg='white',
                                font=("Arial", 10, "bold"))
        clear_button.pack(side='right')
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             relief='sunken', anchor='w',
                             bg='#e0e0e0', font=("Arial", 9))
        status_bar.pack(side='bottom', fill='x')
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        priority = self.priority_var.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create task string: TIMESTAMP|PRIORITY|STATUS|TASK
        task_line = f"{timestamp}|{priority}|Pending|{task_text}"
        
        # Add to listbox with color coding
        display_text = f"[{priority}] {task_text} ({timestamp})"
        self.task_listbox.insert(tk.END, display_text)
        
        # Color code by priority
        index = self.task_listbox.size() - 1
        if priority == "High":
            self.task_listbox.itemconfig(index, {'fg': 'red'})
        elif priority == "Medium":
            self.task_listbox.itemconfig(index, {'fg': 'orange'})
        else:
            self.task_listbox.itemconfig(index, {'fg': 'green'})
        
        # Save to file
        self.save_task(task_line)
        
        # Clear entry
        self.task_entry.delete(0, tk.END)
        self.status_var.set(f"Task added: {task_text}")
    
    def save_task(self, task_line):
        try:
            with open(self.data_file, 'a', encoding='utf-8') as file:
                file.write(task_line + '\n')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save task: {str(e)}")
    
    def load_todos(self):
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split('|', 3)
                    if len(parts) == 4:
                        timestamp, priority, status, task_text = parts
                        
                        if status == "Completed":
                            display_text = f"✓ [{priority}] {task_text} ({timestamp})"
                            self.task_listbox.insert(tk.END, display_text)
                            index = self.task_listbox.size() - 1
                            self.task_listbox.itemconfig(index, {'fg': 'gray'})
                        else:
                            display_text = f"[{priority}] {task_text} ({timestamp})"
                            self.task_listbox.insert(tk.END, display_text)
                            index = self.task_listbox.size() - 1
                            
                            if priority == "High":
                                self.task_listbox.itemconfig(index, {'fg': 'red'})
                            elif priority == "Medium":
                                self.task_listbox.itemconfig(index, {'fg': 'orange'})
                            else:
                                self.task_listbox.itemconfig(index, {'fg': 'green'})
                                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")
    
    def complete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")
            return
        
        index = selection[0]
        self.update_task_status(index, "Completed")
        
        # Update display
        current_text = self.task_listbox.get(index)
        if not current_text.startswith("✓"):
            new_text = "✓ " + current_text
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, new_text)
            self.task_listbox.itemconfig(index, {'fg': 'gray'})
            self.status_var.set("Task marked as completed!")
    
    def edit_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to edit!")
            return
        
        index = selection[0]
        current_text = self.task_listbox.get(index)
        
        # Extract task text from display format
        if current_text.startswith("✓"):
            return  # Don't edit completed tasks
        
        # Parse the current task text
        task_data = self.get_task_data_by_index(index)
        if not task_data:
            return
        
        new_task = simpledialog.askstring("Edit Task", 
                                         "Edit task:", 
                                         initialvalue=task_data['task'])
        if new_task and new_task.strip():
            task_data['task'] = new_task.strip()
            self.update_task_in_file(index, task_data)
            self.refresh_display()
            self.status_var.set("Task updated!")
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            index = selection[0]
            self.remove_task_from_file(index)
            self.task_listbox.delete(index)
            self.status_var.set("Task deleted!")
    
    def clear_completed(self):
        if messagebox.askyesno("Confirm Clear", "Remove all completed tasks?"):
            self.remove_completed_from_file()
            self.refresh_display()
            self.status_var.set("Completed tasks cleared!")
    
    def get_task_data_by_index(self, index):
        tasks = self.read_all_tasks()
        if 0 <= index < len(tasks):
            parts = tasks[index].split('|', 3)
            if len(parts) == 4:
                return {
                    'timestamp': parts[0],
                    'priority': parts[1],
                    'status': parts[2],
                    'task': parts[3]
                }
        return None
    
    def read_all_tasks(self):
        if not os.path.exists(self.data_file):
            return []
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        except:
            return []
    
    def update_task_status(self, index, new_status):
        tasks = self.read_all_tasks()
        if 0 <= index < len(tasks):
            parts = tasks[index].split('|', 3)
            if len(parts) == 4:
                parts[2] = new_status
                tasks[index] = '|'.join(parts)
                self.write_all_tasks(tasks)
    
    def update_task_in_file(self, index, task_data):
        tasks = self.read_all_tasks()
        if 0 <= index < len(tasks):
            new_line = f"{task_data['timestamp']}|{task_data['priority']}|{task_data['status']}|{task_data['task']}"
            tasks[index] = new_line
            self.write_all_tasks(tasks)
    
    def remove_task_from_file(self, index):
        tasks = self.read_all_tasks()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            self.write_all_tasks(tasks)
    
    def remove_completed_from_file(self):
        tasks = self.read_all_tasks()
        tasks = [task for task in tasks if not task.split('|')[2] == "Completed"]
        self.write_all_tasks(tasks)
    
    def write_all_tasks(self, tasks):
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                for task in tasks:
                    file.write(task + '\n')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")
    
    def refresh_display(self):
        self.task_listbox.delete(0, tk.END)
        self.load_todos()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()