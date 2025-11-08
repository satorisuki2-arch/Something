# 🎯 Number Guessing Game - Programming Assignment

**Assignment ID:** NUG-001  
**Course:** Introduction to GUI Programming with Python  
**Assigned Date:** 2025-07-07  
**Due Date:** 2025-07-14  
**Student:** valbenia  
**Difficulty Level:** Beginner  
**Estimated Time:** 4-6 hours  

---

## 📋 Assignment Overview

### 🎯 **Objective:**
Create a complete Number Guessing Game using Python's Tkinter library. This assignment will test your understanding of GUI programming, event handling, game logic, and user experience design.

### 🎮 **Game Description:**
The computer will randomly select a number between 1 and 100. The player has 10 attempts to guess the correct number. After each guess, the game provides feedback ("Too High" or "Too Low") to help the player narrow down their next guess. The game tracks the best score (fewest attempts) and maintains a history of all guesses.

### 📚 **Learning Goals:**
- Master Tkinter GUI components and layout management
- Implement event-driven programming with user input validation
- Design game state management and flow control
- Create engaging user experience with visual feedback
- Practice object-oriented programming principles

---

## 🏗️ Code Structure Requirements

### 📁 **File Organization:**
```
number_guessing_game/
├── main.py                    # Main game implementation
├── game_config.py             # Game configuration constants
├── ui_components.py           # Custom UI components (optional)
├── utils.py                   # Helper functions (optional)
└── README.md                  # Documentation
```

### 🎯 **Class Structure:**

