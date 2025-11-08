import os
import shutil
from datetime import datetime
from typing import List, Dict, Optional

class TodoFileManager:
    """Handles all file operations for the Todo app"""
    
    def __init__(self, data_file: str = "todos.txt", backup_file: str = "todos_backup.txt"):
        self.data_file = data_file
        self.backup_file = backup_file
    
    def create_backup(self) -> bool:
        """Create a backup of the current todo file"""
        try:
            if os.path.exists(self.data_file):
                shutil.copy2(self.data_file, self.backup_file)
                return True
        except Exception as e:
            print(f"Backup failed: {e}")
        return False
    
    def restore_backup(self) -> bool:
        """Restore from backup file"""
        try:
            if os.path.exists(self.backup_file):
                shutil.copy2(self.backup_file, self.data_file)
                return True
        except Exception as e:
            print(f"Restore failed: {e}")
        return False
    
    def read_todos(self) -> List[Dict[str, str]]:
        """Read all todos from file and return as list of dictionaries"""
        todos = []
        if not os.path.exists(self.data_file):
            return todos
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split('|', 3)
                        if len(parts) == 4:
                            todos.append({
                                'timestamp': parts[0],
                                'priority': parts[1],
                                'status': parts[2],
                                'task': parts[3]
                            })
        except Exception as e:
            print(f"Error reading todos: {e}")
        
        return todos
    
    def write_todos(self, todos: List[Dict[str, str]]) -> bool:
        """Write todos to file"""
        try:
            # Create backup before writing
            self.create_backup()
            
            with open(self.data_file, 'w', encoding='utf-8') as file:
                for todo in todos:
                    line = f"{todo['timestamp']}|{todo['priority']}|{todo['status']}|{todo['task']}\n"
                    file.write(line)
            return True
        except Exception as e:
            print(f"Error writing todos: {e}")
            return False
    
    def add_todo(self, task: str, priority: str = "Medium") -> bool:
        """Add a new todo to the file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todo_line = f"{timestamp}|{priority}|Pending|{task}\n"
        
        try:
            with open(self.data_file, 'a', encoding='utf-8') as file:
                file.write(todo_line)
            return True
        except Exception as e:
            print(f"Error adding todo: {e}")
            return False
    
    def update_todo_status(self, index: int, new_status: str) -> bool:
        """Update the status of a specific todo"""
        todos = self.read_todos()
        if 0 <= index < len(todos):
            todos[index]['status'] = new_status
            return self.write_todos(todos)
        return False
    
    def update_todo_task(self, index: int, new_task: str) -> bool:
        """Update the task text of a specific todo"""
        todos = self.read_todos()
        if 0 <= index < len(todos):
            todos[index]['task'] = new_task
            return self.write_todos(todos)
        return False
    
    def delete_todo(self, index: int) -> bool:
        """Delete a specific todo"""
        todos = self.read_todos()
        if 0 <= index < len(todos):
            todos.pop(index)
            return self.write_todos(todos)
        return False
    
    def clear_completed(self) -> bool:
        """Remove all completed todos"""
        todos = self.read_todos()
        todos = [todo for todo in todos if todo['status'] != 'Completed']
        return self.write_todos(todos)
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about todos"""
        todos = self.read_todos()
        stats = {
            'total': len(todos),
            'pending': len([t for t in todos if t['status'] == 'Pending']),
            'completed': len([t for t in todos if t['status'] == 'Completed']),
            'high_priority': len([t for t in todos if t['priority'] == 'High' and t['status'] == 'Pending']),
            'medium_priority': len([t for t in todos if t['priority'] == 'Medium' and t['status'] == 'Pending']),
            'low_priority': len([t for t in todos if t['priority'] == 'Low' and t['status'] == 'Pending'])
        }
        return stats
    
    def search_todos(self, search_term: str) -> List[Dict[str, str]]:
        """Search for todos containing the search term"""
        todos = self.read_todos()
        return [todo for todo in todos if search_term.lower() in todo['task'].lower()]
    
    def export_todos(self, export_file: str, format_type: str = "txt") -> bool:
        """Export todos to different formats"""
        todos = self.read_todos()
        
        try:
            if format_type.lower() == "txt":
                with open(export_file, 'w', encoding='utf-8') as file:
                    file.write("=== TODO LIST EXPORT ===\n")
                    file.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    
                    pending = [t for t in todos if t['status'] == 'Pending']
                    completed = [t for t in todos if t['status'] == 'Completed']
                    
                    if pending:
                        file.write("PENDING TASKS:\n")
                        file.write("-" * 50 + "\n")
                        for i, todo in enumerate(pending, 1):
                            file.write(f"{i}. [{todo['priority']}] {todo['task']} (Created: {todo['timestamp']})\n")
                    
                    if completed:
                        file.write("\nCOMPLETED TASKS:\n")
                        file.write("-" * 50 + "\n")
                        for i, todo in enumerate(completed, 1):
                            file.write(f"{i}. [{todo['priority']}] {todo['task']} (Created: {todo['timestamp']})\n")
            
            elif format_type.lower() == "csv":
                import csv
                with open(export_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Timestamp', 'Priority', 'Status', 'Task'])
                    for todo in todos:
                        writer.writerow([todo['timestamp'], todo['priority'], todo['status'], todo['task']])
            
            return True
        except Exception as e:
            print(f"Export failed: {e}")
            return False

def validate_todo_file(file_path: str) -> bool:
    """Validate the structure of a todo file"""
    if not os.path.exists(file_path):
        return True  # Empty file is valid
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:
                    parts = line.split('|', 3)
                    if len(parts) != 4:
                        print(f"Invalid format at line {line_num}: {line}")
                        return False
                    
                    # Validate timestamp format
                    try:
                        datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        print(f"Invalid timestamp at line {line_num}: {parts[0]}")
                        return False
                    
                    # Validate priority
                    if parts[1] not in ['High', 'Medium', 'Low']:
                        print(f"Invalid priority at line {line_num}: {parts[1]}")
                        return False
                    
                    # Validate status
                    if parts[2] not in ['Pending', 'Completed']:
                        print(f"Invalid status at line {line_num}: {parts[2]}")
                        return False
        
        return True
    except Exception as e:
        print(f"File validation error: {e}")
        return False