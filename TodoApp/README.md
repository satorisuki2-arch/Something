# ToDo App - User Guide & Documentation

## 📋 Overview

This is a comprehensive ToDo application built with Python and Tkinter. The app provides a user-friendly interface for managing tasks with priority levels, search functionality, and data persistence using text files.

## 🚀 Features

### Core Features
- ✅ Add, edit, and delete tasks
- 🎯 Priority levels (High, Medium, Low)
- ✔️ Mark tasks as complete
- 🔍 Search functionality
- 📊 Statistics and analytics
- 💾 Data persistence with text files

### Advanced Features
- 🔄 Backup and restore functionality
- 📤 Export to TXT and CSV formats
- 📁 File management (New, Open files)
- 🎨 Color-coded priority display
- ⌨️ Keyboard shortcuts
- 📈 Real-time statistics

## 🛠 Tech Stack

- **Frontend**: Python Tkinter
- **Backend**: Python Standard Library
- **Database**: Text file (.txt format)
- **Configuration**: Python dictionaries
- **File Handling**: Custom file manager module

## 📁 Project Structure

```
TodoApp/
├── todo_app.py              # Basic version of the app
├── enhanced_todo_app.py     # Full-featured version
├── file_manager.py          # File operations module
├── config.py               # Configuration settings
├── run_app.py              # Application launcher
├── requirements.txt        # Dependencies (minimal)
├── README.md              # This documentation
├── todos.txt              # Data file (created automatically)
└── todos_backup.txt       # Backup file (created automatically)
```

## ⚡ Quick Start

### Prerequisites
- Python 3.6 or higher
- Standard Python installation (no external packages needed)

### Installation & Running

1. **Download/Clone the project**
   ```bash
   # Navigate to the TodoApp directory
   cd TodoApp
   ```

2. **Run the application**
   ```bash
   # Method 1: Using the launcher
   python run_app.py

   # Method 2: Direct execution
   python enhanced_todo_app.py

   # Method 3: Basic version
   python todo_app.py
   ```

3. **The app will start with an empty task list**

## 📖 User Guide

### Adding Tasks

1. **Enter task description** in the text field
2. **Select priority** from dropdown (High/Medium/Low)
3. **Click "Add Task"** or press Enter
4. Task appears in the list with color coding:
   - 🔴 **Red**: High priority
   - 🟠 **Orange**: Medium priority
   - 🟢 **Green**: Low priority

### Managing Tasks

#### Completing Tasks
- Select a task from the list
- Click **"Complete"** button
- Completed tasks show with ✓ and gray color

#### Editing Tasks
- **Double-click** on a task, OR
- Select task and click **"Edit"** button
- Enter new task description
- Note: Cannot edit completed tasks

#### Deleting Tasks
- Select a task from the list
- Click **"Delete"** button
- Confirm deletion in the dialog

### Search Functionality

1. **Type in search box** to filter tasks in real-time
2. **Click "Clear"** to show all tasks again
3. **Menu → Edit → Search** for dialog-based search

### File Operations

#### Menu Options
- **File → New**: Clear all tasks (with confirmation)
- **File → Open**: Load tasks from another file
- **File → Backup**: Create backup of current data
- **File → Restore**: Restore from backup file
- **File → Export as TXT**: Export readable format
- **File → Export as CSV**: Export spreadsheet format

#### Automatic Backups
- Backup created automatically before major operations
- Backup file: `todos_backup.txt`

### Statistics

#### Real-time Display
- **Total tasks**
- **Pending vs Completed**
- **Priority breakdown**

#### Detailed Statistics
- **View → Show Statistics** for complete analytics
- **Completion percentage**
- **Priority distribution**

## 🔧 Configuration

### Customizing the App

Edit `config.py` to modify:

```python
APP_CONFIG = {
    'window_title': 'My ToDo App',           # App title
    'window_size': '600x500',                # Window dimensions
    'theme': {
        'bg_color': '#f0f0f0',              # Background color
        'primary_color': '#4CAF50',          # Add button color
        'font_family': 'Arial',              # Font family
        'font_size': 12                      # Font size
    },
    'priorities': ['High', 'Medium', 'Low'],  # Available priorities
    'priority_colors': {                      # Priority color mapping
        'High': 'red',
        'Medium': 'orange', 
        'Low': 'green'
    }
}
```

## 💾 Data Format

