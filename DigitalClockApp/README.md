# ⏰ Digital Clock & Timer Application - Programming Assignment

**Assignment ID:** DCT-002  
**Course:** Advanced GUI Programming with Python  
**Instructor:** valbenia  
**Assigned Date:** 2025-07-15  
**Due Date:** 2025-07-22  
**Difficulty Level:** Intermediate  
**Estimated Time:** 8-12 hours  

---

## 📋 Assignment Overview

### 🎯 **Objective:**
Create a comprehensive Digital Clock & Timer Application using Python's Tkinter library with advanced features including real-time clock display, countdown timer, stopwatch, and alarm functionality. This assignment will test your understanding of multi-threading, event-driven programming, time manipulation, and complex GUI design.

### 🎮 **Application Description:**
You will build a tabbed application featuring:
- **Real-time Digital Clock** with multiple display formats
- **Countdown Timer** with customizable durations and visual feedback
- **Stopwatch** with lap timing functionality
- **Alarm System** with snooze capabilities
- **Settings Panel** with theme customization and preferences

### 📚 **Learning Goals:**
- Master advanced Tkinter widgets and layout management
- Implement multi-threading for real-time updates
- Handle time operations and datetime manipulation
- Design complex state management systems
- Create responsive and user-friendly interfaces
- Implement data persistence and configuration management

---

## 🏗️ Project Structure Requirements

### 📁 **Required File Organization:**
```
digital_clock_timer/
├── main.py                    # Main application entry point
├── clock_app.py               # Core application class
├── timer_module.py            # Timer functionality
├── stopwatch_module.py        # Stopwatch functionality
├── alarm_module.py            # Alarm system
├── settings_manager.py        # Settings and configuration
├── theme_manager.py           # Theme and styling
├── utils.py                   # Utility functions
├── config/
│   ├── __init__.py
│   ├── themes.json           # Theme definitions
│   └── default_settings.json # Default configuration
├── assets/                   # Optional: sounds and images
│   └── sounds/
│       ├── timer_beep.wav
│       └── alarm_sound.wav
├── docs/                     # Documentation
│   ├── user_manual.md
│   └── technical_specs.md
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

### 🎯 **Core Class Structure:**

```python
# main.py - Entry point
def main():
    """Main application entry point"""
    pass

# clock_app.py - Main application class
class DigitalClockApp:
    """Main application class managing all components"""
    
    def __init__(self, root):
        """Initialize the application"""
        pass
    
    def setup_gui(self):
        """Setup the main GUI structure"""
        pass
    
    def create_tabs(self):
        """Create tabbed interface"""
        pass
    
    def apply_theme(self):
        """Apply current theme to all widgets"""
        pass

# timer_module.py - Timer functionality
class TimerModule:
    """Countdown timer with customizable duration"""
    
    def __init__(self, parent, theme_manager):
        """Initialize timer module"""
        pass
    
    def create_timer_gui(self):
        """Create timer interface"""
        pass
    
    def start_timer(self, hours, minutes, seconds):
        """Start countdown timer"""
        pass
    
    def pause_timer(self):
        """Pause/resume timer"""
        pass
    
    def stop_timer(self):
        """Stop and reset timer"""
        pass
    
    def update_display(self):
        """Update timer display (runs in separate thread)"""
        pass

# stopwatch_module.py - Stopwatch functionality
class StopwatchModule:
    """Stopwatch with lap timing"""
    
    def __init__(self, parent, theme_manager):
        """Initialize stopwatch module"""
        pass
    
    def create_stopwatch_gui(self):
        """Create stopwatch interface"""
        pass
    
    def start_stopwatch(self):
        """Start/resume stopwatch"""
        pass
    
    def pause_stopwatch(self):
        """Pause stopwatch"""
        pass
    
    def record_lap(self):
        """Record lap time"""
        pass
    
    def reset_stopwatch(self):
        """Reset stopwatch to zero"""
        pass

