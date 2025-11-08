"""Configuration constants for the Number Guessing Game"""

class GameConfig:
    """Configuration constants for the game"""
    
    # Game Settings
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    MAX_ATTEMPTS = 10
    
    # UI Settings
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 650
    BACKGROUND_COLOR = "#e8f4fd"
    
    # Colors
    COLORS = {
        'success': '#27ae60',   # Green
        'error': '#e74c3c',     # Red
        'warning': '#f39c12',   # Orange
        'info': '#3498db',      # Blue
        'text': '#2c3e50'       # Dark Gray
    }
    
    # Fonts
    FONTS = {
        'title': ('Arial', 24, 'bold'),
        'heading': ('Arial', 14, 'bold'),
        'normal': ('Arial', 12),
        'small': ('Arial', 10)
    }
    
    # Messages
    MESSAGES = {
        'welcome': '🤔 Make your first guess!',
        'too_high': '📉 Too High! Try a lower number.',
        'too_low': '📈 Too Low! Try a higher number.',
        'correct': '🎉 Congratulations! You found it!',
        'game_over': '💀 Game Over! The number was {}',
        'invalid_input': '❌ Please enter a valid number between {} and {}!',
        'out_of_range': '❌ Number must be between {} and {}!',
        'not_a_number': '❌ Please enter a valid number!'
    }
    
    # Hints
    HINTS = {
        'first_guess': 'Start with 50 - it\'s right in the middle!',
        'strategy': 'Think about the pattern in your guesses',
        'range_tip': 'Try the middle of the remaining range',
        'encouragement': 'You\'re getting closer! Keep trying!'
    }