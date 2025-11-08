import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import datetime
import winsound  # For Windows alarm sound (use playsound for cross-platform)
import json
import os

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("⏰ Digital Clock & Timer")
        self.root.geometry("600x700")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)
        
        # Application state
        self.running = True
        self.timer_running = False
        self.timer_paused = False
        self.stopwatch_running = False
        self.stopwatch_paused = False
        self.alarm_active = False
        
        # Timer variables
        self.timer_hours = tk.IntVar(value=0)
        self.timer_minutes = tk.IntVar(value=5)
        self.timer_seconds = tk.IntVar(value=0)
        self.timer_remaining = 0
        
        # Stopwatch variables
        self.stopwatch_start_time = 0
        self.stopwatch_elapsed = 0
        self.stopwatch_pause_time = 0
        
        # Alarm variables
        self.alarm_time = tk.StringVar(value="07:00")
        self.alarm_enabled = tk.BooleanVar(value=False)
        
        # Theme variables
        self.theme = "light"  # dark, light, colorful
        self.themes = {
            "dark": {
                "bg": "#1a1a2e",
                "fg": "#ffffff",
                "accent": "#16213e",
                "button": "#8fafd5",
                "success": "#2c392f",
                "warning": "#caba75",
                "error": "#5e2e3a",
                "text": "#F0F0F0",
            },
            "light": {
                "bg": "#dcdad5",
                "fg": "#2c3e50",
                "accent": "#e9ecef",
                "button": "#007bff",
                "success": "#28a745",
                "warning": "#ffc107",
                "error": "#dc3545",
                "text": "#2B2B2B",
            },
            "colorful": {
                "bg": "#ad4f4f",
                "fg": "#ffffff",
                "accent": "#11998e",
                "button": "#ff6b6b",
                "success": "#4ecdc4",
                "warning": "#ffe66d",
                "error": "#ff6b6b"
            }
        }
        
        # Load settings
        self.load_settings()
        
        # Setup GUI
        self.setup_gui()
        
        # Start clock update thread
        self.clock_thread = threading.Thread(target=self.update_clock, daemon=True)
        self.clock_thread.start()
        
        # Start timer thread
        self.timer_thread = threading.Thread(target=self.update_timer, daemon=True)
        self.timer_thread.start()
        
        # Start stopwatch thread
        self.stopwatch_thread = threading.Thread(target=self.update_stopwatch, daemon=True)
        self.stopwatch_thread.start()
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_gui(self):
        """Setup the complete interface"""
        
        # Apply theme
        self.apply_theme()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_clock_tab()
        self.create_timer_tab()
        self.create_stopwatch_tab()
        self.create_alarm_tab()
        self.create_settings_tab()
    
    def apply_theme(self):
        """Apply current theme colors"""
        colors = self.themes[self.theme]
        self.root.configure(bg=colors["bg"])
        
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure notebook style
        style.configure('TNotebook', background=colors["bg"])
        style.configure('TNotebook.Tab', background=colors["bg"], foreground=colors["fg"])
        
        # Configure button style
        style.configure('Custom.TButton', background=colors["button"], foreground=colors["fg"])
    
    def create_clock_tab(self):
        """Create main clock display tab"""
        
        clock_frame = ttk.Frame(self.notebook)
        self.notebook.add(clock_frame, text="🕐 Clock")
        
        # Configure frame
        clock_frame.configure(style='Custom.TFrame')
        
        # Main clock display
        self.clock_label = tk.Label(
            clock_frame,
            text="00:00:00",
            font=("Digital-7", 60, "bold"),  # Use monospace if Digital-7 not available
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["text"]
        )
        self.clock_label.pack(pady=50)
        
        # Date display
        self.date_label = tk.Label(
            clock_frame,
            text="Monday, January 1, 2025",
            font=("Arial", 18, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        )
        self.date_label.pack(pady=10)
        
        # Time zone display
        self.timezone_label = tk.Label(
            clock_frame,
            text="UTC+0",
            font=("Arial", 12),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        )
        self.timezone_label.pack(pady=5)
        
        # Format toggle buttons
        format_frame = tk.Frame(clock_frame, bg=self.themes[self.theme]["bg"])
        format_frame.pack(pady=20)
        
        self.format_24hr = tk.BooleanVar(value=True)
        
        format_12_btn = tk.Radiobutton(
            format_frame,
            text="12 Hour",
            variable=self.format_24hr,
            value=False,
            font=("Arial", 12),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"],
            selectcolor=self.themes[self.theme]["accent"]
        )
        format_12_btn.pack(side="left", padx=20)
        
        format_24_btn = tk.Radiobutton(
            format_frame,
            text="24 Hour",
            variable=self.format_24hr,
            value=True,
            font=("Arial", 12),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"],
            selectcolor=self.themes[self.theme]["accent"]
        )
        format_24_btn.pack(side="left", padx=20)
        
        # Current time info
        info_frame = tk.Frame(clock_frame, bg=self.themes[self.theme]["bg"])
        info_frame.pack(pady=30)
        
        self.uptime_label = tk.Label(
            info_frame,
            text="App Running: 00:00:00",
            font=("Arial", 10),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        )
        self.uptime_label.pack()
        
        # Store start time for uptime calculation
        self.start_time = time.time()
    
    def create_timer_tab(self):
        """Create countdown timer tab"""
        
        timer_frame = ttk.Frame(self.notebook)
        self.notebook.add(timer_frame, text="⏱️ Timer")
        
        # Timer display
        self.timer_display = tk.Label(
            timer_frame,
            text="05:00",
            font=("Digital-7", 48, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["text"]
        )
        self.timer_display.pack(pady=30)
        
        # Timer settings
        settings_frame = tk.Frame(timer_frame, bg=self.themes[self.theme]["bg"])
        settings_frame.pack(pady=20)
        
        tk.Label(
            settings_frame,
            text="Set Timer:",
            font=("Arial", 14, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack()
        
        # Time input spinboxes
        time_frame = tk.Frame(settings_frame, bg=self.themes[self.theme]["bg"])
        time_frame.pack(pady=10)
        
        # Hours
        tk.Label(time_frame, text="Hours:", bg=self.themes[self.theme]["bg"], fg=self.themes[self.theme]["fg"]).grid(row=0, column=0, padx=5)
        hours_spin = tk.Spinbox(
            time_frame,
            from_=0,
            to=23,
            width=5,
            textvariable=self.timer_hours,
            font=("Arial", 12)
        )
        hours_spin.grid(row=0, column=1, padx=5)
        
        # Minutes
        tk.Label(time_frame, text="Minutes:", bg=self.themes[self.theme]["bg"], fg=self.themes[self.theme]["fg"]).grid(row=0, column=2, padx=5)
        minutes_spin = tk.Spinbox(
            time_frame,
            from_=0,
            to=59,
            width=5,
            textvariable=self.timer_minutes,
            font=("Arial", 12)
        )
        minutes_spin.grid(row=0, column=3, padx=5)
        
        # Seconds
        tk.Label(time_frame, text="Seconds:", bg=self.themes[self.theme]["bg"], fg=self.themes[self.theme]["fg"]).grid(row=0, column=4, padx=5)
        seconds_spin = tk.Spinbox(
            time_frame,
            from_=0,
            to=59,
            width=5,
            textvariable=self.timer_seconds,
            font=("Arial", 12)
        )
        seconds_spin.grid(row=0, column=5, padx=5)
        
        # Timer control buttons
        control_frame = tk.Frame(timer_frame, bg=self.themes[self.theme]["bg"])
        control_frame.pack(pady=30)
        
        self.timer_start_btn = tk.Button(
            control_frame,
            text="▶️ Start",
            command=self.start_timer,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["success"],
            fg="white",
            padx=20,
            pady=10
        )
        self.timer_start_btn.pack(side="left", padx=10)
        
        self.timer_pause_btn = tk.Button(
            control_frame,
            text="⏸️ Pause",
            command=self.pause_timer,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["warning"],
            fg="white",
            padx=20,
            pady=10,
            state="disabled"
        )
    
        self.timer_pause_btn.pack(side="left", padx=10)
        
        self.timer_stop_btn = tk.Button(
            control_frame,
            text="⏹️ Stop",
            command=self.stop_timer,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["error"],
            fg="white",
            padx=20,
            pady=10,
            state="disabled"
        )
        self.timer_stop_btn.pack(side="left", padx=10)
        
        # Quick timer buttons
        quick_frame = tk.Frame(timer_frame, bg=self.themes[self.theme]["bg"])
        quick_frame.pack(pady=20)
        
        tk.Label(
            quick_frame,
            text="Quick Timers:",
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack()
        
        quick_buttons_frame = tk.Frame(quick_frame, bg=self.themes[self.theme]["bg"])
        quick_buttons_frame.pack(pady=10)
        
        quick_times = [
            ("1 min", 0, 1, 0),
            ("5 mins", 0, 5, 0),
            # ("10 mins", 0, 10, 0),
            ("15 mins", 0, 15, 0),
            # ("30 mins", 0, 30, 0),
            ("1 hour", 1, 0, 0),
            ("2 hours", 2, 0, 0)
        ]
        
        for text, h, m, s in quick_times:
            btn = tk.Button(
                quick_buttons_frame,
                text=text,
                command=lambda h=h, m=m, s=s: self.set_quick_timer(h, m, s),
                font=("Arial", 10),
                bg=self.themes[self.theme]["button"],
                fg="white",
                padx=10,
                pady=5
            )
            btn.pack(side="left", padx=5)
        
        # Progress bar
        self.timer_progress = ttk.Progressbar(
            timer_frame,
            length=400,
            mode='determinate'
        )
        self.timer_progress.pack(pady=20)
    
    def create_stopwatch_tab(self):
        """Create stopwatch tab"""
        
        stopwatch_frame = ttk.Frame(self.notebook)
        self.notebook.add(stopwatch_frame, text="⏱️ Stopwatch")
        
        # Stopwatch display
        self.stopwatch_display = tk.Label(
            stopwatch_frame,
            text="00:00:00.00",
            font=("Digital-7", 48, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["text"]
        )
        self.stopwatch_display.pack(pady=50)
        
        # Control buttons
        control_frame = tk.Frame(stopwatch_frame, bg=self.themes[self.theme]["bg"])
        control_frame.pack(pady=30)
        
        self.stopwatch_start_btn = tk.Button(
            control_frame,
            text="▶️ Start",
            command=self.start_stopwatch,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["success"],
            fg="white",
            padx=20,
            pady=10,
            
        )
        self.stopwatch_start_btn.pack(side="left", padx=10)
        
        self.stopwatch_pause_btn = tk.Button(
            control_frame,
            text="⏸️ Pause",
            command=self.pause_stopwatch,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["warning"],
            fg="white",
            padx=20,
            pady=10,
            state="disabled"
        )
        self.stopwatch_pause_btn.pack(side="left", padx=10)
        
        self.stopwatch_lap_btn = tk.Button(
            control_frame,
            text="🏁 Lap",
            command=self.lap_stopwatch,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["button"],
            fg="white",
            padx=20,
            pady=10,
            state="disabled"
        )
        self.stopwatch_lap_btn.pack(side="left", padx=10)
        
        self.stopwatch_reset_btn = tk.Button(
            control_frame,
            text="🔄 Reset",
            command=self.reset_stopwatch,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["error"],
            fg="white",
            padx=20,
            pady=10
        )
        self.stopwatch_reset_btn.pack(side="left", padx=10)
        
        # Lap times display
        lap_frame = tk.Frame(stopwatch_frame, bg=self.themes[self.theme]["bg"])
        lap_frame.pack(pady=20, fill="both", expand=True)
        
        tk.Label(
            lap_frame,
            text="Lap Times:",
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack()
        
        # Lap times listbox with scrollbar
        lap_container = tk.Frame(lap_frame, bg=self.themes[self.theme]["bg"])
        lap_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(lap_container)
        scrollbar.pack(side="right", fill="y")
        
        self.lap_listbox = tk.Listbox(
            lap_container,
            yscrollcommand=scrollbar.set,
            font=("Courier", 11),
            bg=self.themes[self.theme]["accent"],
            fg=self.themes[self.theme]["fg"],
            height=8
        )
        self.lap_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.lap_listbox.yview)
        
        # Lap counter
        self.lap_count = 0
    
    def create_alarm_tab(self):
        """Create alarm tab"""
        
        alarm_frame = ttk.Frame(self.notebook)
        self.notebook.add(alarm_frame, text="⏰ Alarm")
        
        # Alarm status
        self.alarm_status_label = tk.Label(
            alarm_frame,
            text="Alarm: OFF",
            font=("Arial", 24, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["error"]
        )
        self.alarm_status_label.pack(pady=30)
        
        # Alarm time setting
        time_frame = tk.Frame(alarm_frame, bg=self.themes[self.theme]["bg"])
        time_frame.pack(pady=20)
        
        tk.Label(
            time_frame,
            text="Set Alarm Time:",
            font=("Arial", 14, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack()
        
        time_entry_frame = tk.Frame(time_frame, bg=self.themes[self.theme]["bg"])
        time_entry_frame.pack(pady=10)
        
        self.alarm_time_entry = tk.Entry(
            time_entry_frame,
            textvariable=self.alarm_time,
            font=("Arial", 16),
            width=8,
            justify="center"
        )
        self.alarm_time_entry.pack(side="left", padx=10)
        
        tk.Label(
            time_entry_frame,
            text="(HH:MM format)",
            font=("Arial", 10),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack(side="left")
        
        # Alarm control
        control_frame = tk.Frame(alarm_frame, bg=self.themes[self.theme]["bg"])
        control_frame.pack(pady=30)
        
        self.alarm_toggle_btn = tk.Button(
            control_frame,
            text="🔔 Enable Alarm",
            command=self.toggle_alarm,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["success"],
            fg="white",
            padx=30,
            pady=15
        )
        self.alarm_toggle_btn.pack()
        
        # Alarm info
        info_frame = tk.Frame(alarm_frame, bg=self.themes[self.theme]["bg"])
        info_frame.pack(pady=20)
        
        self.alarm_info_label = tk.Label(
            info_frame,
            text="Set a time and enable the alarm",
            font=("Arial", 12),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        )
        self.alarm_info_label.pack()
        
        # Snooze options
        snooze_frame = tk.Frame(alarm_frame, bg=self.themes[self.theme]["bg"])
        snooze_frame.pack(pady=20)
        
        tk.Label(
            snooze_frame,
            text="Snooze Duration:",
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack()
        
        self.snooze_var = tk.IntVar(value=5)
        snooze_options = [5, 10, 15, 30]
        
        snooze_buttons_frame = tk.Frame(snooze_frame, bg=self.themes[self.theme]["bg"])
        snooze_buttons_frame.pack(pady=10)
        
        for minutes in snooze_options:
            tk.Radiobutton(
                snooze_buttons_frame,
                text=f"{minutes} min",
                variable=self.snooze_var,
                value=minutes,
                font=("Arial", 10),
                bg=self.themes[self.theme]["bg"],
                fg=self.themes[self.theme]["fg"],
                selectcolor=self.themes[self.theme]["accent"]
            ).pack(side="left", padx=10)
    
    def create_settings_tab(self):
        """Create settings tab"""
        
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="⚙️ Settings")
        
        # Theme selection
        theme_frame = tk.Frame(settings_frame, bg=self.themes[self.theme]["bg"])
        theme_frame.pack(pady=20, fill="x")
        
        tk.Label(
            theme_frame,
            text="Theme:",
            font=("Arial", 14, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack(anchor="w", padx=20)
        
        theme_buttons_frame = tk.Frame(theme_frame, bg=self.themes[self.theme]["bg"])
        theme_buttons_frame.pack(pady=10)
        
        self.theme_var = tk.StringVar(value=self.theme)
        
        for theme_name in self.themes.keys():
            tk.Radiobutton(
                theme_buttons_frame,
                text=theme_name.capitalize(),
                variable=self.theme_var,
                value=theme_name,
                command=self.change_theme,
                font=("Arial", 12),
                bg=self.themes[self.theme]["bg"],
                fg=self.themes[self.theme]["fg"],
                selectcolor=self.themes[self.theme]["accent"]
            ).pack(side="left", padx=20)
        
        # Sound settings
        sound_frame = tk.Frame(settings_frame, bg=self.themes[self.theme]["bg"])
        sound_frame.pack(pady=20, fill="x")
        
        tk.Label(
            sound_frame,
            text="Sound Settings:",
            font=("Arial", 14, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack(anchor="w", padx=20)
        
        self.sound_enabled = tk.BooleanVar(value=True)
        sound_check = tk.Checkbutton(
            sound_frame,
            text="Enable alarm sounds",
            variable=self.sound_enabled,
            font=("Arial", 12),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        )
        sound_check.pack(anchor="w", padx=40, pady=5)
        
        # Always on top
        self.always_on_top = tk.BooleanVar(value=False)
        top_check = tk.Checkbutton(
            sound_frame,
            text="Always on top",
            variable=self.always_on_top,
            command=self.toggle_always_on_top,
            font=("Arial", 12),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        )
        top_check.pack(anchor="w", padx=40, pady=5)
        
        # About section
        about_frame = tk.Frame(settings_frame, bg=self.themes[self.theme]["bg"])
        about_frame.pack(pady=40, fill="x")
        
        tk.Label(
            about_frame,
            text="About:",
            font=("Arial", 14, "bold"),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"]
        ).pack(anchor="w", padx=20)
        
        about_text = """Digital Clock & Timer v1.0
Created by: valbenia
Date: 2025-07-15

Features:
• Real-time digital clock with multiple formats
• Countdown timer with quick presets
• Stopwatch with lap times
• Alarm with snooze functionality
• Multiple themes and customization options"""
        
        tk.Label(
            about_frame,
            text=about_text,
            font=("Arial", 10),
            bg=self.themes[self.theme]["bg"],
            fg=self.themes[self.theme]["fg"],
            justify="left"
        ).pack(anchor="w", padx=40)
        
        # Save settings button
        save_btn = tk.Button(
            settings_frame,
            text="💾 Save Settings",
            command=self.save_settings,
            font=("Arial", 12, "bold"),
            bg=self.themes[self.theme]["success"],
            fg="white",
            padx=20,
            pady=10
        )
        save_btn.pack(pady=20)
    
    # === CLOCK FUNCTIONS ===
    
    def update_clock(self):
        """Update the main clock display"""
        while self.running:
            try:
                current_time = datetime.datetime.now()
                
                # Format time based on user preference
                if self.format_24hr.get():
                    time_string = current_time.strftime("%H:%M:%S")
                else:
                    time_string = current_time.strftime("%I:%M:%S %p")
                
                # Update clock display
                self.root.after(0, lambda: self.clock_label.config(text=time_string))
                
                # Update date
                date_string = current_time.strftime("%A, %B %d, %Y")
                self.root.after(0, lambda: self.date_label.config(text=date_string))
                
                # Update uptime
                uptime = time.time() - self.start_time
                uptime_string = self.format_time(uptime)
                self.root.after(0, lambda: self.uptime_label.config(text=f"App Running: {uptime_string}"))
                
                # Check alarm
                if self.alarm_enabled.get():
                    alarm_time = self.alarm_time.get()
                    current_time_str = current_time.strftime("%H:%M")
                    if current_time_str == alarm_time and not self.alarm_active:
                        self.root.after(0, self.trigger_alarm)
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Clock update error: {e}")
                time.sleep(1)
    
    # === TIMER FUNCTIONS ===
    
    def start_timer(self):
        """Start the countdown timer"""
        if not self.timer_running:
            # Calculate total seconds
            total_seconds = (self.timer_hours.get() * 3600 + 
                           self.timer_minutes.get() * 60 + 
                           self.timer_seconds.get())
            
            if total_seconds <= 0:
                messagebox.showwarning("Warning", "Please set a valid timer duration!")
                return
            
            self.timer_remaining = total_seconds
            self.timer_total = total_seconds
            self.timer_running = True
            self.timer_paused = False
            
            # Update button states
            self.timer_start_btn.config(state="disabled")
            self.timer_pause_btn.config(state="normal")
            self.timer_stop_btn.config(state="normal")
            
            # Update progress bar
            self.timer_progress.config(maximum=total_seconds)
        
        elif self.timer_paused:
            # Resume timer
            self.timer_paused = False
            self.timer_start_btn.config(state="disabled")
            self.timer_pause_btn.config(state="normal")
    
    def pause_timer(self):
        """Pause the countdown timer"""
        if self.timer_running and not self.timer_paused:
            self.timer_paused = True
            self.timer_start_btn.config(state="normal", text="▶️ Resume")
            self.timer_pause_btn.config(state="disabled")
    
    def stop_timer(self):
        """Stop the countdown timer"""
        self.timer_running = False
        self.timer_paused = False
        
        # Reset button states
        self.timer_start_btn.config(state="normal", text="▶️ Start")
        self.timer_pause_btn.config(state="disabled")
        self.timer_stop_btn.config(state="disabled")
        
        # Reset display
        self.timer_display.config(text="00:00")
        self.timer_progress.config(value=0)
    
    def set_quick_timer(self, hours, minutes, seconds):
        """Set quick timer values"""
        self.timer_hours.set(hours)
        self.timer_minutes.set(minutes)
        self.timer_seconds.set(seconds)
    
    def update_timer(self):
        """Update timer countdown"""
        while self.running:
            try:
                if self.timer_running and not self.timer_paused:
                    if self.timer_remaining > 0:
                        # Update display
                        time_str = self.format_timer_time(self.timer_remaining)
                        self.root.after(0, lambda: self.timer_display.config(text=time_str))
                        
                        # Update progress bar
                        progress_value = self.timer_total - self.timer_remaining
                        self.root.after(0, lambda: self.timer_progress.config(value=progress_value))
                        
                        # Update color based on remaining time
                        if self.timer_remaining <= 10:
                            self.root.after(0, lambda: self.timer_display.config(fg=self.themes[self.theme]["error"]))
                        elif self.timer_remaining <= 60:
                            self.root.after(0, lambda: self.timer_display.config(fg=self.themes[self.theme]["warning"]))
                        else:
                            self.root.after(0, lambda: self.timer_display.config(fg=self.themes[self.theme]["success"]))
                        
                        self.timer_remaining -= 1
                    else:
                        # Timer finished
                        self.root.after(0, lambda: self.timer_progress.config(value=self.timer_total))
                        self.root.after(0, self.timer_finished)
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Timer update error: {e}")
                time.sleep(1)
    
    def timer_finished(self):
        """Handle timer completion"""
        self.timer_running = False
        self.timer_display.config(text="00:00", fg=self.themes[self.theme]["error"])
        
        # Reset buttons
        self.timer_start_btn.config(state="normal", text="▶️ Start")
        self.timer_pause_btn.config(state="disabled")
        self.timer_stop_btn.config(state="disabled")
        
        # Play sound and show notification
        if self.sound_enabled.get():
            threading.Thread(target=self.play_timer_sound, daemon=True).start()
        
        messagebox.showinfo("Timer", "⏰ Timer finished!")
    
    # === STOPWATCH FUNCTIONS ===
    def start_stopwatch(self):
        """Start the stopwatch"""
        if not self.stopwatch_running:
            self.stopwatch_start_time = time.time()
            self.stopwatch_running = True
            self.stopwatch_paused = False
            
            # Update button states
            self.stopwatch_start_btn.config(state="disabled")
            self.stopwatch_pause_btn.config(state="normal")
            self.stopwatch_lap_btn.config(state="normal")
        
        elif self.stopwatch_paused:
            # Resume
            self.stopwatch_start_time = time.time() - self.stopwatch_elapsed
            self.stopwatch_paused = False
            self.stopwatch_start_btn.config(state="disabled")
            self.stopwatch_pause_btn.config(state="normal")
    
    def pause_stopwatch(self):
        """Pause the stopwatch"""
        if self.stopwatch_running and not self.stopwatch_paused:
            self.stopwatch_paused = True
            self.stopwatch_elapsed = time.time() - self.stopwatch_start_time
            
            self.stopwatch_start_btn.config(state="normal", text="▶️ Resume")
            self.stopwatch_pause_btn.config(state="disabled")
    
    def lap_stopwatch(self):
        """Record a lap time"""
        if self.stopwatch_running:
            current_time = time.time() - self.stopwatch_start_time
            self.lap_count += 1
            
            lap_time = self.format_stopwatch_time(current_time)
            lap_entry = f"Lap {self.lap_count}: {lap_time}"
            
            self.lap_listbox.insert(tk.END, lap_entry)
            self.lap_listbox.see(tk.END)
    
    def reset_stopwatch(self):
        """Reset the stopwatch"""
        self.stopwatch_running = False
        self.stopwatch_paused = False
        self.stopwatch_elapsed = 0
        self.lap_count = 0
        
        # Reset display
        self.stopwatch_display.config(text="00:00:00.00")
        
        # Reset buttons
        self.stopwatch_start_btn.config(state="normal", text="▶️ Start")
        self.stopwatch_pause_btn.config(state="disabled")
        self.stopwatch_lap_btn.config(state="disabled")
        
        # Clear lap times
        self.lap_listbox.delete(0, tk.END)
    
    def update_stopwatch(self):
        """Update stopwatch display"""
        while self.running:
            try:
                if self.stopwatch_running and not self.stopwatch_paused:
                    elapsed = time.time() - self.stopwatch_start_time
                    time_str = self.format_stopwatch_time(elapsed)
                    self.root.after(0, lambda: self.stopwatch_display.config(text=time_str))
                
                time.sleep(0.01)  # Update every 10ms for smooth display
                
            except Exception as e:
                print(f"Stopwatch update error: {e}")
                time.sleep(0.01)
    
    # === ALARM FUNCTIONS ===
    
    def toggle_alarm(self):
        """Toggle alarm on/off"""
        if self.alarm_enabled.get():
            # Disable alarm
            self.alarm_enabled.set(False)
            self.alarm_status_label.config(text="Alarm: OFF", fg=self.themes[self.theme]["error"])
            self.alarm_toggle_btn.config(text="🔔 Enable Alarm")
            self.alarm_info_label.config(text="Alarm disabled")
        else:
            # Enable alarm
            try:
                # Validate time format
                time_str = self.alarm_time.get()
                datetime.datetime.strptime(time_str, "%H:%M")
                
                self.alarm_enabled.set(True)
                self.alarm_status_label.config(text="Alarm: ON", fg=self.themes[self.theme]["success"])
                self.alarm_toggle_btn.config(text="🔕 Disable Alarm")
                self.alarm_info_label.config(text=f"Alarm set for {time_str}")
                
            except ValueError:
                messagebox.showerror("Error", "Invalid time format! Use HH:MM (24-hour format)")
    
    def trigger_alarm(self):
        """Trigger the alarm"""
        self.alarm_active = True
        
        # Play alarm sound
        if self.sound_enabled.get():
            threading.Thread(target=self.play_alarm_sound, daemon=True).start()
        
        # Show alarm dialog
        result = messagebox.askyesnocancel(
            "⏰ ALARM!", 
            f"Alarm time reached!\n\nTime: {self.alarm_time.get()}\n\nSnooze for {self.snooze_var.get()} minutes?",
            icon='warning'
        )
        
        if result is True:  # Snooze
            self.snooze_alarm()
        elif result is False:  # Turn off
            self.alarm_enabled.set(False)
            self.alarm_status_label.config(text="Alarm: OFF", fg=self.themes[self.theme]["error"])
            self.alarm_toggle_btn.config(text="🔔 Enable Alarm")
            self.alarm_info_label.config(text="Alarm turned off")
        
        self.alarm_active = False
    
    def snooze_alarm(self):
        """Snooze the alarm"""
        current_time = datetime.datetime.now()
        snooze_time = current_time + datetime.timedelta(minutes=self.snooze_var.get())
        new_alarm_time = snooze_time.strftime("%H:%M")
        
        self.alarm_time.set(new_alarm_time)
        self.alarm_info_label.config(text=f"Alarm snoozed until {new_alarm_time}")
    
    # === UTILITY FUNCTIONS ===
    
    def format_time(self, seconds):
        """Format seconds into HH:MM:SS"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def format_timer_time(self, seconds):
        """Format timer time"""
        if seconds >= 3600:
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            seconds = int(seconds % 60)
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            minutes = int(seconds // 60)
            seconds = int(seconds % 60)
            return f"{minutes:02d}:{seconds:02d}"
    
    def format_stopwatch_time(self, seconds):
        """Format stopwatch time with centiseconds"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        centisecs = int((seconds * 100) % 100)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}.{centisecs:02d}"
    
    def play_timer_sound(self):
        """Play timer completion sound"""
        try:
            for _ in range(3):
                winsound.Beep(800, 500)
                time.sleep(0.1)
        except:
            pass
    
    def play_alarm_sound(self):
        """Play alarm sound"""
        try:
            for _ in range(10):
                winsound.Beep(1000, 200)
                time.sleep(0.1)
        except:
            pass
    
    def change_theme(self):
        """Change application theme"""
        self.theme = self.theme_var.get()
        self.apply_theme()
        
        # Update all widgets with new theme
        self.root.configure(bg=self.themes[self.theme]["bg"])
        
        # You would need to update all widgets here
        # For brevity, this is a simplified version
        messagebox.showinfo("Theme", f"Theme changed to {self.theme.capitalize()}!\nRestart app to see full changes.")
    
    def toggle_always_on_top(self):
        """Toggle always on top"""
        self.root.attributes('-topmost', self.always_on_top.get())
    
    def save_settings(self):
        """Save application settings"""
        settings = {
            'theme': self.theme,
            'sound_enabled': self.sound_enabled.get(),
            'always_on_top': self.always_on_top.get(),
            'snooze_duration': self.snooze_var.get(),
            'format_24hr': self.format_24hr.get()
        }
        
        try:
            with open('clock_settings.json', 'w') as f:
                json.dump(settings, f, indent=2)
            messagebox.showinfo("Settings", "Settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")
    
    def load_settings(self):
        """Load application settings"""
        try:
            if os.path.exists('clock_settings.json'):
                with open('clock_settings.json', 'r') as f:
                    settings = json.load(f)
                
                self.theme = settings.get('theme', 'dark')
                # Other settings would be loaded here
                
        except Exception as e:
            print(f"Failed to load settings: {e}")
    
    def on_closing(self):
        """Handle application closing"""
        self.running = False
        self.save_settings()
        self.root.destroy()

def main():
    
    
    """Main function to run the application"""
    
    root = tk.Tk()
    app = DigitalClock(root)
    

    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()