# alarm_module.py - Alarm system
class AlarmModule:
    """Alarm system with snooze functionality"""
    
    def __init__(self, parent, theme_manager, sound_manager):
        """Initialize alarm module"""
        pass
    
    def create_alarm_gui(self):
        """Create alarm interface"""
        pass
    
    def set_alarm(self, time_string):
        """Set alarm time"""
        pass
    
    def enable_alarm(self):
        """Enable alarm monitoring"""
        pass
    
    def disable_alarm(self):
        """Disable alarm"""
        pass
    
    def trigger_alarm(self):
        """Trigger alarm notification"""
        pass
    
    def snooze_alarm(self, minutes):
        """Snooze alarm for specified minutes"""
        pass

# settings_manager.py - Settings and configuration
class SettingsManager:
    """Manage application settings and persistence"""
    
    def __init__(self, config_file="settings.json"):
        """Initialize settings manager"""
        pass
    
    def load_settings(self):
        """Load settings from file"""
        pass
    
    def save_settings(self):
        """Save current settings to file"""
        pass
    
    def get_setting(self, key, default=None):
        """Get specific setting value"""
        pass
    
    def set_setting(self, key, value):
        """Set specific setting value"""
        pass
    
    def reset_to_defaults(self):
        """Reset all settings to default values"""
        pass

# theme_manager.py - Theme and styling
class ThemeManager:
    """Manage application themes and styling"""
    
    def __init__(self, themes_file="config/themes.json"):
        """Initialize theme manager"""
        pass
    
    def load_themes(self):
        """Load theme definitions from file"""
        pass
    
    def get_current_theme(self):
        """Get current theme colors"""
        pass
    
    def set_theme(self, theme_name):
        """Set active theme"""
        pass
    
    def apply_theme_to_widget(self, widget, widget_type):
        """Apply theme colors to specific widget"""
        pass
    
    def get_available_themes(self):
        """Get list of available themes"""
        pass

# utils.py - Utility functions
def format_time(seconds, include_hours=True, include_centiseconds=False):
    """Format seconds into time string"""
    pass

def validate_time_input(time_string):
    """Validate time input format"""
    pass

def play_sound(sound_file, duration=1000):
    """Play sound file"""
    pass

def get_system_timezone():
    """Get system timezone information"""
    pass

def create_notification(title, message, sound=True):
    """Create system notification"""
    pass
```

---

## ✅ Implementation Requirements

### 🎯 **Core Features (80 points):**

#### 1. **Digital Clock Display (20 points)**
- ✅ **Real-time clock** updates every second
- ✅ **Multiple time formats** (12/24 hour with AM/PM)
- ✅ **Date display** with full day, month, year
- ✅ **Time zone information** display
- ✅ **Uptime counter** showing application runtime
- ✅ **Large, readable font** for time display
- ✅ **Threading implementation** for smooth updates

#### 2. **Countdown Timer (20 points)**
- ✅ **Customizable duration** (hours, minutes, seconds)
- ✅ **Start/Pause/Stop** functionality
- ✅ **Visual progress bar** showing remaining time
- ✅ **Color-coded display** (green → yellow → red)
- ✅ **Quick timer presets** (1min, 5min, 10min, 15min, 30min, 1hr)
- ✅ **Completion notification** with sound
- ✅ **Thread-safe updates** without UI blocking

#### 3. **Stopwatch Functionality (20 points)**
- ✅ **Precise timing** with centiseconds display
- ✅ **Start/Pause/Resume** controls
- ✅ **Lap timing** with numbered records
- ✅ **Scrollable lap history** display
- ✅ **Reset functionality** to clear all times
- ✅ **Export lap times** to CSV file
- ✅ **High-precision timing** implementation

#### 4. **Alarm System (20 points)**
- ✅ **Set alarm time** in HH:MM format
- ✅ **Enable/Disable** alarm toggle
- ✅ **Visual status indicator** (ON/OFF with colors)
- ✅ **Snooze functionality** with customizable duration
- ✅ **Sound notification** when alarm triggers
- ✅ **Multiple alarm support** (bonus)
- ✅ **Alarm persistence** across app sessions

### 🌟 **Advanced Features (20 points):**

#### 5. **User Interface & Experience (10 points)**
- ✅ **Tabbed interface** using ttk.Notebook
- ✅ **Responsive design** with proper layout management
- ✅ **Keyboard shortcuts** for common actions
- ✅ **Context menus** for additional options
- ✅ **Tooltips** for user guidance
- ✅ **Window state management** (minimize to tray)

#### 6. **Customization & Settings (10 points)**
- ✅ **Multiple themes** (Dark, Light, Colorful)
- ✅ **Settings persistence** to JSON file
- ✅ **Sound enable/disable** option
- ✅ **Always on top** window option
- ✅ **Font size customization**
- ✅ **Export/Import settings**

### 🎨 **Bonus Features (+20 points):**

#### 7. **Enhanced Functionality (+10 points)**
- ✅ **World clock** with multiple time zones
- ✅ **Pomodoro timer** with work/break cycles
- ✅ **Voice notifications** using text-to-speech
- ✅ **System tray integration**
- ✅ **Calendar integration**

#### 8. **Polish & Extras (+10 points)**
- ✅ **Smooth animations** for transitions
- ✅ **Custom sound files** support
- ✅ **Database storage** for settings and history
- ✅ **Network time synchronization**
- ✅ **Plugin system** for extensibility

---

## 🧪 Testing Requirements

### 🔍 **Required Test Cases:**

#### **Timer Module Tests:**
```python
def test_timer_creation():
    """Test timer initialization"""
    pass

