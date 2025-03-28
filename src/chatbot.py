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
        TypeError: Raised if account number entered cannot be parsed into an integer.
        ValueError: Raised if the account number entered does not exist in the "ACCOUNTS" dictionary.
    """
    
    acc_num = input("Please enter your account number: ")
    try: 
            acc_num = int(acc_num)
    except ValueError:
            raise TypeError("Account number must be a whole number.")
    if acc_num not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    return acc_num


def get_amount() -> float:
    """Prompts the user to input the amount to deposit and return the amount as float.
    
    Returns: 
        float: Returns the amount to deposit.
    
    Raises:
        ValueError: Raised if deposit amount entered cannot be parsed into an integer.
        ValueError: Raised if deposit amount is 0 or a negative value.
    """

    dep_num = input("Enter an amount: ")
    try:
            dep_num = float(dep_num)
    except ValueError:
            raise ValueError("Amount must be a numeric type.")
    if dep_num == 0:
        raise ValueError("Amount must be a value greater than zero.")
    elif dep_num < 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    return dep_num

def get_balance(acc_num: int) -> str:
    """Returns a message containing the balance of the specified account number and returns the message as str.
    
    Returns
        str: " Your current balance for account {account-number} is {balance-formatted-as-currency}."
    
    Raises:
        TypeError: Raised if value of the parameter is not an integer type.
        ValueError: Raised if the specified account number does not exist in the ACCOUNTS dictionary.
    """
    try:
            acc_num = int(acc_num)
    except ValueError:
            raise TypeError('Account number must be an int type.')
    if acc_num not in ACCOUNTS:
          raise ValueError('Account number does not exist.')
    balance = ACCOUNTS[acc_num]["balance"]

    return (f"Your current balance for account {acc_num} is ${balance:,.2f}")

def make_deposit(acc_num: int, dep_num: int) -> str:
    """Returns an increased bank accounts balance by a specified amount as str.

    Returns:
        str: "You have made a deposit of {account-balance-formatted as currency} to account {account-number}.
    
    Raises:
        TypeError: Raised if the value of the parameter is not an integer type.
        ValueError: Raised if the specified account number does not exists in the ACCOUNTS dictionary.
        ValueError: Raised if the amount entered is not numeric type (not int or float).
        ValueError: Raised if the amount entered is zero or a negative value.
    """
    try:
            acc_num = int(acc_num)
    except ValueError:
            raise TypeError('Account number must be an int type.')
    try:
            dep_num = float(dep_num)
    except ValueError:
            raise ValueError('Amount must be a numeric type.')
    if acc_num not in ACCOUNTS:
        raise ValueError('Account number does not exist.')
    elif dep_num == 0:
          raise ValueError('Amount must be a value greater than zero.')
    elif dep_num < 0:
          raise ValueError('Amount must be a value greater than zero.')


    return (f"You have made a deposit of ${dep_num:,.2f} to account {acc_num}.")

def get_task() -> str:
    """Prompts the user to input a task and returns the task as str.

    Returns:
        str: Returns the task entered by the user.
    
    Raises:
        ValueError: Raised if input is not in VALID_TASKS list.
    """
    task = input("What would you like to do (balance/deposit/exit)?: ")
    task = task.lower()
    if task in VALID_TASKS:
        return task
    else:
        raise ValueError(f'"{task}" is an unknown task.')


def chatbot():
    # Performs the Chatbot functionality.
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")
    while True:
        # Menu Selection
        try:
                task = get_task()
        except ValueError as e:
                print(f"Error: {e}")
                continue
        # Exit Task
        if task == "exit":
            break
        # Account number input
        try:
                acc_num = get_account_number()
        # get_account_number error message
        except (TypeError, ValueError) as e:
                print(f"Error: {e}")
                continue
        # Deposit Task
        if task == "deposit":
            try:
                    amount = get_amount()
                    message = make_deposit(acc_num, amount)
                    print(message)
            # make_deposit() error message
            except ValueError as e:
                    print(f"Error: {e}")
                    continue
        # Balance Task
        elif task == "balance":
            try:
                balance_message = get_balance(acc_num)
                print(balance_message)
            # get_balance() error message
            except (TypeError, ValueError) as e:
                print(f"Error: {e}")
                continue
    

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()
