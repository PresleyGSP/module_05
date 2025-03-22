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
from src.chatbot import get_balance
from src.chatbot import make_deposit
from src.chatbot import get_task

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
    # Testing for non numeric parameter
    def test_get_balance_non_numeric(self):
        # Arrange
        acc_num = "Presley"
        expected = "Account number must be an int type."
        # Act and Assert
        with self.assertRaises(TypeError) as context:
            get_balance(acc_num)
            
        self.assertEqual(str(context.exception), expected)
    # Testing for non account number
    def test_get_balance_not_account(self):
        # Arrange
        acc_num = 222222
        expected = "Account number does not exist."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            get_balance(acc_num)
        
        self.assertEqual(str(context.exception), expected)
    # Testing for valid account number
    def test_get_balance_valid_input(self):
        # Arrange
        acc_num = 123456
        expected = "Your current balance for account 123456 is $1,000.00"
        # Act
        actual = get_balance(acc_num)
        # Assert
        self.assertEqual(expected, actual)
# TESTING make_deposit()
    # Testing for non numeric account number
    def test_make_deposit_account_not_int(self):
        # Arrange
        acc_num = "Presley"
        dep_num = 400
        expected = "Account number must be an int type."
        # Act and Assert
        with self.assertRaises(TypeError) as context:
            make_deposit(acc_num, dep_num)
        
        self.assertEqual(str(context.exception), expected)
    # Testing for not an account number
    def test_make_deposit_not_account(self):
        # Arrange
        acc_num = 123455
        dep_num = 1000
        expected = "Account number does not exist."
        # Act an Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(acc_num, dep_num)

        self.assertEqual(str(context.exception), expected)
    # Testing for non numeric deposit
    def test_make_deposit_non_numeric_deposit(self):
        # Arrange
        acc_num = 123456
        dep_num = "Presley"
        expected = "Amount must be a numeric type."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(acc_num, dep_num)

        self.assertEqual(str(context.exception), expected)
    # Testing for deposit amount is zero
    def test_make_deposit_zero(self):
        # Arrange
        acc_num = 123456
        dep_num = 0
        expected = "Amount must be a value greater than zero."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(acc_num, dep_num)

        self.assertEqual(str(context.exception), expected)
    # Testing if deposit amount is less than zero
    def test_make_deposit_negative(self):
        # Arrange
        acc_num = 123456
        dep_num = -1
        expected = "Amount must be a value greater than zero."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(acc_num, dep_num)

        self.assertEqual(str(context.exception), expected)
    # Testing when all parameters are valid
    def test_make_deposit_valid(self):
        # Arrange
        acc_num = 123456
        dep_num = 1000
        expected = "You have made a deposit of $1,000.00 to account 123456."
        # Act
        actual = make_deposit(acc_num, dep_num)
        # Assert
        self.assertEqual(actual, expected)
# TESTING get_task()
    # Testing for invalid task
    def test_get_task_not_valid(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["Presley"]
            expected = '"presley" is an unknown task.'
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_task()
            
            self.assertEqual(str(context.exception), expected)
    # Testing for valid task
    def test_get_task_valid(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["deposit"]
            expected = "deposit"
            # Act
            actual = get_task()
            # Assert
            self.assertEqual(expected, actual)
    # Testing when valid lowercase user selection is entered
    def test_get_task_selection_lowercase(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["DEPOSIT"]
            expected = "deposit"
            # Act
            actual = get_task()
            # Assert
            self.assertEqual(expected, actual)

            

                         

if __name__ == "__main__":
    unittest.main()