### File Structure
Tasks are stored in `todos.txt` with pipe-separated values:
```
TIMESTAMP|PRIORITY|STATUS|TASK_DESCRIPTION
```

### Example Data
```
2024-10-24 10:30:15|High|Pending|Complete project documentation
2024-10-24 11:45:22|Medium|Completed|Review code changes
2024-10-24 14:20:05|Low|Pending|Update README file
```

### Data Fields
- **TIMESTAMP**: Creation date/time (YYYY-MM-DD HH:MM:SS)
- **PRIORITY**: High, Medium, or Low
- **STATUS**: Pending or Completed
- **TASK_DESCRIPTION**: The actual task text

## ⌨️ Keyboard Shortcuts

- **Enter**: Add new task (when in task entry field)
- **Double-click**: Edit selected task
- **Delete key**: Delete selected task (with confirmation)
- **F5**: Refresh display
- **Ctrl+N**: New file
- **Ctrl+O**: Open file
- **Ctrl+S**: Create backup
- **Ctrl+F**: Search

## 🧪 Testing the App

### Manual Testing Steps

1. **Basic Operations**
   ```
   ✅ Add a new task
   ✅ Edit a task
   ✅ Mark task as complete
   ✅ Delete a task
   ```

2. **Priority Testing**
   ```
   ✅ Add tasks with different priorities
   ✅ Verify color coding
   ✅ Check priority in statistics
   ```

3. **Search Testing**
   ```
   ✅ Search for existing task
   ✅ Search for non-existing task
   ✅ Clear search results
   ```

4. **File Operations**
   ```
   ✅ Create backup
   ✅ Restore from backup
   ✅ Export to TXT/CSV
   ✅ Open different file
   ```

### Automated Testing
```python
# Example test cases (future implementation)
def test_add_task():
    # Test task addition functionality
    pass

def test_file_operations():
    # Test file save/load operations
    pass
```

## 🐛 Troubleshooting

### Common Issues

#### App Won't Start
```
Error: ModuleNotFoundError: No module named 'tkinter'
Solution: Install Python with Tkinter support
```

#### File Permission Errors
```
Error: Permission denied when saving
Solution: Run from a directory with write permissions
```

#### Data File Corruption
```
Error: Invalid data format
Solution: Use File → Restore to recover from backup
```

### Data Recovery

1. **Check backup file**: `todos_backup.txt`
2. **Manual recovery**: Edit `todos.txt` directly
3. **Last resort**: Start fresh with File → New

## 🔄 Future Enhancements

### Planned Features
- [ ] **Due dates and reminders**
- [ ] **Task categories/tags**
- [ ] **Multiple todo lists**
- [ ] **Cloud synchronization**
- [ ] **Mobile app version**
- [ ] **Themes and customization**

### Technical Improvements
- [ ] **SQLite database option**
- [ ] **Unit test coverage**
- [ ] **Configuration GUI**
- [ ] **Plugin architecture**
- [ ] **Undo/Redo functionality**

## 📝 Development Notes

### Code Architecture
```
enhanced_todo_app.py    # Main GUI application
├── EnhancedTodoApp    # Main application class
├── GUI Components     # Widgets and layout
├── Event Handlers     # User interaction logic
└── Display Methods    # Data visualization

file_manager.py         # Data persistence layer
├── TodoFileManager    # File operations class
├── CRUD Operations    # Create, Read, Update, Delete
├── Backup System      # Data backup/restore
└── Export Functions   # Data export utilities

config.py              # Configuration management
└── APP_CONFIG         # Application settings dictionary
```

### Best Practices Implemented
- **Separation of concerns**: GUI, logic, and data layers
- **Error handling**: Try-catch blocks with user feedback
- **Data validation**: Input sanitization and format checking
- **User experience**: Confirmations for destructive operations
- **Modularity**: Reusable components and functions

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and distribute.

## 🤝 Contributing

### How to Contribute
1. **Fork the project**
2. **Create feature branch**
3. **Make improvements**
4. **Test thoroughly**
5. **Submit pull request**

### Coding Standards
- **PEP 8** style guide
- **Meaningful variable names**
- **Comprehensive comments**
- **Error handling**
- **Type hints where applicable**

## 📞 Support

For issues, questions, or suggestions:
- **Check troubleshooting section**
- **Review user guide**
- **Create GitHub issue** (if applicable)
- **Contact developer**

---

**Happy Task Managing! 🎯**

*This documentation covers all aspects of the ToDo app. Keep it handy as a reference while using the application.*