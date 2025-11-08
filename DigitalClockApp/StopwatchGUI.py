import tkinter as tk
from tkinter import ttk
import time

class StopwatchGUI:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Stopwatch variables
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
        self.laps = []
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.parent_frame, padding="20")
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Stopwatch", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Time display
        self.time_var = tk.StringVar(value="00:00.000")
        time_label = ttk.Label(main_frame, textvariable=self.time_var, 
                              font=("Arial", 32, "bold"),
                              foreground="blue")
        time_label.grid(row=1, column=0, columnspan=3, pady=20)
        
        # Control buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Start/Stop button
        self.start_stop_btn = ttk.Button(button_frame, text="Start", 
                                        command=self.toggle_start_stop,
                                        width=10)
        self.start_stop_btn.grid(row=0, column=0, padx=5)
        
        # Lap button
        self.lap_btn = ttk.Button(button_frame, text="Lap", 
                                 command=self.record_lap,
                                 width=10, state="disabled")
        self.lap_btn.grid(row=0, column=1, padx=5)
        
        # Reset button
        self.reset_btn = ttk.Button(button_frame, text="Reset", 
                                   command=self.reset,
                                   width=10)
        self.reset_btn.grid(row=0, column=2, padx=5)
        
        # Lap times frame
        lap_frame = ttk.LabelFrame(main_frame, text="Lap Times", padding="10")
        lap_frame.grid(row=3, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Lap times listbox with scrollbar
        list_frame = ttk.Frame(lap_frame)
        list_frame.pack(fill='both', expand=True)
        
        self.lap_listbox = tk.Listbox(list_frame, height=8, width=40)
        self.lap_listbox.pack(side='left', fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", 
                                 command=self.lap_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.lap_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
    
    def toggle_start_stop(self):
        """Toggle between start and stop"""
        if not self.is_running:
            self.start()
        else:
            self.stop()
    
    def start(self):
        """Start the stopwatch"""
        self.start_time = time.time()
        self.is_running = True
        self.start_stop_btn.config(text="Stop")
        self.lap_btn.config(state="normal")
    
    def stop(self):
        """Stop the stopwatch"""
        if self.is_running:
            self.elapsed_time += time.time() - self.start_time
            self.is_running = False
            self.start_stop_btn.config(text="Start")
            self.lap_btn.config(state="disabled")
    
    def reset(self):
        """Reset the stopwatch"""
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
        self.laps = []
        self.start_stop_btn.config(text="Start")
        self.lap_btn.config(state="disabled")
        self.lap_listbox.delete(0, tk.END)
        self.time_var.set("00:00.000")
    
    def record_lap(self):
        """Record a lap time"""
        if self.is_running:
            current_time = self.get_current_elapsed_time()
            self.laps.append(current_time)
            lap_number = len(self.laps)
            formatted_time = self.format_time(current_time)
            
            # Calculate split time (time since last lap)
            if lap_number > 1:
                split_time = current_time - self.laps[-2]
                split_formatted = self.format_time(split_time)
                lap_text = f"Lap {lap_number}: {formatted_time} (Split: {split_formatted})"
            else:
                lap_text = f"Lap {lap_number}: {formatted_time}"
            
            self.lap_listbox.insert(tk.END, lap_text)
            # Auto-scroll to bottom
            self.lap_listbox.see(tk.END)
    
    def get_current_elapsed_time(self):
        """Get current elapsed time as float"""
        if self.is_running:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time
    
    def format_time(self, seconds):
        """Format time as MM:SS.mmm"""
        minutes = int(seconds // 60)
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:06.3f}"
    
    def update_display(self):
        """Update the time display"""
        current_time = self.get_current_elapsed_time()
        self.time_var.set(self.format_time(current_time))
        # Update every 10ms for smooth display
        self.parent_frame.after(10, self.update_display)