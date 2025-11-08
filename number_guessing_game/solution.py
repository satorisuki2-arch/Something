import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
from game_config import GameConfig
from utils import generate_random_number, format_history_entry, validate_number_input

class NumberGuessingGame:
    """Main game class implementing the Number Guessing Game"""
    
    def __init__(self, root):
        """
        Initialize the game with the main window
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry(f"{GameConfig.WINDOW_WIDTH}x{GameConfig.WINDOW_HEIGHT}")
        self.root.configure(bg=GameConfig.BACKGROUND_COLOR)
        self.root.resizable(False, False)
        
        # Game configuration variables
        self.min_number = GameConfig.MIN_NUMBER
        self.max_number = GameConfig.MAX_NUMBER
        self.max_attempts = GameConfig.MAX_ATTEMPTS
        
        # Game state variables
        self.target_number = 0
        self.attempts = 0
        self.best_score = float('inf')
        self.game_active = False
        self.guess_history = []
        
        # UI component references
        self.guess_entry = None
        self.submit_button = None
        self.feedback_label = None
        self.attempts_label = None
        self.best_score_label = None
        self.history_listbox = None
        self.new_game_button = None
        self.hint_button = None
        
        # Setup method calls
        self.setup_gui()
        self.setup_key_bindings()
        self.new_game()
    
    # === CORE GAME METHODS ===
    
    def setup_gui(self):
        """Create and layout all GUI components"""
        
        # Title label with game name
        title_label = tk.Label(
            self.root,
            text="🎯 Number Guessing Game",
            font=GameConfig.FONTS['title'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg=GameConfig.COLORS['text']
        )
        title_label.pack(pady=20)
        
        # Score display frame
        score_frame = tk.Frame(self.root, bg=GameConfig.BACKGROUND_COLOR)
        score_frame.pack(pady=10)
        
        # Range display
        range_label = tk.Label(
            score_frame,
            text=f"🎲 Guess a number between {self.min_number} and {self.max_number}",
            font=GameConfig.FONTS['heading'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg=GameConfig.COLORS['info']
        )
        range_label.pack()
        
        # Attempts display with color coding
        self.attempts_label = tk.Label(
            score_frame,
            text=f"Attempts: {self.attempts}/{self.max_attempts}",
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg=GameConfig.COLORS['success']
        )
        self.attempts_label.pack(pady=5)
        
        # Best score display
        self.best_score_label = tk.Label(
            score_frame,
            text="Best Score: Not set",
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg=GameConfig.COLORS['warning']
        )
        self.best_score_label.pack()
        
        # Input section with entry and submit button
        input_frame = tk.Frame(self.root, bg=GameConfig.BACKGROUND_COLOR)
        input_frame.pack(pady=30)
        
        tk.Label(
            input_frame,
            text="Enter your guess:",
            font=GameConfig.FONTS['heading'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg=GameConfig.COLORS['text']
        ).pack()
        
        self.guess_entry = tk.Entry(
            input_frame,
            font=GameConfig.FONTS['normal'],
            width=15,
            justify="center",
            relief="solid",
            borderwidth=2
        )
        self.guess_entry.pack(pady=10)
        
        self.submit_button = tk.Button(
            input_frame,
            text="🎯 Submit Guess",
            command=self.submit_guess,
            font=GameConfig.FONTS['heading'],
            bg=GameConfig.COLORS['info'],
            fg="white",
            padx=20,
            pady=10,
            relief="raised",
            borderwidth=2
        )
        self.submit_button.pack(pady=5)
        
        # Feedback display area with appropriate colors
        self.feedback_frame = tk.Frame(self.root, bg=GameConfig.BACKGROUND_COLOR)
        self.feedback_frame.pack(pady=20, fill="x", padx=50)
        
        self.feedback_label = tk.Label(
            self.feedback_frame,
            text="🤔 Make your first guess!",
            font=GameConfig.FONTS['heading'],
            bg=GameConfig.COLORS['warning'],
            fg="white",
            pady=15,
            relief="solid",
            borderwidth=2
        )
        self.feedback_label.pack(fill="x")
        
        # Guess history with scrollable listbox
        history_frame = tk.Frame(self.root, bg=GameConfig.BACKGROUND_COLOR)
        history_frame.pack(pady=20, fill="both", expand=True, padx=50)
        
        tk.Label(
            history_frame,
            text="📋 Guess History:",
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg=GameConfig.COLORS['text']
        ).pack(anchor="w")
        
        # History listbox with scrollbar
        history_container = tk.Frame(history_frame, bg=GameConfig.BACKGROUND_COLOR)
        history_container.pack(fill="both", expand=True, pady=5)
        
        scrollbar = tk.Scrollbar(history_container)
        scrollbar.pack(side="right", fill="y")
        
        self.history_listbox = tk.Listbox(
            history_container,
            font=("Courier", 10),
            yscrollcommand=scrollbar.set,
            relief="solid",
            borderwidth=1,
            bg="#ffffff",
            height=6
        )
        self.history_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.history_listbox.yview)
        
        # Control buttons (New Game, Hint, Quit)
        button_frame = tk.Frame(self.root, bg=GameConfig.BACKGROUND_COLOR)
        button_frame.pack(pady=20)
        
        self.new_game_button = tk.Button(
            button_frame,
            text="🎮 New Game",
            command=self.new_game,
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.COLORS['success'],
            fg="white",
            padx=15,
            pady=8
        )
        self.new_game_button.pack(side="left", padx=10)
        
        self.hint_button = tk.Button(
            button_frame,
            text="💡 Hint",
            command=self.show_hint,
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.COLORS['warning'],
            fg="white",
            padx=15,
            pady=8
        )
        self.hint_button.pack(side="left", padx=10)
        
        reset_button = tk.Button(
            button_frame,
            text="🔄 Reset",
            command=self.reset_game,
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.COLORS['info'],
            fg="white",
            padx=15,
            pady=8
        )
        reset_button.pack(side="left", padx=10)
        
        quit_button = tk.Button(
            button_frame,
            text="❌ Quit",
            command=self.on_window_close,
            font=GameConfig.FONTS['normal'],
            bg=GameConfig.COLORS['error'],
            fg="white",
            padx=15,
            pady=8
        )
        quit_button.pack(side="left", padx=10)
        
        # Instructions/help text
        instructions_frame = tk.Frame(self.root, bg=GameConfig.BACKGROUND_COLOR)
        instructions_frame.pack(pady=10)
        
        instructions = tk.Label(
            instructions_frame,
            text="🎯 First to guess in fewest attempts wins! | Press Enter to submit | Use hints wisely!",
            font=GameConfig.FONTS['small'],
            bg=GameConfig.BACKGROUND_COLOR,
            fg="gray"
        )
        instructions.pack()
    
    def setup_key_bindings(self):
        """Setup keyboard controls"""
        self.guess_entry.bind('<Return>', self.on_enter_key)
        self.root.bind('<Control-n>', lambda e: self.new_game())
        self.root.bind('<Control-h>', lambda e: self.show_hint())
        self.root.bind('<Control-r>', lambda e: self.reset_game())
        self.root.bind('<Control-q>', lambda e: self.on_window_close())
        
        # Set focus to entry field
        self.guess_entry.focus_set()
    
    def new_game(self):
        """Initialize a new game round"""
        
        # Generate new random target number (1-100)
        self.target_number = generate_random_number(self.min_number, self.max_number)
        
        # Reset attempt counter to 0
        self.attempts = 0
        
        # Clear input field and guess history
        self.guess_entry.delete(0, tk.END)
        self.history_listbox.delete(0, tk.END)
        self.guess_history.clear()
        
        # Reset feedback messages
        self.show_feedback("🤔 Make your first guess!", GameConfig.COLORS['warning'])
        
        # Enable input controls
        self.guess_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.hint_button.config(state="normal")
        
        # Set game state to active
        self.game_active = True
        
        # Focus cursor on input field
        self.guess_entry.focus_set()
        
        # Update display
        self.update_display()
        
        print(f"Debug: Target number is {self.target_number}")  # Remove in production
    
    def submit_guess(self):
        """Process and validate player's guess"""
        
        if not self.game_active:
            return
        
        # Get and validate input
        input_text = self.guess_entry.get().strip()
        is_valid, guess, error_message = self.validate_input(input_text)
        
        if not is_valid:
            self.show_feedback(f"❌ {error_message}", GameConfig.COLORS['error'])
            self.guess_entry.delete(0, tk.END)
            return
        
        # Increment attempt counter
        self.attempts += 1
        
        # Compare guess with target number
        feedback = self.calculate_feedback(guess, self.target_number)
        
        # Add guess to history display
        self.add_to_history(guess, feedback)
        
        # Generate appropriate feedback message
        if feedback == "Correct!":
            self.show_feedback("🎉 Congratulations! You found it!", GameConfig.COLORS['success'])
            self.check_game_end()
        elif feedback == "Too High":
            self.show_feedback("📉 Too High! Try a lower number.", GameConfig.COLORS['error'])
        else:  # Too Low
            self.show_feedback("📈 Too Low! Try a higher number.", GameConfig.COLORS['error'])
        
        # Clear input for next guess
        self.guess_entry.delete(0, tk.END)
        
        # Update UI elements accordingly
        self.update_display()
        
        # Check for win/loss conditions
        if self.attempts >= self.max_attempts and feedback != "Correct!":
            self.check_game_end()
    
    def check_game_end(self):
        """Determine if game has ended and handle accordingly"""
        
        if not self.game_active:
            return
        
        # Win Condition: Player guessed correct number
        if self.guess_history and self.guess_history[-1][1] == "Correct!":
            # Update best score if applicable
            self.update_best_score(self.attempts)
            
            # Display victory message
            if self.attempts == self.best_score:
                messagebox.showinfo(
                    "🏆 New Record!",
                    f"New best score: {self.attempts} attempts!\n🎉 Excellent guessing!"
                )
            else:
                messagebox.showinfo(
                    "🎉 You Won!",
                    f"Great job! You found {self.target_number} in {self.attempts} attempts!"
                )
            
            # Disable input controls
            self.guess_entry.config(state="disabled")
            self.submit_button.config(state="disabled")
            self.game_active = False
            
        # Loss Condition: Maximum attempts reached without correct guess
        elif self.attempts >= self.max_attempts:
            # Reveal the target number
            self.show_feedback(
                f"💀 Game Over! The number was {self.target_number}",
                GameConfig.COLORS['error']
            )
            
            # Display game over message
            messagebox.showinfo(
                "😔 Game Over",
                f"Sorry! You've used all {self.max_attempts} attempts.\n"
                f"The number was {self.target_number}.\n\nTry again!"
            )
            
            # Disable input controls
            self.guess_entry.config(state="disabled")
            self.submit_button.config(state="disabled")
            self.game_active = False
    
    # === UI UPDATE METHODS ===
    
    def update_display(self):
        """Refresh all dynamic UI elements"""
        
        # Attempt counter with color coding
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        
        remaining = self.max_attempts - self.attempts
        if remaining <= 2:
            self.attempts_label.config(fg=GameConfig.COLORS['error'])  # Red
        elif remaining <= 5:
            self.attempts_label.config(fg=GameConfig.COLORS['warning'])  # Orange
        else:
            self.attempts_label.config(fg=GameConfig.COLORS['success'])  # Green
        
        # Best score display
        if self.best_score == float('inf'):
            self.best_score_label.config(text="Best Score: Not set")
        else:
            self.best_score_label.config(text=f"Best Score: {self.best_score} attempts")
    
    def show_feedback(self, message, color):
        """Display feedback message to player"""
        self.feedback_label.config(text=message, bg=color)
    
    def add_to_history(self, guess, feedback):
        """Add guess and result to history display"""
        
        # Format: "#3: 45 → Too High"
        history_text = format_history_entry(self.attempts, guess, feedback)
        
        # Add to internal history
        self.guess_history.append((guess, feedback))
        
        # Add to listbox
        self.history_listbox.insert(tk.END, history_text)
        
        # Auto-scroll to bottom
        self.history_listbox.see(tk.END)
        
        # Limit history to reasonable size (optional)
        if self.history_listbox.size() > 20:
            self.history_listbox.delete(0)
    
    # === GAME LOGIC METHODS ===
    
    def validate_input(self, input_text):
        """Validate and convert user input"""
        return validate_number_input(input_text, self.min_number, self.max_number)
    
    def calculate_feedback(self, guess, target):
        """Generate feedback based on guess comparison"""
        if guess == target:
            return "Correct!"
        elif guess > target:
            return "Too High"
        else:
            return "Too Low"
    
    def update_best_score(self, attempts):
        """Update best score if current game is better"""
        if attempts < self.best_score:
            self.best_score = attempts
            self.update_display()
    
    # === HELPER FEATURES ===
    
    def show_hint(self):
        """Provide helpful hint to player"""
        
        if not self.game_active:
            messagebox.showinfo("Game Not Active", "Start a new game first!")
            return
        
        if self.attempts == 0:
            messagebox.showinfo("💡 Hint", "Start with 50 - it's right in the middle!")
            return
        
        # Based on previous guesses: suggest strategy
        if len(self.guess_history) > 0:
            last_guess, last_feedback = self.guess_history[-1]
            
            if last_feedback == "Too High":
                hint = f"🎯 Try a number lower than {last_guess}"
            elif last_feedback == "Too Low":
                hint = f"🎯 Try a number higher than {last_guess}"
            else:
                hint = "🤔 Think about the pattern in your guesses"
        else:
            hint = "🎲 Try the middle of the remaining range"
        
        # Show remaining attempts
        remaining = self.max_attempts - self.attempts
        hint += f"\n💭 You have {remaining} attempts left"
        
        messagebox.showinfo("💡 Hint", hint)
    
    def reset_game(self):
        """Reset entire game to initial state"""
        
        # Clear all scores and statistics
        self.best_score = float('inf')
        self.attempts = 0
        self.target_number = 0
        self.game_active = False
        
        # Clear guess history
        self.guess_history.clear()
        self.history_listbox.delete(0, tk.END)
        
        # Reset all UI elements to defaults
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.hint_button.config(state="normal")
        
        self.show_feedback("🎮 Click 'New Game' to start!", GameConfig.COLORS['info'])
        
        # Update displays
        self.update_display()
        
        # Focus on entry
        self.guess_entry.focus_set()
    
    # === EVENT HANDLERS ===
    
    def on_enter_key(self, event):
        """Handle Enter key press in input field"""
        self.submit_guess()
    
    def on_button_click(self, button_type):
        """Handle various button click events"""
        if button_type == "new_game":
            self.new_game()
        elif button_type == "hint":
            self.show_hint()
        elif button_type == "reset":
            self.reset_game()
        elif button_type == "quit":
            self.on_window_close()
    
    def on_window_close(self):
        """Handle application shutdown gracefully"""
        if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
            self.root.quit()

def main():
    """Main function to initialize and run the game"""
    
    try:
        # Create root window with proper configuration
        root = tk.Tk()
        
        # Initialize game instance
        game = NumberGuessingGame(root)
        
        # Center window on screen
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Start the main event loop
        root.mainloop()
        
    except Exception as e:
        # Handle any startup errors gracefully
        messagebox.showerror("Startup Error", f"Failed to start game: {str(e)}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()