def test_timer_start_stop():
    """Test timer start/stop functionality"""
    pass

def test_timer_pause_resume():
    """Test timer pause/resume"""
    pass

def test_timer_completion():
    """Test timer completion notification"""
    pass

def test_quick_timer_presets():
    """Test quick timer buttons"""
    pass
```

#### **Stopwatch Module Tests:**
```python
def test_stopwatch_accuracy():
    """Test stopwatch timing accuracy"""
    pass

def test_lap_timing():
    """Test lap recording functionality"""
    pass

def test_stopwatch_reset():
    """Test stopwatch reset"""
    pass

def test_lap_export():
    """Test lap times export to CSV"""
    pass
```

#### **Alarm Module Tests:**
```python
def test_alarm_setting():
    """Test alarm time setting"""
    pass

def test_alarm_trigger():
    """Test alarm triggering at set time"""
    pass

def test_snooze_functionality():
    """Test alarm snooze feature"""
    pass

def test_alarm_persistence():
    """Test alarm settings persistence"""
    pass
```

#### **Settings & Theme Tests:**
```python
def test_settings_save_load():
    """Test settings persistence"""
    pass

def test_theme_switching():
    """Test theme changes"""
    pass

def test_settings_validation():
    """Test settings validation"""
    pass
```

#### **Integration Tests:**
```python
def test_multi_threading():
    """Test thread safety and synchronization"""
    pass

def test_memory_usage():
    """Test memory efficiency during long runs"""
    pass

def test_error_handling():
    """Test error handling and recovery"""
    pass
