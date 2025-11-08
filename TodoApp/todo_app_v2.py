"""
Todo App V2 - Sticky Notes Design
Inspired by Microsoft Sticky Notes
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, font
from datetime import datetime
from file_manager import TodoFileManager
import random

class StickyNote(tk.Frame):
    """Individual sticky note widget"""
    
    COLORS = {
        'yellow': '#FFFF88',
        'blue': '#A0D8F1',
        'green': '#B4E7CE',
        'pink': '#F5B5FC',
        'purple': '#D6B8FF',
        'orange': '#FFD4A3'
    }
    
    def __init__(self, parent, todo_data, index, on_delete, on_update, on_complete):
        super().__init__(parent)
        
        self.todo_data = todo_data
        self.index = index
        self.on_delete = on_delete
        self.on_update = on_update
        self.on_complete = on_complete
        
        # Determine color based on priority or status
        if todo_data['status'] == 'Completed':
            bg_color = '#D0D0D0'  # Gray for completed
        else:
            priority_colors = {
                'High': 'pink',
                'Medium': 'yellow',
                'Low': 'green'
            }
            color_name = priority_colors.get(todo_data['priority'], 'blue')
            bg_color = self.COLORS[color_name]
        
        self.bg_color = bg_color
        self.configure(bg=bg_color, relief='raised', borderwidth=2)
        
        # Shadow effect
        self.configure(highlightbackground='#888888', highlightthickness=1)
        
        self.create_widgets()
        
        # Hover effects
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
    
    def create_widgets(self):
        # Header frame with priority and timestamp
        header_frame = tk.Frame(self, bg=self.bg_color)
        header_frame.pack(fill='x', padx=5, pady=(5, 2))
        
        # Priority badge
        priority_badge = tk.Label(
            header_frame,
            text=self.todo_data['priority'],
            bg=self.get_priority_badge_color(),
            fg='white',
            font=('Arial', 8, 'bold'),
            padx=6,
            pady=2,
            relief='flat'
        )
        priority_badge.pack(side='left')
        
        # Timestamp
        time_label = tk.Label(
            header_frame,
            text=self.format_timestamp(),
            bg=self.bg_color,
            fg='#555555',
            font=('Arial', 7)
        )
        time_label.pack(side='right')
        
        # Task text
        task_frame = tk.Frame(self, bg=self.bg_color)
        task_frame.pack(fill='both', expand=True, padx=8, pady=5)
        
        # Scrollable text area
        task_text = tk.Text(
            task_frame,
            wrap='word',
            height=4,
            width=25,
            bg=self.bg_color,
            fg='#000000',
            font=('Segoe UI', 10),
            relief='flat',
            cursor='hand2',
            highlightthickness=0,
            padx=5,
            pady=5
        )
        task_text.pack(fill='both', expand=True)
        task_text.insert('1.0', self.todo_data['task'])
        
        # Add strikethrough if completed
        if self.todo_data['status'] == 'Completed':
            task_text.tag_add('completed', '1.0', 'end')
            task_text.tag_config('completed', overstrike=True, foreground='#666666')
        
        task_text.config(state='disabled')
        
        # Double click to edit
        task_text.bind('<Double-Button-1>', lambda e: self.edit_task())
        
        # Action buttons frame
        action_frame = tk.Frame(self, bg=self.bg_color)
        action_frame.pack(fill='x', padx=5, pady=(0, 5))
        
        button_font = ('Segoe UI', 8)
        
        # Complete/Uncomplete button
        if self.todo_data['status'] == 'Completed':
            complete_btn = tk.Button(
                action_frame,
                text='↶ Undo',
                command=lambda: self.on_complete(self.index, 'Pending'),
                bg='#4CAF50',
                fg='white',
                font=button_font,
                relief='flat',
                cursor='hand2',
                padx=5,
                pady=2
            )
        else:
            complete_btn = tk.Button(
                action_frame,
                text='✓ Done',
                command=lambda: self.on_complete(self.index, 'Completed'),
                bg='#4CAF50',
                fg='white',
                font=button_font,
                relief='flat',
                cursor='hand2',
                padx=5,
                pady=2
            )
        complete_btn.pack(side='left', padx=2)
        
        # Edit button
        edit_btn = tk.Button(
            action_frame,
            text='✎ Edit',
            command=self.edit_task,
            bg='#2196F3',
            fg='white',
            font=button_font,
            relief='flat',
            cursor='hand2',
            padx=5,
            pady=2
        )
        edit_btn.pack(side='left', padx=2)
        
        # Delete button
        delete_btn = tk.Button(
            action_frame,
            text='🗑 Delete',
            command=lambda: self.on_delete(self.index),
            bg='#f44336',
            fg='white',
            font=button_font,
            relief='flat',
            cursor='hand2',
            padx=5,
            pady=2
        )
        delete_btn.pack(side='right', padx=2)
    
    def get_priority_badge_color(self):
        colors = {
            'High': '#E53935',
            'Medium': '#FB8C00',
            'Low': '#43A047'
        }
        return colors.get(self.todo_data['priority'], '#757575')
    
    def format_timestamp(self):
        try:
            dt = datetime.strptime(self.todo_data['timestamp'], "%Y-%m-%d %H:%M:%S")
            return dt.strftime("%b %d, %H:%M")
        except:
            return self.todo_data['timestamp'][:16]
    
    def edit_task(self):
        if self.todo_data['status'] == 'Completed':
            messagebox.showwarning("Warning", "Cannot edit completed tasks!")
            return
        
        new_task = simpledialog.askstring(
            "Edit Task",
            "Edit your task:",
            initialvalue=self.todo_data['task']
        )
        
        if new_task and new_task.strip():
            self.on_update(self.index, new_task.strip())
    
    def on_enter(self, event):
        self.configure(relief='groove', borderwidth=3)
    
    def on_leave(self, event):
        self.configure(relief='raised', borderwidth=2)


class TodoAppV2:
    """Main application with sticky notes interface"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Todo App - Sticky Notes")
        self.root.geometry("1000x700")
        self.root.configure(bg='#F5F5F5')
        
        # Initialize file manager
        self.file_manager = TodoFileManager()
        
        # Current filter
        self.current_filter = 'All'
        self.search_term = ''
        
        # Create UI
        self.create_menubar()
        self.create_header()
        self.create_toolbar()
        self.create_notes_area()
        self.create_statusbar()
        
        # Load todos
        self.refresh_notes()
    
    def create_menubar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📁 File", menu=file_menu)
        file_menu.add_command(label="New Note", command=self.show_add_dialog, accelerator="Ctrl+N")
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
        menubar.add_cascade(label="✎ Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear Completed", command=self.clear_completed)
        edit_menu.add_command(label="Clear All", command=self.clear_all)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="👁 View", menu=view_menu)
        view_menu.add_command(label="Show All", command=lambda: self.apply_filter('All'))
        view_menu.add_command(label="Show Pending", command=lambda: self.apply_filter('Pending'))
        view_menu.add_command(label="Show Completed", command=lambda: self.apply_filter('Completed'))
        view_menu.add_separator()
        view_menu.add_command(label="Statistics", command=self.show_statistics)
        view_menu.add_command(label="Refresh", command=self.refresh_notes)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="❓ Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.show_add_dialog())
        self.root.bind('<F5>', lambda e: self.refresh_notes())
    
    def create_header(self):
        header = tk.Frame(self.root, bg='#2196F3', height=80)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header,
            text="📝 My Sticky Notes",
            font=('Segoe UI', 24, 'bold'),
            bg='#2196F3',
            fg='white'
        )
        title_label.pack(pady=15)
    
    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg='#FFFFFF', height=60, relief='flat')
        toolbar.pack(fill='x', padx=10, pady=10)
        toolbar.pack_propagate(False)
        
        # Left side - Add button
        add_button = tk.Button(
            toolbar,
            text="➕ New Note",
            command=self.show_add_dialog,
            bg='#4CAF50',
            fg='white',
            font=('Segoe UI', 11, 'bold'),
            relief='flat',
            cursor='hand2',
            padx=20,
            pady=8
        )
        add_button.pack(side='left', padx=5)
        
        # Filter buttons
        tk.Label(toolbar, text="Filter:", bg='#FFFFFF', font=('Segoe UI', 10)).pack(side='left', padx=(20, 5))
        
        filter_frame = tk.Frame(toolbar, bg='#FFFFFF')
        filter_frame.pack(side='left')
        
        self.filter_var = tk.StringVar(value='All')
        
        filters = [('All', 'All'), ('Pending', 'Pending'), ('Completed', 'Completed')]
        for text, value in filters:
            btn = tk.Radiobutton(
                filter_frame,
                text=text,
                variable=self.filter_var,
                value=value,
                command=lambda v=value: self.apply_filter(v),
                bg='#FFFFFF',
                font=('Segoe UI', 9),
                selectcolor='#2196F3',
                cursor='hand2'
            )
            btn.pack(side='left', padx=3)
        
        # Search box
        search_frame = tk.Frame(toolbar, bg='#FFFFFF')
        search_frame.pack(side='right', padx=5)
        
        tk.Label(search_frame, text="🔍", bg='#FFFFFF', font=('Segoe UI', 12)).pack(side='left')
        
        self.search_entry = tk.Entry(
            search_frame,
            font=('Segoe UI', 10),
            width=25,
            relief='solid',
            borderwidth=1
        )
        self.search_entry.pack(side='left', padx=5)
        self.search_entry.bind('<KeyRelease>', self.on_search)
        
        search_clear = tk.Button(
            search_frame,
            text="✕",
            command=self.clear_search,
            bg='#f44336',
            fg='white',
            font=('Segoe UI', 9),
            relief='flat',
            cursor='hand2',
            width=3
        )
        search_clear.pack(side='left')
    
    def create_notes_area(self):
        # Container with scrollbar
        container = tk.Frame(self.root, bg='#F5F5F5')
        container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Canvas for scrolling
        self.canvas = tk.Canvas(container, bg='#F5F5F5', highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient='vertical', command=self.canvas.yview)
        
        # Frame to hold notes
        self.notes_frame = tk.Frame(self.canvas, bg='#F5F5F5')
        
        # Configure scrolling
        self.notes_frame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        )
        
        self.canvas.create_window((0, 0), window=self.notes_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        
        # Mouse wheel scrolling
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_statusbar(self):
        statusbar = tk.Frame(self.root, bg='#E0E0E0', height=30)
        statusbar.pack(side='bottom', fill='x')
        statusbar.pack_propagate(False)
        
        self.status_var = tk.StringVar(value='Ready')
        status_label = tk.Label(
            statusbar,
            textvariable=self.status_var,
            bg='#E0E0E0',
            fg='#333333',
            font=('Segoe UI', 9),
            anchor='w'
        )
        status_label.pack(side='left', padx=10)
        
        # Statistics on right
        self.stats_var = tk.StringVar()
        stats_label = tk.Label(
            statusbar,
            textvariable=self.stats_var,
            bg='#E0E0E0',
            fg='#555555',
            font=('Segoe UI', 9),
            anchor='e'
        )
        stats_label.pack(side='right', padx=10)
        
        self.update_stats_display()
    
    def show_add_dialog(self):
        # Custom dialog for adding tasks
        dialog = tk.Toplevel(self.root)
        dialog.title("New Sticky Note")
        dialog.geometry("400x300")
        dialog.configure(bg='#FFFF88')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Title
        tk.Label(
            dialog,
            text="Create New Note",
            font=('Segoe UI', 14, 'bold'),
            bg='#FFFF88'
        ).pack(pady=10)
        
        # Task entry
        tk.Label(dialog, text="What do you need to do?", bg='#FFFF88', font=('Segoe UI', 10)).pack(pady=5)
        
        task_text = tk.Text(
            dialog,
            height=6,
            width=40,
            font=('Segoe UI', 10),
            wrap='word',
            relief='solid',
            borderwidth=1
        )
        task_text.pack(padx=20, pady=5)
        task_text.focus()
        
        # Priority selection
        priority_frame = tk.Frame(dialog, bg='#FFFF88')
        priority_frame.pack(pady=10)
        
        tk.Label(priority_frame, text="Priority:", bg='#FFFF88', font=('Segoe UI', 10)).pack(side='left', padx=5)
        
        priority_var = tk.StringVar(value='Medium')
        for priority in ['High', 'Medium', 'Low']:
            rb = tk.Radiobutton(
                priority_frame,
                text=priority,
                variable=priority_var,
                value=priority,
                bg='#FFFF88',
                font=('Segoe UI', 9)
            )
            rb.pack(side='left', padx=5)
        
        # Buttons
        button_frame = tk.Frame(dialog, bg='#FFFF88')
        button_frame.pack(pady=10)
        
        def add_task():
            task = task_text.get('1.0', 'end-1c').strip()
            if not task:
                messagebox.showwarning("Warning", "Please enter a task!")
                return
            
            priority = priority_var.get()
            if self.file_manager.add_todo(task, priority):
                self.status_var.set(f"✓ Added: {task[:30]}...")
                self.refresh_notes()
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Failed to add task!")
        
        tk.Button(
            button_frame,
            text="✓ Add Note",
            command=add_task,
            bg='#4CAF50',
            fg='white',
            font=('Segoe UI', 10, 'bold'),
            relief='flat',
            cursor='hand2',
            padx=20,
            pady=5
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="✕ Cancel",
            command=dialog.destroy,
            bg='#f44336',
            fg='white',
            font=('Segoe UI', 10),
            relief='flat',
            cursor='hand2',
            padx=20,
            pady=5
        ).pack(side='left', padx=5)
        
        # Bind Enter to add
        task_text.bind('<Control-Return>', lambda e: add_task())
    
    def refresh_notes(self):
        # Clear existing notes
        for widget in self.notes_frame.winfo_children():
            widget.destroy()
        
        # Load todos
        todos = self.file_manager.read_todos()
        
        # Apply filter
        if self.current_filter != 'All':
            todos = [t for t in todos if t['status'] == self.current_filter]
        
        # Apply search
        if self.search_term:
            todos = [t for t in todos if self.search_term.lower() in t['task'].lower()]
        
        if not todos:
            # Show empty state
            empty_label = tk.Label(
                self.notes_frame,
                text="📝 No notes yet!\nClick '➕ New Note' to get started.",
                font=('Segoe UI', 14),
                bg='#F5F5F5',
                fg='#999999'
            )
            empty_label.pack(pady=50)
        else:
            # Create grid of sticky notes
            row = 0
            col = 0
            max_cols = 3
            
            for idx, todo in enumerate(todos):
                note = StickyNote(
                    self.notes_frame,
                    todo,
                    idx,
                    self.delete_note,
                    self.update_note,
                    self.complete_note
                )
                note.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
                
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
            
            # Configure grid weights
            for i in range(max_cols):
                self.notes_frame.grid_columnconfigure(i, weight=1, uniform='cols')
        
        self.update_stats_display()
        self.canvas.yview_moveto(0)  # Scroll to top
    
    def delete_note(self, index):
        if messagebox.askyesno("Confirm", "Delete this note?"):
            # Get actual index from filtered list
            todos = self.file_manager.read_todos()
            if self.current_filter != 'All':
                filtered = [t for t in todos if t['status'] == self.current_filter]
            else:
                filtered = todos
            
            if self.search_term:
                filtered = [t for t in filtered if self.search_term.lower() in t['task'].lower()]
            
            # Find the actual index in the full list
            actual_todo = filtered[index]
            actual_index = todos.index(actual_todo)
            
            if self.file_manager.delete_todo(actual_index):
                self.status_var.set("🗑 Note deleted")
                self.refresh_notes()
    
    def update_note(self, index, new_task):
        todos = self.file_manager.read_todos()
        if self.current_filter != 'All':
            filtered = [t for t in todos if t['status'] == self.current_filter]
        else:
            filtered = todos
        
        if self.search_term:
            filtered = [t for t in filtered if self.search_term.lower() in t['task'].lower()]
        
        actual_todo = filtered[index]
        actual_index = todos.index(actual_todo)
        
        if self.file_manager.update_todo_task(actual_index, new_task):
            self.status_var.set("✎ Note updated")
            self.refresh_notes()
    
    def complete_note(self, index, new_status):
        todos = self.file_manager.read_todos()
        if self.current_filter != 'All':
            filtered = [t for t in todos if t['status'] == self.current_filter]
        else:
            filtered = todos
        
        if self.search_term:
            filtered = [t for t in filtered if self.search_term.lower() in t['task'].lower()]
        
        actual_todo = filtered[index]
        actual_index = todos.index(actual_todo)
        
        if self.file_manager.update_todo_status(actual_index, new_status):
            status_msg = "✓ Completed" if new_status == 'Completed' else "↶ Reopened"
            self.status_var.set(status_msg)
            self.refresh_notes()
    
    def apply_filter(self, filter_type):
        self.current_filter = filter_type
        self.filter_var.set(filter_type)
        self.refresh_notes()
        self.status_var.set(f"Filter: {filter_type}")
    
    def on_search(self, event=None):
        self.search_term = self.search_entry.get().strip()
        self.refresh_notes()
    
    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.search_term = ''
        self.refresh_notes()
    
    def clear_completed(self):
        if messagebox.askyesno("Confirm", "Remove all completed notes?"):
            if self.file_manager.clear_completed():
                self.status_var.set("🗑 Completed notes cleared")
                self.refresh_notes()
    
    def clear_all(self):
        if messagebox.askyesno("Warning", "Delete ALL notes? This cannot be undone!"):
            todos = self.file_manager.read_todos()
            for i in range(len(todos) - 1, -1, -1):
                self.file_manager.delete_todo(i)
            self.status_var.set("🗑 All notes cleared")
            self.refresh_notes()
    
    def create_backup(self):
        if self.file_manager.create_backup():
            messagebox.showinfo("Success", "Backup created!")
            self.status_var.set("💾 Backup created")
    
    def restore_backup(self):
        if messagebox.askyesno("Confirm", "Restore from backup? Current data will be replaced."):
            if self.file_manager.restore_backup():
                self.refresh_notes()
                messagebox.showinfo("Success", "Backup restored!")
                self.status_var.set("↶ Backup restored")
    
    def export_todos(self, format_type):
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=f".{format_type}",
            filetypes=[(f"{format_type.upper()} files", f"*.{format_type}")]
        )
        if file_path:
            if self.file_manager.export_todos(file_path, format_type):
                messagebox.showinfo("Success", f"Exported to {file_path}")
                self.status_var.set(f"📤 Exported")
    
    def update_stats_display(self):
        stats = self.file_manager.get_statistics()
        stats_text = f"📊 Total: {stats['total']} | ⏳ Pending: {stats['pending']} | ✓ Done: {stats['completed']}"
        self.stats_var.set(stats_text)
    
    def show_statistics(self):
        stats = self.file_manager.get_statistics()
        completion_rate = (stats['completed'] / stats['total'] * 100) if stats['total'] > 0 else 0
        
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistics")
        stats_window.geometry("350x300")
        stats_window.configure(bg='#FFFFFF')
        stats_window.transient(self.root)
        
        tk.Label(
            stats_window,
            text="📊 Statistics",
            font=('Segoe UI', 16, 'bold'),
            bg='#FFFFFF'
        ).pack(pady=15)
        
        stats_frame = tk.Frame(stats_window, bg='#FFFFFF')
        stats_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        stats_data = [
            ("Total Notes:", stats['total']),
            ("Pending:", stats['pending']),
            ("Completed:", stats['completed']),
            ("", ""),
            ("High Priority:", stats['high_priority']),
            ("Medium Priority:", stats['medium_priority']),
            ("Low Priority:", stats['low_priority']),
            ("", ""),
            ("Completion Rate:", f"{completion_rate:.1f}%")
        ]
        
        for label, value in stats_data:
            if label:
                row = tk.Frame(stats_frame, bg='#FFFFFF')
                row.pack(fill='x', pady=3)
                
                tk.Label(row, text=label, font=('Segoe UI', 11), bg='#FFFFFF', anchor='w').pack(side='left')
                tk.Label(row, text=str(value), font=('Segoe UI', 11, 'bold'), bg='#FFFFFF', anchor='e').pack(side='right')
    
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        about_window.geometry("400x300")
        about_window.configure(bg='#2196F3')
        about_window.transient(self.root)
        
        tk.Label(
            about_window,
            text="📝",
            font=('Segoe UI', 48),
            bg='#2196F3',
            fg='white'
        ).pack(pady=20)
        
        tk.Label(
            about_window,
            text="Todo App V2",
            font=('Segoe UI', 18, 'bold'),
            bg='#2196F3',
            fg='white'
        ).pack()
        
        tk.Label(
            about_window,
            text="Sticky Notes Design",
            font=('Segoe UI', 12),
            bg='#2196F3',
            fg='white'
        ).pack(pady=5)
        
        tk.Label(
            about_window,
            text="\nInspired by Microsoft Sticky Notes\nBuilt with Python + Tkinter\n\nFeatures:\n• Beautiful sticky note interface\n• Priority-based color coding\n• Search and filter\n• Export and backup",
            font=('Segoe UI', 10),
            bg='#2196F3',
            fg='white',
            justify='center'
        ).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoAppV2(root)
    root.mainloop()