```python
class NumberGuessingGame:
    """Main game class implementing the Number Guessing Game"""
    
    def __init__(self, root):
        """
        Initialize the game with the main window
        
        Args:
            root: Tkinter root window
        
        Required Initializations:
        - Game configuration variables
        - UI component references
        - Game state variables
        - Setup method calls
        """
        pass
    
    # === CORE GAME METHODS ===
    
    def setup_gui(self):
        """
        Create and layout all GUI components
        
        Required Components:
        - Title label with game name
        - Score display frame
        - Input section with entry and submit button
        - Feedback display area
        - Guess history with scrollable listbox
        - Control buttons (New Game, Hint, Quit)
        - Instructions/help text
        
        Layout Requirements:
        - Professional appearance with consistent styling
        - Proper spacing and alignment
        - Color scheme for visual appeal
        - Responsive design elements
        """
        pass
    
    def new_game(self):
        """
        Initialize a new game round
        
        Required Actions:
        - Generate new random target number (1-100)
        - Reset attempt counter to 0
        - Clear input field and guess history
        - Reset feedback messages
        - Enable input controls
        - Set game state to active
        - Focus cursor on input field
        """
        pass
    
    def submit_guess(self):
        """
        Process and validate player's guess
        
        Required Validations:
        - Check if input is a valid integer
        - Verify number is within valid range (1-100)
        - Ensure game is currently active
        
        Required Processing:
        - Increment attempt counter
        - Compare guess with target number
        - Generate appropriate feedback message
        - Add guess to history display
        - Check for win/loss conditions
        - Update UI elements accordingly
        """
        pass
    
    def check_game_end(self):
        """
        Determine if game has ended and handle accordingly
        
        Win Condition:
        - Player guessed correct number
        - Update best score if applicable
        - Display victory message
        - Disable input controls
        
        Loss Condition:
        - Maximum attempts (10) reached without correct guess
        - Reveal the target number
        - Display game over message
        - Disable input controls
        """
        pass
    
    # === UI UPDATE METHODS ===
    
    def update_display(self):
        """
        Refresh all dynamic UI elements
        
        Required Updates:
        - Attempt counter with color coding
        - Best score display
        - Feedback message with appropriate colors
        - Guess history scrolling to latest entry
        """
        pass
    
    def show_feedback(self, message, color):
        """
        Display feedback message to player
        
        Args:
            message (str): Feedback text to display
            color (str): Text color for the message
        
        Message Types:
        - "Too High" with red color
        - "Too Low" with red color  
        - "Correct!" with green color
        - "Invalid input" with orange color
        """
        pass
    
    def add_to_history(self, guess, feedback):
        """
        Add guess and result to history display
        
        Args:
            guess (int): The number guessed
            feedback (str): Result of the guess
        
        Format: "#3: 45 → Too High"
        Requirements:
        - Include attempt number
        - Show guess and feedback
        - Auto-scroll to bottom
        - Limit history to reasonable size
        """
        pass
    
    # === GAME LOGIC METHODS ===
    
    def validate_input(self, input_text):
        """
        Validate and convert user input
        
        Args:
            input_text (str): Raw input from entry field
            
        Returns:
            tuple: (is_valid: bool, number: int, error_message: str)
        
        Validation Rules:
        - Must be a valid integer
        - Must be between 1 and 100 (inclusive)
        - Handle empty input gracefully
        """
        pass
    
    def calculate_feedback(self, guess, target):
        """
        Generate feedback based on guess comparison
        
        Args:
            guess (int): Player's guess
            target (int): Target number
            
        Returns:
            str: Feedback message ("Too High", "Too Low", or "Correct!")
        """
        pass
    
    def update_best_score(self, attempts):
        """
        Update best score if current game is better
        
        Args:
            attempts (int): Number of attempts in current game
            
        Requirements:
        - Only update if fewer attempts than previous best
        - Handle first game (no previous score)
        - Persist best score during session
        """
        pass
    
    # === HELPER FEATURES ===
    
    def show_hint(self):
        """
        Provide helpful hint to player
        
        Hint Types:
        - For first guess: suggest starting with 50
        - Based on previous guesses: suggest strategy
        - Show remaining attempts
        - Encourage with motivational messages
        """
        pass
    
    def reset_game(self):
        """
        Reset entire game to initial state
        
        Reset Actions:
        - Clear all scores and statistics
        - Reset best score display
        - Clear guess history
        - Return to new game state
        - Reset all UI elements to defaults
        """
        pass
    
    # === EVENT HANDLERS ===
    
    def on_enter_key(self, event):
        """Handle Enter key press in input field"""
        pass
    
    def on_button_click(self, button_type):
        """Handle various button click events"""
        pass
    
    def on_window_close(self):
        """Handle application shutdown gracefully"""
        pass

# === CONFIGURATION CLASS ===

class GameConfig:
    """Configuration constants for the game"""
    
    # Game Settings
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    MAX_ATTEMPTS = 10
    
    # UI Settings
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 600
    BACKGROUND_COLOR = "#e8f4fd"
    
    # Colors
    COLORS = {
        'success': '#27ae60',
        'error': '#e74c3c', 
        'warning': '#f39c12',
        'info': '#3498db',
        'text': '#2c3e50'
    }
    
    # Fonts
    FONTS = {
        'title': ('Arial', 24, 'bold'),
        'heading': ('Arial', 14, 'bold'),
        'normal': ('Arial', 12),
        'small': ('Arial', 10)
    }

# === UTILITY FUNCTIONS ===

def generate_random_number(min_val, max_val):
    """Generate random number within specified range"""
    pass

def format_history_entry(attempt_num, guess, feedback):
    """Format guess history entry for display"""
    pass

def validate_number_input(text, min_val, max_val):
    """Validate numeric input within range"""
    pass

# === MAIN EXECUTION ===

def main():
    """
    Main function to initialize and run the game
    
    Requirements:
    - Create root window with proper configuration
    - Initialize game instance
    - Set window properties (title, size, centering)
    - Start the main event loop
    - Handle any startup errors gracefully
    """
    pass

if __name__ == "__main__":
    main()
```

---

## ✅ Implementation Requirements

### 🎯 **Core Functionality (70 points):**

#### 1. **Game Logic (25 points)**
- ✅ Generate random number between 1-100
- ✅ Accept and validate user input
- ✅ Compare guess with target number
- ✅ Provide "Too High" or "Too Low" feedback
- ✅ Track attempt count (max 10)
- ✅ Detect win/loss conditions
- ✅ Handle edge cases (invalid input, out of range)

#### 2. **User Interface (25 points)**
- ✅ Professional layout with proper spacing
- ✅ Clear title and instructions
- ✅ Input field with submit button
- ✅ Real-time feedback display
- ✅ Attempt counter with visual indicators
- ✅ Scrollable guess history
- ✅ Control buttons (New Game, Hint, Quit)

#### 3. **User Experience (20 points)**
- ✅ Intuitive and responsive interface
- ✅ Visual feedback with appropriate colors
- ✅ Keyboard support (Enter to submit)
- ✅ Clear error messages and validation
- ✅ Smooth game flow and transitions
- ✅ Help/hint system for guidance

