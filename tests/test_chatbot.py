"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "Presley McFarlane-Goolcharan"
__version__ = "1.0.2025"

import unittest
from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS
# Importing functions to be tested
from src.chatbot import get_account_number
from src.chatbot import get_amount

class TestReverseString(unittest.TestCase):
    # TESTING get_account
    # Testing for non integer datatype
    def test_get_account_number_value_error_not_whole_number(self):
    
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["Presley"]
            expected = "Account number must be a whole number."
            # Act and Assert 
            with self.assertRaises(TypeError) as context:
                get_account_number()

            self.assertEqual(str(context.exception), expected)
    # Testing for account number not in ACCOUNTS
    def test_get_account_number_value_error_not_an_account_number(self):

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["123444"]
            expected = "Account number entered does not exist."
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account_number()

            self.assertEqual(str(context.exception), expected)
    # Testing for valid account number
    def test_get_account_number_is_valid(self):

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["123456"]
            expected = 123456
            # Act
            actual = get_account_number()

            # Assert
            self.assertEqual(expected, actual)
    # TESTING get_amount
    # Testing for non-numeric input
    def test_get_amount_value_error_not_numeric(self):

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["Presley"]
            expected = "Amount must be a numeric type."
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            
            self.assertEqual(str(context.exception), expected)
    # Testing for input = 0
    def test_get_amount_value_error_input_zero(self):

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["0"]
            expected = "Amount must be a value greater than zero."
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()

            self.assertEqual(str(context.exception), expected)
    # Testing for negative input
    def test_get_amount_value_error_input_negative(self):

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["-1"]
            expected = "Amount must be a value greater than zero."
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            
            self.assertEqual(str(context.exception), expected)
    # Testing for valid input
    def test_get_amount_valid_input(self):

        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["2000"]
            expected = 2000
            # Act
            actual = get_amount()
            # Assert
            self.assertEqual(expected, actual)
    # TESTING get_balance
                         

if __name__ == "__main__":
    unittest.main()