```

---

## 📊 Grading Rubric

| Component | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D/F) |
|-----------|---------------|----------|------------------|------------------|
| **Digital Clock** | Perfect real-time display, multiple formats, threading | Good display, basic threading | Basic clock works | Clock doesn't update properly |
| **Timer Function** | Full functionality, visual feedback, presets | Core features work, minor issues | Basic countdown works | Timer doesn't work reliably |
| **Stopwatch** | Precise timing, lap records, export | Good timing, lap functionality | Basic stopwatch works | Timing inaccurate or broken |
| **Alarm System** | Full alarm, snooze, persistence | Basic alarm with snooze | Simple alarm notification | Alarm doesn't trigger |
| **User Interface** | Professional, responsive, intuitive | Clean, functional design | Basic but usable | Poor layout or confusing |
| **Threading** | Proper multi-threading, no blocking | Good threading implementation | Basic threading works | UI blocks or freezes |
| **Settings/Themes** | Full customization, persistence | Good settings management | Basic settings work | Settings don't save/load |
| **Code Quality** | Clean, documented, modular | Well-structured, readable | Adequate organization | Poor structure or documentation |
| **Testing** | Comprehensive test suite | Good test coverage | Basic tests present | Missing or inadequate tests |

### 🎯 **Grade Breakdown:**
- **A (90-100):** All requirements + advanced features + excellent code quality + comprehensive testing
- **B (80-89):** All core requirements + some advanced features + good implementation
- **C (70-79):** Most core requirements + functional but basic implementation
- **D/F (<70):** Major requirements missing or non-functional code

---

## 🚀 Implementation Guidelines

### 📅 **Week 1 (Days 1-3): Foundation**
- ✅ Set up project structure and file organization
- ✅ Create main application window and tabbed interface
- ✅ Implement basic digital clock with real-time updates
- ✅ Set up threading for clock updates
- ✅ Create basic theme system

### 📅 **Week 2 (Days 4-5): Core Features**
- ✅ Implement countdown timer with all controls
- ✅ Add stopwatch functionality with lap timing
- ✅ Create alarm system with basic notifications
- ✅ Implement settings persistence

### 📅 **Week 3 (Days 6-7): Polish & Testing**
- ✅ Add advanced features and customization
- ✅ Implement comprehensive testing suite
- ✅ Polish user interface and add animations
- ✅ Write documentation and prepare submission

### 🛠️ **Development Tips:**

#### **Threading Best Practices:**
```python
import threading
import time

def update_clock(self):
    """Safe threading for real-time updates"""
    while self.running:
        current_time = time.strftime("%H:%M:%S")
        # Use root.after() for thread-safe GUI updates
        self.root.after(0, lambda: self.clock_label.config(text=current_time))
        time.sleep(1)

# Start thread
self.clock_thread = threading.Thread(target=self.update_clock, daemon=True)
self.clock_thread.start()
```

#### **Settings Management:**
```python
import json
import os

class SettingsManager:
    def __init__(self, config_file="settings.json"):
        self.config_file = config_file
        self.settings = self.load_settings()
    
    def load_settings(self):
        """Load settings with error handling"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading settings: {e}")
        
        return self.get_default_settings()
    
    def save_settings(self):
        """Save settings with error handling"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")
```

#### **Theme Implementation:**
```python
class ThemeManager:
    def __init__(self):
        self.themes = {
            "dark": {
                "bg": "#1a1a2e",
                "fg": "#ffffff",
                "accent": "#16213e",
                "button": "#0f3460",
                "success": "#00ff41",
                "warning": "#ff9500",
                "error": "#ff0040"
            },
            "light": {
                "bg": "#f8f9fa",
                "fg": "#2c3e50",
                "accent": "#e9ecef",
                "button": "#007bff",
                "success": "#28a745",
                "warning": "#ffc107",
                "error": "#dc3545"
            }
        }
    
    def apply_theme(self, theme_name, widget):
        """Apply theme to widget"""
        colors = self.themes.get(theme_name, self.themes["dark"])
        widget.configure(bg=colors["bg"], fg=colors["fg"])
