# Module 5 Assignment

## Description

In this assignment I will demonstrate the use of defining functions and unit testing

## Author

Presley McFarlane-Goolcharan

## Code Modification 1

- Added account number validation to "get_account_number()" function.

## Code Modification 2

- Fixed "get_account_number" function so it does not print to console, it returns just the "acc_num" variable and it does not trigger input when testing the itself.
- Added unit testing for function "get_account_number".

## Code Modification 3

- Added deposit validation to "get_amount()" function.

## Code Modification 4

- Added unit testing for function "get_amount()".

## Code Modification 5

- Added balance validation to "get_balance()" function.

## Code Modification 6

- Added unit testing for function "get_balance()" function.

## Code Modification 7

- Added function "make_deposit()" that increases accounts balance by a specified amount.

## Code Modification 8

- Added unit testing for function "make_deposit()" function.

## Code Modification 9

- Added function "get_task()" that returns a valid task selected by the user.
- Added unit testing for "get_task()" function.

## Code Modification 10

- Completed "chatbot()" function using all previously made functions.

## Reflection

### 1. Identify any challenges or issues you encountered while writing your functions.

- While writing the first function I had issues with nesting the input function, it was being called when I was testing even though I mocked the input.
- While testing the functions, numerous times it ran 0 tests, I had to add in at the end of my code "if __name__ == "__main__": unittest.main()" so the tests ran.
- Finding the balance in the "ACCOUNTS" dictionary, I had to access the list within the list which I found out how to do.

### 2. Discuss the benefits and challenges of developing and using unit tests.

- It makes creating larger programs easier to tackle, you break them down into smaller steps/components and fit them together like a puzzle.
- Sometime the way you are unit testing can be the error and not the function you wrote, this can throw off your program.
- With unit testing you are sure that program achieves the specified results with every outcome.
