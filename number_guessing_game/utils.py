"""Helper functions for the Number Guessing Game"""

import random

def generate_random_number(min_val, max_val):
    """
    Generate random number within specified range
    
    Args:
        min_val (int): Minimum value (inclusive)
        max_val (int): Maximum value (inclusive)
        
    Returns:
        int: Random number within range
    """
    return random.randint(min_val, max_val)

def format_history_entry(attempt_num, guess, feedback):
    """
    Format guess history entry for display
    
    Args:
        attempt_num (int): Current attempt number
        guess (int): The number guessed
        feedback (str): Result of the guess
        
    Returns:
        str: Formatted history entry
    """
    emoji_map = {
        "Too High": "📉",
        "Too Low": "📈", 
        "Correct!": "🎉"
    }
    
    emoji = emoji_map.get(feedback, "❓")
    return f"#{attempt_num}: {guess} → {emoji} {feedback}"

def validate_number_input(text, min_val, max_val):
    """
    Validate numeric input within range
    
    Args:
        text (str): Input text to validate
        min_val (int): Minimum allowed value
        max_val (int): Maximum allowed value
        
    Returns:
        tuple: (is_valid: bool, number: int, error_message: str)
    """
    # Handle empty input
    if not text.strip():
        return False, 0, "Please enter a number!"
    
    # Try to convert to integer
    try:
        number = int(text.strip())
    except ValueError:
        return False, 0, "Please enter a valid number!"
    
    # Check range
    if number < min_val or number > max_val:
        return False, number, f"Number must be between {min_val} and {max_val}!"
    
    return True, number, ""

def calculate_optimal_guess(guesses_history, min_val, max_val):
    """
    Calculate optimal next guess based on history (bonus feature)
    
    Args:
        guesses_history (list): List of (guess, feedback) tuples
        min_val (int): Current minimum possible value
        max_val (int): Current maximum possible value
        
    Returns:
        int: Suggested optimal guess
    """
    if not guesses_history:
        return (min_val + max_val) // 2
    
    # Update range based on history
    current_min = min_val
    current_max = max_val
    
    for guess, feedback in guesses_history:
        if feedback == "Too High":
            current_max = min(current_max, guess - 1)
        elif feedback == "Too Low":
            current_min = max(current_min, guess + 1)
    
    # Return middle of remaining range
    return (current_min + current_max) // 2

def get_encouragement_message(attempts, max_attempts):
    """
    Get encouragement message based on attempts
    
    Args:
        attempts (int): Current attempt count
        max_attempts (int): Maximum allowed attempts
        
    Returns:
        str: Encouragement message
    """
    remaining = max_attempts - attempts
    
    if remaining >= 7:
        return "🌟 Great start! You have plenty of attempts left!"
    elif remaining >= 4:
        return "💪 Keep going! You're doing well!"
    elif remaining >= 2:
        return "⏰ Time to focus! You can do this!"
    else:
        return "🔥 Last chance! Make it count!"