```

---

## 📝 Required Configuration Files

### 🎨 **config/themes.json**
```json
{
  "dark": {
    "name": "Dark Theme",
    "colors": {
      "background": "#1a1a2e",
      "foreground": "#ffffff",
      "accent": "#16213e",
      "button": "#0f3460",
      "success": "#00ff41",
      "warning": "#ff9500",
      "error": "#ff0040"
    }
  },
  "light": {
    "name": "Light Theme",
    "colors": {
      "background": "#f8f9fa",
      "foreground": "#2c3e50",
      "accent": "#e9ecef",
      "button": "#007bff",
      "success": "#28a745",
      "warning": "#ffc107",
      "error": "#dc3545"
    }
  },
  "colorful": {
    "name": "Colorful Theme",
    "colors": {
      "background": "#2d1b69",
      "foreground": "#ffffff",
      "accent": "#11998e",
      "button": "#ff6b6b",
      "success": "#4ecdc4",
      "warning": "#ffe66d",
      "error": "#ff6b6b"
    }
  }
}
```

### ⚙️ **config/default_settings.json**
```json
{
  "appearance": {
    "theme": "dark",
    "font_size": 12,
    "always_on_top": false,
    "window_position": "center"
  },
  "clock": {
    "format_24hour": true,
    "show_seconds": true,
    "show_date": true,
    "show_timezone": true
  },
  "timer": {
    "default_duration": 300,
    "quick_presets": [60, 300, 600, 900, 1800, 3600],
    "sound_enabled": true,
    "visual_notifications": true
  },
  "stopwatch": {
    "precision": "centiseconds",
    "auto_lap": false,
    "export_format": "csv"
  },
  "alarm": {
    "sound_enabled": true,
    "snooze_duration": 300,
    "max_snoozes": 3,
    "volume": 0.8
  },
  "advanced": {
    "minimize_to_tray": false,
    "start_minimized": false,
    "auto_save_interval": 60,
    "backup_settings": true
  }
}
```

### 📦 **requirements.txt**
```txt
tkinter
threading
datetime
json
os
time
winsound
playsound==1.3.0
pygame==2.5.2
pillow==10.0.0
pytest==7.4.0
pytest-cov==4.1.0
```

---

## 📚 Solution Template Files

### 🎯 **main.py - Application Entry Point**
```python
#!/usr/bin/env python3
"""
Digital Clock & Timer Application
Main entry point for the application

Author: [Student Name]
Date: 2025-07-15
Assignment: DCT-002
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from clock_app import DigitalClockApp
from settings_manager import SettingsManager

def main():
    """Main application entry point"""
    try:
        # Initialize settings
        settings = SettingsManager()
        
        # Create main window
        root = tk.Tk()
        root.title("⏰ Digital Clock & Timer")
        root.geometry("600x700")
        
        # Initialize application
        app = DigitalClockApp(root, settings)
        
        # Center window on screen
        app.center_window()
        
        # Start application
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Application Error", f"Failed to start application: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### 🏗️ **clock_app.py - Main Application Class**
```python
"""
Digital Clock & Timer Application
Main application class managing all components

Author: [Student Name]
Date: 2025-07-15
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import datetime

from timer_module import TimerModule
from stopwatch_module import StopwatchModule
from alarm_module import AlarmModule
from theme_manager import ThemeManager

class DigitalClockApp:
    """Main application class managing all components"""
    
    def __init__(self, root, settings_manager):
        """Initialize the application"""
        self.root = root
        self.settings = settings_manager
        self.theme_manager = ThemeManager()
        
        # Application state
        self.running = True
        self.start_time = time.time()
        
        # Initialize components
        self.timer_module = None
        self.stopwatch_module = None
        self.alarm_module = None
        
        # Setup GUI
        self.setup_gui()
        self.create_tabs()
        self.apply_theme()
        
        # Start clock update thread
        self.start_clock_thread()
        
        # Bind events
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_gui(self):
        """Setup the main GUI structure"""
        # TODO: Implement main GUI setup
        pass
    
    def create_tabs(self):
        """Create tabbed interface"""
        # TODO: Implement tabbed interface
        pass
    
    def apply_theme(self):
        """Apply current theme to all widgets"""
        # TODO: Implement theme application
        pass
    
    def start_clock_thread(self):
        """Start the clock update thread"""
        # TODO: Implement clock threading
        pass
    
    def center_window(self):
        """Center window on screen"""
        # TODO: Implement window centering
        pass
    
    def on_closing(self):
        """Handle application closing"""
        # TODO: Implement graceful shutdown
        pass
