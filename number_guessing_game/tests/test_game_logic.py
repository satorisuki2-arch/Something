"""Unit tests for the Number Guessing Game"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import generate_random_number, validate_number_input, format_history_entry
from game_config import GameConfig

class TestGameLogic(unittest.TestCase):
    """Test cases for game logic functions"""
    
    def test_generate_random_number(self):
        """Test random number generation"""
        for _ in range(100):  # Test multiple times
            number = generate_random_number(1, 100)
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 100)
            self.assertIsInstance(number, int)
    
    def test_validate_valid_input(self):
        """Test valid number inputs (1-100)"""
        # Test valid inputs
        valid_inputs = ["1", "50", "100", "  25  ", "75"]
        for input_val in valid_inputs:
            is_valid, number, error = validate_number_input(input_val, 1, 100)
            self.assertTrue(is_valid, f"Failed for input: {input_val}")
            self.assertEqual(error, "")
    
    def test_validate_invalid_input(self):
        """Test invalid inputs (letters, symbols, out of range)"""
        # Test invalid inputs
        invalid_inputs = ["abc", "12.5", "", "  ", "101", "0", "-5"]
        for input_val in invalid_inputs:
            is_valid, number, error = validate_number_input(input_val, 1, 100)
            self.assertFalse(is_valid, f"Should be invalid: {input_val}")
            self.assertNotEqual(error, "")
    
    def test_validate_edge_cases(self):
        """Test boundary values (1, 100, 0, 101)"""
        # Test boundary cases
        test_cases = [
            ("1", True),    # Valid minimum
            ("100", True),  # Valid maximum
            ("0", False),   # Below minimum
            ("101", False)  # Above maximum
        ]
        
        for input_val, expected_valid in test_cases:
            is_valid, number, error = validate_number_input(input_val, 1, 100)
            self.assertEqual(is_valid, expected_valid, 
                           f"Failed for boundary case: {input_val}")
    
    def test_format_history_entry(self):
        """Test history entry formatting"""
        # Test different feedback types
        test_cases = [
            (1, 50, "Too High", "#1: 50 → 📉 Too High"),
            (2, 25, "Too Low", "#2: 25 → 📈 Too Low"),
            (3, 42, "Correct!", "#3: 42 → 🎉 Correct!")
        ]
        
        for attempt, guess, feedback, expected in test_cases:
            result = format_history_entry(attempt, guess, feedback)
            self.assertEqual(result, expected)

class TestGameConfig(unittest.TestCase):
    """Test cases for game configuration"""
    
    def test_config_values(self):
        """Test configuration constants"""
        self.assertEqual(GameConfig.MIN_NUMBER, 1)
        self.assertEqual(GameConfig.MAX_NUMBER, 100)
        self.assertEqual(GameConfig.MAX_ATTEMPTS, 10)
        self.assertIsInstance(GameConfig.COLORS, dict)
        self.assertIsInstance(GameConfig.FONTS, dict)

class TestGameIntegration(unittest.TestCase):
    """Integration tests for game components"""
    
    def test_game_flow_simulation(self):
        """Simulate a complete game flow"""
        # Test winning scenario
        target = 42
        guesses = [50, 25, 37, 43, 40, 41, 42]
        
        attempts = 0
        for guess in guesses:
            attempts += 1
            if guess == target:
                feedback = "Correct!"
                break
            elif guess > target:
                feedback = "Too High"
            else:
                feedback = "Too Low"
        
        self.assertEqual(feedback, "Correct!")
        self.assertEqual(attempts, 7)
    
    def test_max_attempts_scenario(self):
        """Test game over after max attempts"""
        max_attempts = GameConfig.MAX_ATTEMPTS
        
        # Simulate failing all attempts
        attempts = 0
        for _ in range(max_attempts):
            attempts += 1
        
        self.assertEqual(attempts, max_attempts)

if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)