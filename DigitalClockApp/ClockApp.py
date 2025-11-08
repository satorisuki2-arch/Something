import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime

class ClockApp:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Clock variables
        self.time_format = "12"  # 12 or 24 hour format
        self.show_seconds = True
        self.show_date = True
        self.alarm_time = None
        self.alarm_enabled = False
        
        self.setup_ui()
        self.update_clock()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.parent_frame, padding="20")
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Digital Clock", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Time display
        self.time_var = tk.StringVar()
        self.time_label = ttk.Label(main_frame, textvariable=self.time_var, 
                                   font=("Arial", 32, "bold"),
                                   foreground="blue")
        self.time_label.grid(row=1, column=0, columnspan=3, pady=20)
        
        # Date display
        self.date_var = tk.StringVar()
        self.date_label = ttk.Label(main_frame, textvariable=self.date_var, 
                                   font=("Arial", 14))
        self.date_label.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.grid(row=3, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        # Time format selection
        format_frame = ttk.Frame(options_frame)
        format_frame.grid(row=0, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        ttk.Label(format_frame, text="Time Format:").grid(row=0, column=0, padx=(0, 10))
        
        self.format_var = tk.StringVar(value="12")
        format_12 = ttk.Radiobutton(format_frame, text="12 Hour", 
                                   variable=self.format_var, value="12",
                                   command=self.change_format)
        format_12.grid(row=0, column=1, padx=5)
        
        format_24 = ttk.Radiobutton(format_frame, text="24 Hour", 
                                   variable=self.format_var, value="24",
                                   command=self.change_format)
        format_24.grid(row=0, column=2, padx=5)
        
        # Checkboxes
        checkbox_frame = ttk.Frame(options_frame)
        checkbox_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.seconds_var = tk.BooleanVar(value=True)
        seconds_check = ttk.Checkbutton(checkbox_frame, text="Show Seconds",
                                       variable=self.seconds_var,
                                       command=self.toggle_seconds)
        seconds_check.grid(row=0, column=0, padx=10, sticky=tk.W)
        
        self.date_var_check = tk.BooleanVar(value=True)
        date_check = ttk.Checkbutton(checkbox_frame, text="Show Date",
                                    variable=self.date_var_check,
                                    command=self.toggle_date)
        date_check.grid(row=0, column=1, padx=10, sticky=tk.W)
        
        # Alarm frame
        alarm_frame = ttk.LabelFrame(main_frame, text="Alarm", padding="10")
        alarm_frame.grid(row=4, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        # Alarm time input
        alarm_input_frame = ttk.Frame(alarm_frame)
        alarm_input_frame.grid(row=0, column=0, columnspan=3, pady=5)
        
        ttk.Label(alarm_input_frame, text="Set Alarm Time:").grid(row=0, column=0, padx=(0, 10))
        
        self.hour_var = tk.StringVar(value="12")
        hour_spinbox = ttk.Spinbox(alarm_input_frame, from_=1, to=12, 
                                  textvariable=self.hour_var, width=3)
        hour_spinbox.grid(row=0, column=1, padx=2)
        
        ttk.Label(alarm_input_frame, text=":").grid(row=0, column=2)
        
        self.minute_var = tk.StringVar(value="00")
        minute_spinbox = ttk.Spinbox(alarm_input_frame, from_=0, to=59, 
                                    textvariable=self.minute_var, width=3,
                                    format="%02.0f")
        minute_spinbox.grid(row=0, column=3, padx=2)
        
        self.ampm_var = tk.StringVar(value="AM")
        ampm_combo = ttk.Combobox(alarm_input_frame, textvariable=self.ampm_var,
                                 values=["AM", "PM"], width=3, state="readonly")
        ampm_combo.grid(row=0, column=4, padx=(5, 0))
        
        # Alarm buttons
        alarm_btn_frame = ttk.Frame(alarm_frame)
        alarm_btn_frame.grid(row=1, column=0, columnspan=3, pady=10)
        
        self.set_alarm_btn = ttk.Button(alarm_btn_frame, text="Set Alarm",
                                       command=self.set_alarm)
        self.set_alarm_btn.grid(row=0, column=0, padx=5)
        
        self.clear_alarm_btn = ttk.Button(alarm_btn_frame, text="Clear Alarm",
                                         command=self.clear_alarm, state="disabled")
        self.clear_alarm_btn.grid(row=0, column=1, padx=5)
        
        # Alarm status
        self.alarm_status_var = tk.StringVar(value="No alarm set")
        alarm_status_label = ttk.Label(alarm_frame, textvariable=self.alarm_status_var,
                                      font=("Arial", 10))
        alarm_status_label.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Color theme buttons
        theme_frame = ttk.LabelFrame(main_frame, text="Theme", padding="10")
        theme_frame.grid(row=5, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        theme_btn_frame = ttk.Frame(theme_frame)
        theme_btn_frame.grid(row=0, column=0, columnspan=3)
        
        colors = [("Blue", "blue"), ("Green", "green"), ("Red", "red"), ("Purple", "purple")]
        for i, (name, color) in enumerate(colors):
            btn = ttk.Button(theme_btn_frame, text=name, 
                           command=lambda c=color: self.change_color(c))
            btn.grid(row=0, column=i, padx=5)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
    
    def update_clock(self):
        """Update the clock display"""
        now = datetime.now()
        
        # Format time based on user preference
        if self.time_format == "12":
            if self.show_seconds:
                time_str = now.strftime("%I:%M:%S %p")
            else:
                time_str = now.strftime("%I:%M %p")
        else:  # 24 hour format
            if self.show_seconds:
                time_str = now.strftime("%H:%M:%S")
            else:
                time_str = now.strftime("%H:%M")
        
        self.time_var.set(time_str)
        
        # Update date if enabled
        if self.show_date:
            date_str = now.strftime("%A, %B %d, %Y")
            self.date_var.set(date_str)
            self.date_label.grid()
        else:
            self.date_label.grid_remove()
        
        # Check alarm
        self.check_alarm(now)
        
        # Schedule next update
        self.parent_frame.after(1000, self.update_clock)
    
    def change_format(self):
        """Change time format between 12 and 24 hour"""
        self.time_format = self.format_var.get()
    
    def toggle_seconds(self):
        """Toggle showing seconds"""
        self.show_seconds = self.seconds_var.get()
    
    def toggle_date(self):
        """Toggle showing date"""
        self.show_date = self.date_var_check.get()
    
    def change_color(self, color):
        """Change clock color theme"""
        self.time_label.config(foreground=color)
    
    def set_alarm(self):
        """Set the alarm"""
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            ampm = self.ampm_var.get()
            
            # Convert to 24-hour format for comparison
            if ampm == "PM" and hour != 12:
                hour += 12
            elif ampm == "AM" and hour == 12:
                hour = 0
            
            self.alarm_time = (hour, minute)
            self.alarm_enabled = True
            
            # Update UI
            alarm_display = f"{self.hour_var.get()}:{self.minute_var.get():0>2} {ampm}"
            self.alarm_status_var.set(f"Alarm set for {alarm_display}")
            self.set_alarm_btn.config(state="disabled")
            self.clear_alarm_btn.config(state="normal")
            
        except ValueError:
            self.alarm_status_var.set("Invalid time format")
    
    def clear_alarm(self):
        """Clear the alarm"""
        self.alarm_time = None
        self.alarm_enabled = False
        self.alarm_status_var.set("No alarm set")
        self.set_alarm_btn.config(state="normal")
        self.clear_alarm_btn.config(state="disabled")
    
    def check_alarm(self, now):
        """Check if alarm should trigger"""
        if self.alarm_enabled and self.alarm_time:
            current_hour = now.hour
            current_minute = now.minute
            
            if (current_hour, current_minute) == self.alarm_time:
                self.trigger_alarm()
    
    def trigger_alarm(self):
        """Trigger the alarm"""
        # Create alarm popup
        alarm_window = tk.Toplevel(self.parent_frame)
        alarm_window.title("ALARM!")
        alarm_window.geometry("300x150")
        alarm_window.resizable(False, False)
        
        # Center the alarm window
        alarm_window.transient(self.parent_frame)
        alarm_window.grab_set()
        
        # Alarm message
        alarm_label = ttk.Label(alarm_window, text="⏰ ALARM! ⏰", 
                               font=("Arial", 20, "bold"), foreground="red")
        alarm_label.pack(pady=30)
        
        time_label = ttk.Label(alarm_window, text=datetime.now().strftime("%I:%M %p"),
                              font=("Arial", 14))
        time_label.pack(pady=10)
        
        # Stop alarm button
        stop_btn = ttk.Button(alarm_window, text="Stop Alarm",
                             command=lambda: [self.clear_alarm(), alarm_window.destroy()])
        stop_btn.pack(pady=10)