### 🌟 **Advanced Features (20 points):**

#### 4. **Enhanced Functionality (10 points)**
- ✅ Best score tracking across games
- ✅ Guess history with formatted display
- ✅ Hint system with strategic advice
- ✅ Game statistics and analytics

#### 5. **Polish and Extras (10 points)**
- ✅ Consistent visual design and theming
- ✅ Smooth animations or transitions
- ✅ Sound effects (optional)
- ✅ Difficulty levels or customization

### 📝 **Code Quality (10 points)**
- ✅ Clean, readable code with proper comments
- ✅ Object-oriented design principles
- ✅ Error handling and edge cases
- ✅ Modular structure and organization

---

## 📊 Grading Rubric

| Component | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D/F) |
|-----------|---------------|----------|------------------|------------------|
| **Game Logic** | All features work perfectly, handles edge cases | Core functionality works, minor issues | Basic features work, some bugs | Major functionality missing |
| **User Interface** | Professional, polished design | Clean, functional layout | Basic but usable interface | Poor layout or missing elements |
| **User Experience** | Intuitive, engaging, smooth | Good usability, clear feedback | Functional but basic | Confusing or frustrating |
| **Code Quality** | Clean, well-documented, modular | Good structure, readable | Adequate organization | Poor structure, hard to follow |
| **Requirements** | All requirements met plus extras | Most requirements completed | Basic requirements met | Many requirements missing |

### 🎯 **Grade Breakdown:**
- **A (90-100):** All requirements + advanced features + excellent code quality
- **B (80-89):** All core requirements + good implementation + minor issues
- **C (70-79):** Most requirements met + functional but basic implementation
- **D/F (<70):** Major requirements missing or non-functional code

---

## 📚 Resources and References

### 🔗 **Required Reading:**
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Tkinter Tutorial - Real Python](https://realpython.com/python-gui-tkinter/)
- [GUI Programming Best Practices](https://wiki.python.org/moin/TkInter)

### 💡 **Helpful Examples:**
- Event handling with Tkinter
- Input validation techniques
- Layout management (pack, grid, place)
- Color schemes and styling

### 🛠️ **Development Tools:**
- Python 3.7+ with Tkinter
- Code editor (VS Code, PyCharm, etc.)
- Git for version control (recommended)

---

## 📝 Submission Guidelines

### 📦 **What to Submit:**
1. **Source Code** - All Python files with proper documentation
2. **README.md** - Setup instructions and feature description
3. **Screenshots** - Key game screens and functionality
4. **Test Cases** - Unit tests or test documentation
5. **Reflection** - 1-2 page report on challenges and learning

### 📅 **Submission Format:**
- ZIP file named: `valbenia_number_guessing_game.zip`
- Submit via course management system
- Include all required files and documentation

### ⏰ **Late Policy:**
- 10% deduction per day late
- No submissions accepted after 1 week
- Contact instructor for extensions with valid reasons

---

## 🤝 Academic Integrity

### ✅ **Allowed:**
- Using course materials and provided examples
- Consulting Python/Tkinter documentation
- Discussing general concepts with classmates
- Getting help with debugging specific issues

### ❌ **Not Allowed:**
- Copying code from online sources without attribution
- Sharing complete solutions with other students
- Using AI code generators for entire implementations
- Submitting work that is not your own

---

## 💬 Getting Help

### 🆘 **Support Channels:**
- **Office Hours:** Tuesdays 2-4 PM, Thursdays 10-12 PM
- **Discussion Forum:** Post questions and help classmates
- **Email:** instructor@university.edu (48-hour response time)
- **Study Groups:** Encourage peer learning and collaboration

### 🎯 **Tips for Success:**
1. **Start Early** - Begin with basic functionality and add features incrementally
2. **Test Frequently** - Verify each feature works before moving to the next
3. **Read Documentation** - Understand Tkinter widgets and their properties
4. **Plan Your Design** - Sketch the UI layout before coding
5. **Ask Questions** - Don't hesitate to seek help when stuck

---

**Good luck with your Number Guessing Game implementation!** 🎮✨

*Remember: The goal is to learn GUI programming concepts while creating an engaging and functional game. Focus on understanding the principles rather than just completing the requirements.*

---

**Assignment Generated:** 2025-07-07 10:30:44 UTC  
**Student:** valbenia  
**File:** NumberGuessingGame_Assignment.md