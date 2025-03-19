"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Presley McFarlane-Goolcharan"
__version__ = "1.0.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def get_account_number() -> int:
    """Prompts the user to input an account number, validates the input
    and returns the account number as an integer.
    
    Returns:
        int: Returns the account the number.
    
    Raises:
        ValueError: Raised if account number entered cannot be parsed into an integer.
        ValueError: Raised if the account number entered does not exist in the "ACCOUNTS" dictionary.

    """
    try:
            acc_num = input(f"Please enter your account number: ")
            try:
                    iter = int(acc_num)
            except ValueError:
                    raise TypeError("Account must be a whole number.")
            
            if iter in ACCOUNTS:
                result = print(iter)
            else:
                raise ValueError("Account number entered does not exist.")
    except TypeError as e:
            result = print(e)
    except ValueError as e:
            result = print(e)
         
    
    return result

get_account_number()
    
"""
def chatbot():
    Performs the Chatbot functionality.
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()
"""