```

### ⏱️ **timer_module.py - Timer Implementation**
```python
"""
Timer Module for Digital Clock Application
Implements countdown timer functionality

Author: [Student Name]
Date: 2025-07-15
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

class TimerModule:
    """Countdown timer with customizable duration"""
    
    def __init__(self, parent, theme_manager):
        """Initialize timer module"""
        self.parent = parent
        self.theme_manager = theme_manager
        
        # Timer state
        self.timer_running = False
        self.timer_paused = False
        self.timer_remaining = 0
        self.timer_total = 0
        
        # GUI variables
        self.hours_var = tk.IntVar(value=0)
        self.minutes_var = tk.IntVar(value=5)
        self.seconds_var = tk.IntVar(value=0)
        
        # Create GUI
        self.create_timer_gui()
        
        # Start update thread
        self.start_update_thread()
    
    def create_timer_gui(self):
        """Create timer interface"""
        # TODO: Implement timer GUI
        pass
    
    def start_timer(self, hours, minutes, seconds):
        """Start countdown timer"""
        # TODO: Implement timer start
        pass
    
    def pause_timer(self):
        """Pause/resume timer"""
        # TODO: Implement timer pause
        pass
    
    def stop_timer(self):
        """Stop and reset timer"""
        # TODO: Implement timer stop
        pass
    
    def update_display(self):
        """Update timer display (runs in separate thread)"""
        # TODO: Implement timer display updates
        pass
    
    def start_update_thread(self):
        """Start the timer update thread"""
        # TODO: Implement timer threading
        pass
    
    def timer_finished(self):
        """Handle timer completion"""
        # TODO: Implement timer completion
        pass
```

### 📊 **Test Template - test_timer.py**
```python
"""
Unit tests for Timer Module
Tests timer functionality and edge cases

Author: [Student Name]
Date: 2025-07-15
"""

import unittest
import time
import tkinter as tk
from unittest.mock import Mock, patch

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from timer_module import TimerModule
from theme_manager import ThemeManager

class TestTimerModule(unittest.TestCase):
    """Test cases for TimerModule"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.root = tk.Tk()
        self.theme_manager = ThemeManager()
        self.timer = TimerModule(self.root, self.theme_manager)
    
    def tearDown(self):
        """Clean up after tests"""
        self.root.destroy()
    
    def test_timer_initialization(self):
        """Test timer initialization"""
        # TODO: Test timer creation
        pass
    
    def test_timer_start_stop(self):
        """Test timer start/stop functionality"""
        # TODO: Test timer controls
        pass
    
    def test_timer_pause_resume(self):
        """Test timer pause/resume"""
        # TODO: Test timer pause functionality
        pass
    
    def test_timer_completion(self):
        """Test timer completion notification"""
        # TODO: Test timer completion
        pass
    
    def test_quick_timer_presets(self):
        """Test quick timer buttons"""
        # TODO: Test preset buttons
        pass
    
    def test_timer_validation(self):
        """Test timer input validation"""
        # TODO: Test input validation
        pass

if __name__ == '__main__':
    unittest.main()
```

---
## 🆘 Help and Resources

### 📚 **Required Reading:**
- [Python Threading Tutorial](https://docs.python.org/3/library/threading.html)
- [Tkinter Time and Date Widgets](https://docs.python.org/3/library/tkinter.html)
- [JSON Configuration Management](https://docs.python.org/3/library/json.html)

### 🔗 **Helpful Resources:**
- [Real-time GUI Updates with Threading](https://stackoverflow.com/questions/459336/how-to-run-functions-in-background-in-tkinter)
- [Tkinter Best Practices](https://python-course.eu/tkinter/layout-management-in-tkinter.php)
- [Time Format Handling](https://docs.python.org/3/library/datetime.html)

### 🎯 **Success Tips:**
1. **Start with the basics** - Get the clock working first
2. **Use threading correctly** - Don't block the GUI
3. **Test frequently** - Verify each feature as you build
4. **Handle errors gracefully** - Provide user feedback
5. **Document as you go** - Don't leave documentation for last

---

**Good luck with your Digital Clock & Timer Application!** ⏰🚀

*This assignment is designed to challenge you while providing a solid foundation for advanced GUI programming. Focus on creating a professional, user-friendly application that demonstrates your mastery of Python GUI development.*

**Remember:** The goal is to learn advanced programming concepts while building something useful and engaging. Take your time to understand each component and don't hesitate to ask for help when needed.
